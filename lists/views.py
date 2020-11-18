from django.http.response import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse('<html><head><title>To-Do lists</title></head></html>')
