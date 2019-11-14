from django.shortcuts import render, get_object_or_404, redirect

import csv, io
from .models import Gift
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


# Create your views here.

def index(request):
    gift_list = Gift.objects.order_by('-name').filter(available=True)
    context = {
        'gift_list': gift_list,
    }
    return render(request, 'entries/index.html', context)

def indexAll(request):
    gift_list = Gift.objects.order_by('-name')
    context = {
        'gift_list': gift_list,
    }
    return render(request, 'entries/index.html', context)

def detail(request, gift_id):
    if request.method == "POST":
        gift = get_object_or_404(Gift, pk=gift_id)
        if request.POST.get("Yes"):
            gift.available = False
            gift.save()
        return redirect('entries:index')
    else:
        gift = get_object_or_404(Gift, pk=gift_id)
        data = serializers.serialize( "python", Gift.objects.all() )
        #See if the user clicked a button

    return render(request, 'entries/detail.html', {'gift': gift, 'data': data})

