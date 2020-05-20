from django.shortcuts import render
from django.views.decorators.http import require_GET
from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
import threading
import requests
from json import loads
import os
import smtplib



@require_GET
def HomeView(request):
    return render(request, 'scraper/home.html')


@api_view(['POST'])
@permission_classes([AllowAny])
def ScrapeView(request):
    try:
        urls = request.POST.get('urls')
       
        if None not in (urls):
            url = threading.Thread(target=process_request, args=(urls))
            url.start()
            return Response(data={'success': True, 'message': 'Website is loading'})
        else:
            raise Exception('Invalid URLs!')

    except Exception as e:
        return Response(data={'success': False, 'message': str(e)}, status=HTTP_400_BAD_REQUEST)


def ProcessRequest(url):
    website_file = downloadFile(url)
   

def DownloadFile(urls):
    url = loads(url)

    if len(url) > 3:
        url = url[:3]

    file_names = []
    for link in url:
        print(link)
        request = requests.get(link)
        file_name = f'{str(uuid4())}.html'
        file_names.append(file_name)
        with open(file_name, 'wb') as f:
            f.write(request.content)

    return file_names


def GenerateFile(file_names, url):
    file_name = f'url.txt'
    f = open(file_name, "w")
     
    for file in file_names:
        f.write(file)
            
    return f


