from django.shortcuts import render
import json
import requests

def home(request):
    price_requests=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,TRX,DASH,XRP&tsyms=USD")
    price=json.loads(price_requests.content)


    api_requests=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_requests.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):
    if request.method=='POST':
        quote=request.POST['quote']
        quote=quote.upper()
        crypto_requests=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        crypto=json.loads(crypto_requests.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        notfound="Enter the Crypto Currency symbol into the form above...."
        return render(request,'prices.html',{'notfound':notfound})
