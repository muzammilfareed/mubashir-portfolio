from django.shortcuts import render
from .models import mubashir_studio

# Create your views here.


def index(request):
    # if request.method == "POST":
    #     obj = mubashir_studio()
    #     obj.name = request.POST.get('name')
    #     obj.email = request.POST.get('email')
    #     obj.phone = request.POST.get('phone')
    #     obj.address = request.POST.get('address')
    #     obj.subject = request.POST.get('subject')
    #     obj.message = request.POST.get('message')
    #     obj.save()
    #     return render(request, 'index.html')
    return render(request, 'index.html')