from django.shortcuts import render

# Create your views here.
def mdb2(request):
    return render(request,'mdb2.html')

def child(request):
    return render(request,'child.html')