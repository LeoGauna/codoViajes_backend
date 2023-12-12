from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def pack_disney(request):
    return render(request, 'core/pack_disney.html')

def pack_europa(request):
    return render(request, 'core/pack_europa.html')

def about_us(request):
    return render(request, 'core/about_us.html')