# -*- coding: utf-8 -*- 

from django.utils import timezone

from django.shortcuts import render
from .models import Feedback
import json
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def feedbackRecieve(request):
    print 'feedback'
    if request.method == 'POST':
        device_post = request.POST.get('device')
        key_post = request.POST.get('key')
        content_post = request.POST.get('content')
        if device_post == 'iOS':
            if key_post == 'KqePnWoGfHhbLCU4yoPEXi5qXWQk69IE':
                # ok
                print 'ok'
                f = Feedback(content=content_post, date=timezone.now())
                f.save()
                jsonData = {
                    'code': 0
                }
                return HttpResponse(json.dumps(jsonData, ensure_ascii=False), content_type='application/json')
            else:
                return None
        else:
            return None
    else:
        return None
