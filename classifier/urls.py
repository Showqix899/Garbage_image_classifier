from django.urls import path
from .views import UploadImageAPIView,ListImagesView

urlpatterns = [
    path('upload/', UploadImageAPIView.as_view(), name='upload-image'),
    path('images/', ListImagesView.as_view(), name='list-images'),

]
