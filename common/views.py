from django.shortcuts import render,redirect
from . models import Customer,Seller
from django.conf import settings
from django.http import JsonResponse

import random
from django.core.mail import send_mail


# Create your views here.
    
def common_custlogin(request):
    print('cust home')
    custmsg = ''
    if request.method == 'POST':
        cust_email = request.POST['c_email'] 
        cust_password = request.POST['password'] 

        try :
            print('try block')
            customer = Customer.objects.get(email_address = cust_email, cust_password = cust_password )
            
            request.session['customer'] = customer.id
            return redirect('customer:userhome')
        except:
            custmsg = 'username or password incorrect'  
            
    return render(request,'common/custlogin.html',{'custmsg':custmsg})
    
def common_commonhome(request):
    return render(request,'common/commonhome.html')

def common_custreg(request):
    msg = ''
    if request.method == 'POST':
        c_name = request.POST['c_name']
        c_address = request.POST['c_address']
        c_number = request.POST['c_phone']
        c_gender = request.POST['c_gender']
        c_email = request.POST['c_email']
        c_pass = request.POST['c_password']

        new_customer = Customer(customer_name = c_name ,
      address =c_address , phone_number = c_number ,
         gender = c_gender,   email_address = c_email ,  cust_password = c_pass)
        new_customer.save()
        msg ='Customer Registerion Successfully'
    return render(request,'common/custreg.html',{'msg': msg})

def common_adminlog(request):
    msg = ''
    if request.method == 'POST':
        sell_username = request.POST['s_username'] 
        sell_password = request.POST['s_password'] 

        try :
            seller = Seller.objects.get(username = sell_username, password= sell_password )
            request.session['seller'] = seller.id
            return redirect('adbook:home')
        except :            
             msg = 'username or password incorrect'

    return render(request,'common/adminlog.html',{'msg':msg})
def common_adminreg(request):
    
    return render(request,'common/adminreg.html')
def common_master(request):
    
    return render(request,'common/master.html')
