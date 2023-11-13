from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import requests
import feedparser
from csv import reader
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import favPain
from .models import History


csv_file_path = staticfiles_storage.path('currency_name.csv')
content = {}
with open(csv_file_path,'r') as f:
    a =( reader(f))
    for i in a:
        content[i[0]]=i[1]
def index(request):
    global content
    favpair = favPain.objects.all()
    history = History.objects.all()

    if request.GET.get('fav'):
        tAmount=request.GET.get('bamount')
        fAmount=request.GET.get('oamount')
        field1_data = request.GET.get('fromCode')
        field2_data = request.GET.get('toCode')
        if(field1_data!='Search'and field2_data!='Search'):
    
            data = favPain.objects.create(fromCode=field1_data, toCode=field2_data)
            data.save()
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':field1_data,'tcurrencyCode':field2_data,'history':history,'favpair':favpair})

    elif request.GET.get('convert'):
        try:
            fcurrencyCode=str(request.GET['fromCode'])
            fAmount=request.GET['oamount']
            tcurrencyCode=request.GET['toCode']
            url ="https://api.exchangerate-api.com/v4/latest/USD"
            response = requests.get(url).json()
            tAmount=response['rates'][tcurrencyCode]/response['rates'][fcurrencyCode]  * float(fAmount) 
            tAmount=round(tAmount,3)
            data = History.objects.create(fcurrencyCode=fcurrencyCode,fAmount=fAmount,tcurrencyCode=tcurrencyCode,tAmount=tAmount)
            data.save()
        except:
            tAmount='0.00'
            fcurrencyCode='Search'
            fAmount='0.00'
            tcurrencyCode='Search'
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair})

    elif request.GET.get('calcwindow'):
        

        tAmount=request.GET.get('bamount')
        fAmount=request.GET.get('oamount')
        field1_data = request.GET.get('fromCode')
        field2_data = request.GET.get('toCode')
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':field1_data,'tcurrencyCode':field2_data,'favpair':favpair,'history':history})
    else:
        tAmount='0.00'
        fcurrencyCode='Search'
        fAmount='0.00'
        tcurrencyCode='Search'
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair})

       
    