from django.shortcuts import render

# Create your views here.
def app1first(request):
    return render(request,'app1first.html')

def app1second(request):
    return render(request,'app1second.html')
