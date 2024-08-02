from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def upload_file_view(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.method == "POST" and request.FILES.get("myfile"):
        file: InMemoryUploadedFile = request.FILES['myfile']
        if file.size < 1000000:
            fs = FileSystemStorage()
            fs.save(file.name, file)
            print(type(file), file.size)
        else:
            context['exception_text'] = "Файл превышает заданный лимит"
        # size_file = fs.size(file.name)
    return render(request, "requestdataapp/uploadfile.html", context=context)

