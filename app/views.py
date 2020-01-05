from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# upload_image에서 form을 사용하기 위해 import
from .forms import ImageForm
from .models import ImageData


def tweet_image(request):
    tweetimage = ImageData.objects.all().order_by('-create_dt')

    paginator = Paginator(tweetimage, 9)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'image_gallery.html', {
        # 'images' : tweetimage,
        'images': contacts
    })


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweet_image')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {
        'image_form': form
    })


# def index(request):
#     return render(request, 'grid-gallery.html')

