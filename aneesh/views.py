from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={}
    return render(request, 'aneesh/index.html',context)


