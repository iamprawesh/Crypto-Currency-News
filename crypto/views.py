from django.shortcuts import render

# Create your views here.

def info(request):
    x = 'Lorem ipsum, in graphical and textual context, refers to filler text that is placed in a document or visual presentation. Lorem ipsum is derived from the Latin  roughly translated as pain itself.' 
    return render(request,'info.html',{'x':x})

def home(request):
    import requests
    import json 

    # grab crypto news

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,ETC,LTC,BCH,EOS,BNB,OKB,TRX,&tsyms=USD")
    price = json.loads(price_request.content)


    # grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json 
    # grab crypto news
        quote = request.POST['quote']
        quote = quote.upper()
        # try:
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote +"&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        # status = "Successfully Searched" 
        if 'Response' in crypto:        
            invalid_search = crypto['Message']
            errstatus = "Invalid Crypto Symbol"
            return render(request,'prices.html',{'invalid_search':invalid_search,'errstatus':errstatus})
        # else:
        else:
            status = "Successfully Searched"
            return render(request,'prices.html',{'quote':quote,'crypto':crypto,'status':status})           
    else:
        notfound = "Enter the crypto currency symbol into the above form"
        return render(request,'prices.html',{'notfound':notfound})
