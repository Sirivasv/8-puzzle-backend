from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse




# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse({'resultPhrase':'newPhrase', 'status_code':200})