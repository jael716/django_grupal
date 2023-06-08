from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user=User.objects.all()
    clientes=["Gabriel","pedro","juan","diego","pedro"]
    context={"usuario":user,
             "cliente":clientes

    }
    return render (request,'clientes.html',context=context)

# Create your views here.

def landing_page(request):

    return render(request,'index.html')

