from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import requests
import feedparser
from csv import reader
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import favPain
# import ajax_required

# @ajax_required
csv_file_path = staticfiles_storage.path('currency_name.csv')
content = {}
with open(csv_file_path,'r') as f:
    a =( reader(f))
    for i in a:
        content[i[0]]=i[1]
context={}
context={'context':content}
def index(request):
    global context
    # if request.method == 'POST':
    #     field1_data = request.POST.get('field1')
    #     field2_data = request.POST.get('field2')
    #     # Get more fields as per your requirements

    #     favPain.objects.create(field1=field1_data, field2=field2_data)
    #     favPain.save()
        # Create more fields as 

    return render(request,'index2.html',context)

def fav(request):
    global context
    if request.method == 'POST':
        field1_data = request.POST.get('fromCode')
        field2_data = request.POST.get('toCode')

    data = favPain.objects.create(fromCode=field1_data, toCode=field2_data)
    data.save()
    return render(request,'index2.html',context)
def calculator(request):
    return render(request,'index4.html')
 
def news_feed(request):
    NewsFeed = feedparser.parse("http://www.ecb.europa.eu/rss/usd.html")
    return render(request, 'index3.html', {"feed": NewsFeed})

# def convert_currency(request):
#     amount = request.GET.get('amount')
#     from_currency = request.GET.get('from_currency')
#     to_currency = request.GET.get('to_currency')

#     # Make sure to replace 'your_api_key' with your actual API key
#     url = f"http://api.exchangeratesapi.io/v1/latest?access_key=aa54007b6c5e6136b3eba5cf93f4a9a9{from_currency}"
#     response = requests.get(url)
#     data = response.json()

#     conversion_rate = data['rates'][to_currency]
#     converted_amount = float(amount) * conversion_rate

#     return JsonResponse({'result': converted_amount})
