from django.urls import path, include

from folders import views

urlpatterns = [
    path('folders/', views.FolderView.as_view()),
    path('document/', views.DocumentView.as_view()),
    path('document/<int:id>/', views.DocumentView.as_view()),
    path('edit-document/<int:id>/', views.DocumentView.as_view()),
    path('delete-document/<int:id>/', views.DocumentView.as_view()),
    path('pending-document/',views.PendingDocumentView.as_view()),
    path('disabled-document/',views.DisabledDocumentView.as_view()),
    path('get-document/<str:ref_num>/', views.GetDocumentRefView.as_view()),
    path('get-document-count/', views.DocumentStatusCountView.as_view())
]