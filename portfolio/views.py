from django.shortcuts import render, HttpResponse
#from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('test_portfolio_index.html')
    return HttpResponse(template.render())
    # return HttpResponse("Home")


def portfolio(request):
    template = loader.get_template('portfolio_page.html')
    return HttpResponse(template.render())
    # return render(request,'portfolio_page.html')