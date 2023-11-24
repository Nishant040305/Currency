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

#proxie of mnnit
proxies = {
  'http': 'http://edcguest:edcguest@172.31.100.27:3128',
  'https': 'http://edcguest:edcguest@172.31.100.27:3128',
}


# location of currency_name file( include (currency 2 letter code and 3 letter currency code)
csv_file_path = staticfiles_storage.path('currency_name.csv')
content = {}
with open(csv_file_path,'r') as f:
    a =(reader(f))
    for i in a:
      content[f"""/static/flag/{i[0]}.png"""]=i[1]
#data of csv file

#duration for reload
duration = 6000
start = time.time()

#loading data of Api (exchange rate and news)
try:
  #for normal
    API_KEY = "45e8907276ac4e1e9a77d3e83a9f19f7"
    url = "https://newsapi.org/v2/everything?q="
    query="Finance"
    newsurl = f'{url}{query}&apiKey={API_KEY}'
    url ="https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url).json()
    news = requests.get(newsurl).json()
    article = news['articles']

except:
    #for proxy servers
    API_KEY = "45e8907276ac4e1e9a77d3e83a9f19f7"
    url = "https://newsapi.org/v2/everything?q="
    query="Finance"
    newsurl = f'{url}{query}&apiKey={API_KEY}'
    news = requests.get(newsurl,proxies=proxies).json()
    article = news['articles']
    url ="https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url,proxies=proxies).json()

rates = response[ "rates"] #for dict to hold exchange rates
cur_ = "USD" # to hold the present currency of exchange rate table

def exchange(rates,cur):#fuction to get exchange rate for different currency
  exrates = {}
  rate_cur = rates[cur]
  for i in rates:
    exrates[i]=round(rates[i]/rate_cur,4)
  return exrates


def index(request):#main function
    global content
    global response
    global start
    global duration
    global rates
    global exrates
    global query
    global cur_

    favpair = favPain.objects.all()
    history = History.objects.all()
    
    try:#condition of reload
        if((time.time()-start)>duration):
            url ="https://api.exchangerate-api.com/v4/latest/USD"
            response = requests.get(url).json()
            start = time.time()
            rates = response['rates'] #reload rates
            exrates=exchange(exrates,rates,cur_)# data for live according to currency
    except:
        pass

    if request.GET.get('fav'):#function to store data in favPain database(favourites)
        tAmount=request.GET.get('bamount')
        fAmount=request.GET.get('oamount')
        field1_data = request.GET.get('fromCode')
        field2_data = request.GET.get('toCode')
      
        if(field1_data!='Search'and field2_data!='Search'):#to check that the value of fromCode and toCode is correct that is selected
    
            data = favPain.objects.create(fromCode=field1_data, toCode=field2_data)#to store the object into database
            data.save()
          
        return render(request,'index.html',{"x":cur_,'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':field1_data,'tcurrencyCode':field2_data,'history':history,'favpair':favpair,'rates':rates,'exrates':exrates})
    
    elif request.GET.get('exchange'):#to check exchange rate change button is pressed or not
        fcurrencyCode=request.GET.get('fromCode')
        fAmount=request.GET.get('oamount')
        tcurrencyCode=request.GET.get('toCode')
        tAmount=request.GET.get('bamount')
        cur=request.GET["currency"]#to get the value of its search value
        exrates = exchange(rates,cur)
        cur_ = cur
        return render(request,'index.html',{"x":cur_,'exrates':exrates,'rates':rates,'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair,'rates':rates})
    
    elif request.GET.get('convert'):#to check if exchange rate button is pressed or not for conversion process
        try:#to save in history
            fcurrencyCode=request.GET['fromCode']
            fAmount=request.GET['oamount']
            tcurrencyCode=request.GET['toCode']
            tAmount=rates[tcurrencyCode]/rates[fcurrencyCode]  * float(fAmount) 
            tAmount=round(tAmount,3)
            data = History.objects.create(fcurrencyCode=fcurrencyCode,fAmount=fAmount,tcurrencyCode=tcurrencyCode,tAmount=tAmount)
            data.save()

        except:#if something went wrong
            tAmount=0.00
            fcurrencyCode=request.GET['fromCode']
            fAmount=0.00
            tcurrencyCode=request.GET['toCode']

        return render(request,'index.html',{"x":cur_,'exrates':exrates,'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair,'rates':rates})
    
    else:#default or starting webpage setting
        exrates=rates #intial exchange rates for currency USD
      
        tAmount='0.00'#tAmount holds value of amount converted in to required currency
      
        fcurrencyCode='Search'#intial value of from currency
      
        fAmount=''#holds amount to be converted (from currency amount)
      
        tcurrencyCode='Search'#holds code of to currency that to be converted
      
        return render(request,'index.html',{"x":cur_,'exrates':exrates,'context':content,'tAmount':tAmount,'fAmount':fAmount,'fcurrencyCode':fcurrencyCode,'tcurrencyCode':tcurrencyCode,'history':history,'favpair':favpair,'rates':rates})


def news(request):#fuction for news data or page
    global query #to hold query for news default is given to be finance
  
    if request.GET.get("but"):#if search button is clicked
       query = request.GET.get("search")#data search bar
      
    try:
        API_KEY = "45e8907276ac4e1e9a77d3e83a9f19f7"#news api
      
        url = "https://newsapi.org/v2/everything?q="
      
        newsurl = f'{url}{query}&apiKey={API_KEY}'

        news = requests.get(newsurl).json()#news response
      
        article = news['articles'] #articles contain source,article,image url,and link


    except:
        #for proxy servers
        API_KEY = "45e8907276ac4e1e9a77d3e83a9f19f7"
        url = "https://newsapi.org/v2/everything?q="
        
        newsurl = f'{url}{query}&apiKey={API_KEY}'
        news = requests.get(newsurl,proxies=proxies).json()
        article = news['articles']
    return render(request,'news.html',{'news':article})
