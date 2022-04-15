from django.shortcuts import render
from .forms import SubscriberForm
from parts.models import Part
from django.contrib import messages
# from utils.uploadings import UploadingParts

def main(request):
    # form = SubscriberForm(request.POST or None)
    # if request.method == 'POST' and form.is_valid():
    #     form.save()
    parts = Part.objects.filter()
    return render(request, 'main.html', locals())


def about(request):
    return render(request, 'about.html')


# def download_parts(request):
#     if request.method == 'POST':
#         file = request.FILES['file']
#         uploading_file = UploadingParts({"file": file})
#         if uploading_file:
#             messages.success(request, 'Успешная загрузка')
#         else:
#             messages.error(request, 'Ошибка при загрузке')
#     return render(request, 'download_parts.html', locals())
