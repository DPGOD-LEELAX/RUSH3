from .serializers import FolderListSerializer
from .serializers import DocumentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from django.db.models import Count
from .models import Folders,Documents

import os
from django.conf import settings

class FolderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        data = Folders.objects.filter(is_parent=True, is_child=False).order_by('id')
        serializer = FolderListSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = FolderListSerializer(data = data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DocumentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):
        if id:
            try:
                document = Documents.objects.get(id=id)
                serializer = DocumentSerializer(document)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Documents.DoesNotExist:
                return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        
        documents = Documents.objects.exclude(status__in=['disable', 'pending']).order_by('id')
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Document creation failed',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            document = Documents.objects.get(id=kwargs['id'])
            serializer = DocumentSerializer(document, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Documents.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            document = Documents.objects.get(id=kwargs['id'])
        except Documents.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)

        if document.status != 'disable':
            document.status = 'disable'
            document.save()
            serializer = DocumentSerializer(document)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Delete document file after deletion from DB
        file_path = os.path.join(settings.MEDIA_ROOT, document.file.name)
        document.delete()
        if document.file and os.path.exists(file_path):
            os.remove(file_path)
        return Response({'message': 'Document deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
class PendingDocumentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        data = Documents.objects.filter(status='pending').order_by('id')
        serializer = DocumentSerializer(data, many=True)
        return Response(serializer.data)
class DisabledDocumentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        data = Documents.objects.filter(status='disable').order_by('id')
        serializer = DocumentSerializer(data, many=True)
        return Response(serializer.data)
class GetDocumentRefView(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request, **kwargs):
        try:
            data = Documents.objects.get(reference_number=kwargs['ref_num'])
        except Documents.DoesNotExist:
            return Response({'error':'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(data)
        return Response(serializer.data)
    
class DocumentStatusCountView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwargs):
        try:
            total_documents = Documents.objects.count()

            status_counts = Documents.objects.values('status').annotate(count=Count('status')).order_by('status')

            status_display_map = dict(Documents.STATUS_CHOICES)

            formatted_status_counts = [
                {
                    'name': status_display_map.get(item['status'], item['status']),
                    'count': item['count']
                }
                for item in status_counts
            ]

            if not formatted_status_counts:
                return Response({'error': 'No documents found'}, status=status.HTTP_404_NOT_FOUND)

            return Response({
                'total_documents': total_documents,
                'status_counts': formatted_status_counts
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)