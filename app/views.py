from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def create_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TDFO=TopicForm(request.POST)
        if TDFO.is_valid():
            tn=TDFO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('create_topic is creadted')
        else:
            return HttpResponse('data is invalid')
    return render(request,'create_topic.html',d)

def create_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            tn=WDFO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WDFO.cleaned_data['name']
            u=WDFO.cleaned_data['url']
            e=WDFO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('create_webpage is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'create_webpage.html',d)

def create_accessrecord(request):
    EARFO=AccessRecordForm()
    d={'EARFO':EARFO}
    if request.method=='POST':
        ARDFO=AccessRecordForm(request.POST)
        if ARDFO.is_valid():
            n=ARDFO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            d=ARDFO.cleaned_data['date']
            a=ARDFO.cleaned_data['author']
            ARO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            ARO.save()
            return HttpResponse('create_accessrecord is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'create_accessrecord.html',d)
