import json

import math
import os
import cv2
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from backend.settings import STATIC_URL


# home page,return html.
def home(request):
    dimension = cache.get('dimension')

    return render(request, 'index.html', {'dimensions': dimension})


# process gray scale request
def grayscale_process(request, pk):
    # search for image already grayed
    image_names = os.listdir('gray')
    for image in image_names:
        # if images already grayed
        if str(pk) == image.split('_')[1].split('-')[0]:
            return HttpResponse(content=STATIC_URL + image, status=200)

    # images not be grayed
    grayscale = request.GET.get('grayscale', default=None)
    # if grayscale param in request
    if grayscale != None:
        # find in cached images directory
        image_names = os.listdir('images')
        for image in image_names:
            if str(pk) == image.split('-')[0]:
                img = cv2.imread('images/' + image)
                # Graying
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # save grayed file
                cv2.imwrite('gray/gray_' + image, gray)
                # return file's url
                return HttpResponse(content=STATIC_URL + 'gray_' + image, status=200)


# Return images by list
def index(request):
    # read urls from cache
    urls = cache.get('urls')
    urls = urls.split('\n')
    dimension = request.GET.get('dimension', default=None)

    # Get images by dimension?
    if dimension:
        dimension_url = []
        for url in urls:
            if '/'.join(dimension.split('x')[0:2]) in url:
                dimension_url.append(url)
        # change urls to dimension url
        urls = dimension_url
    # paged by 12
    total_page = math.ceil(len(urls) / 12)
    page = request.GET.get('page', default=1)

    start = (int(page) - 1) * 12
    end = (int(page) - 1) * 12 + 12
    images = urls[start:end]
    json.dumps(images)
    return HttpResponse(
        content=json.dumps({"images": json.dumps(tuple(images)), "total_page": total_page, 'current_page': page,
                            }),
        content_type='application/json', status=200)
