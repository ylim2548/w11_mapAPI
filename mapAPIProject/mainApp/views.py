from django.shortcuts import render
from .models import Cafe

def main(request):
    cafes = Cafe.objects.all()
    return render(request, 'main.html', {'cafes':cafes})