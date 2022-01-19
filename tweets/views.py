from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import Http404
from django.http import JsonResponse

from .models import Tweet

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
    

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    returns json data
    """
   
    data = {
        "id": tweet_id,
    }
    status = 200
    try:

        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "not found"
        status = 404

    return JsonResponse(data, status=status)