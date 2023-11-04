
from django.http import JsonResponse
import requests
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


#copied from chatgpt
def convert_currency(request):
    amount = request.GET.get('amount')
    from_currency = request.GET.get('from_currency')
    to_currency = request.GET.get('to_currency')

    # Make sure to replace 'your_api_key' with your actual API key
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key=aa54007b6c5e6136b3eba5cf93f4a9a9{from_currency}"
    response = requests.get(url)
    data = response.json()

    conversion_rate = data['rates'][to_currency]
    converted_amount = float(amount) * conversion_rate

    return JsonResponse({'result': converted_amount})
