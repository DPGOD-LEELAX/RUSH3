from rest_framework import serializers

from .models import Folders
from .models import Documents

class FolderListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = Folders
        fields = [
            'id',
            'name',
            'is_parent',
            'is_child',
            'parent',
            'created_at',
            'children'
        ]
    def get_children(self, obj):
        children = Folders.objects.filter(parent=obj)
        if children.exists():
            return FolderListSerializer(children, many=True).data
        return []
    
class DocumentSerializer(serializers.ModelSerializer):
    to_username = serializers.CharField(source='assigned_to.username', read_only=True)
    from_username = serializers.CharField(source='from_person.username', read_only=True)
    status_display = serializers.SerializerMethodField()
    class Meta:
        model =  Documents
        fields = '__all__'
        
    def get_status_display(self, obj):
        return obj.get_status_display()