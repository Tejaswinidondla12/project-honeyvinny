from django.shortcuts import render

# Create your views here.
def app2first(request):
    return render(request,'app2first.html')

def app2second(request):
    return render(request,'app2second.html')
