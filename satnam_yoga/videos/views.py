import requests
import json

from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from videos.models import Video

#Video cipher vdocipher


# Create your views here.

def list_menu(request):
    return render(request, 'videos/feed.html')


def video_list(request):

    # for video in video_content:
    #     print("Video: ", type(video))
    #     url = "https://dev.vdocipher.com/api/videos/{video.upload}/otp"
    #     payloadStr = json.dumps({'ttl': 300})
    #     headers = {
    #       'Authorization': "Apisecret bGz8aFy2o0mfQrbbq7ozvFy6LawbhTzkbvGXKvaskFsgySV87Xb5BAUzwu5rPxyN",
    #       'Content-Type': "application/json",
    #       'Accept': "application/json"
    #     }
    #
    #     response = requests.request("POST", url, data=payloadStr, headers=headers)
    #
    #     # print(f"Esta es la respuesta OTP: {response.text["otp"]}")
    #     dict =eval(response.text)

    video_content = Video.objects.all().order_by('created')

    return render(request, 'videos/videos.html', {'video_content': video_content})


def video_id_show(request, video_id):
    video= Video.objects.get(id=video_id)
    print(type(video))
    video_content = Video.objects.all().order_by('created')

    return render(request, 'videos/videos.html', {'video_content': video_content, 'video': video})
