from django.urls import path, include

from .views import upload_file_view

app_name = "requestdataapp"


urlpatterns = [
    path('file/', upload_file_view, name='fileupload'),
]
