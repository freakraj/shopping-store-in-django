from django.shortcuts import render
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        mobiles = Product.objects.filter(category = 'M')
        return render(request, 'app/home.html',{'topwears':topwears, 'bottomwears':bottomwears,
        'mobiles':mobiles})

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def profile(request):
 return render(request, 'app/profile.html')

def mobile(request,data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'MI' or data == 'Sumsang':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Oppo' or data == 'Vivo':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Nokia' or data == 'Apple':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    # elif data == 'Real Me':
    #     mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

class CustomerRegistrationView(View):
    def get(self,request): # to showing blank form get
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request, "Congratulation !! Registration Succesfull.")
            form.save()
            # print(form)
        return render(request, 'app/customerregistration.html',{'form':form})
