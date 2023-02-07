from django.conf.urls.static import static
from django.urls import path

from config import settings
from dl import views

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='upload'),
    path('upload/', views.FileUploadViewByForm.as_view(), name='form_upload'),
    path('list/', views.FileListView.as_view(), name='list'),
    path('<int:pk>/', views.FileDownloadView.as_view(), name='download'),
    path('update/<int:pk>/', views.FileUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.FileDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
