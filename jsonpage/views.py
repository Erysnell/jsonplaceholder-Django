import requests
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    data = response.json()
    return render(request, "page.html", { 'data': data })