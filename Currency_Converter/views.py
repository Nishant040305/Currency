from django.shortcuts import render

# Create your views here.
import time
import threading
from django.http import JsonResponse
import requests
from csv import reader
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import favPain
from .models import History
proxies = {
  'http': 'http://edcguest:edcguest@172.31.100.27:3128',
  'https': 'http://edcguest:edcguest@172.31.100.27:3128',
}
csv_file_path = staticfiles_storage.path('currency_name.csv')
content = {}
with open(csv_file_path,'r') as f:
    a =( reader(f))
    for i in a:
        content[f"""/static/flag/{i[0]}.png"""]=i[1]
duration = 6000
start = time.time()
try:
    url ="https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url).json()
except:
    #for proxy servers
    url ="https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url,proxies=proxies).json()
rates = response[ "rates"]
def index(request):
    global content
    global response
    global start
    global duration
    global rates
    
    favpair = favPain.objects.all()
    history = History.objects.all()
    try:
        if((time.time()-start)>duration):
            try:
                url ="https://api.exchangerate-api.com/v4/latest/USD"
                response = requests.get(url).json()
            except:
                #for proxy servers
                url ="https://api.exchangerate-api.com/v4/latest/USD"
                response = requests.get(url,proxies=proxies).json()
            start = time.time()
            rates = response['rates']
    except:
        pass
    
    if request.GET.get('fav'):
        tAmount=request.GET.get('bamount')
        fAmount=request.GET.get('oamount')
        field1_data = request.GET.get('fromCode')
        field2_data = request.GET.get('toCode')
        if(field1_data!='Search'and field2_data!='Search'):
    
            data = favPain.objects.create(fromCode=field1_data, toCode=field2_data)
            data.save()
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':field1_data,'tcurrencyCode':field2_data,'history':history,'favpair':favpair,'rates':rates})

    elif request.GET.get('convert'):
        try:
            fcurrencyCode=request.GET['fromCode']
            fAmount=request.GET['oamount']
            tcurrencyCode=request.GET['toCode']
            tAmount=rates[tcurrencyCode]/rates[fcurrencyCode]  * float(fAmount) 
            tAmount=round(tAmount,3)
            data = History.objects.create(fcurrencyCode=fcurrencyCode,fAmount=fAmount,tcurrencyCode=tcurrencyCode,tAmount=tAmount)
            data.save()
            
        except:
            tAmount=0.00
            fcurrencyCode=request.GET['fromCode']
            fAmount=0.00
            tcurrencyCode=request.GET['toCode']

        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair,'rates':rates})

    elif request.GET.get('calcwindow'):
        

        tAmount=request.GET.get('bamount')
        fAmount=request.GET.get('oamount')
        field1_data = request.GET.get('fromCode')
        field2_data = request.GET.get('toCode')
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':field1_data,'tcurrencyCode':field2_data,'favpair':favpair,'rates':rates,'history':history})
    else:
        tAmount='0.00'
        fcurrencyCode='Search'
        fAmount=''
        tcurrencyCode='Search'
        return render(request,'index.html',{'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair,'rates':rates})
