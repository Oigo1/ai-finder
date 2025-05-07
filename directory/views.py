from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def index(request):
    return render(request, 'directory/index.html')

def get_models(request):
    models_path = os.path.join(os.path.dirname(__file__), 'models.json')
    with open(models_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
