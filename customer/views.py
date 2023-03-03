from django.shortcuts import render,redirect
from common.models import Customer,Seller
from customer.models import Carts,Wishlist
from adbook.models import Order,Productsss,Author
from django.http import JsonResponse


# Create your views here.


# def customer_custhome(request):
#     print('cust home')
#     cust_data =  Customer.objects.get(id = request.session['customer'])
#     product_list = Productsss.objects.all()

#     print(product_list)

#     return render(request,'customer/custhome.html',{'data':cust_data,'products': product_list})


def customer_userhome(request):
  
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_list = Productsss.objects.all()

  

    return render(request,'customer/userhome.html',{'data':cust_data,'products': product_list})

def customer_productdetails(request,pid):
    msg=''
    product_details = Productsss.objects.get(id = pid)# fetching singledata
    if request.method == 'POST':
        product_id = request.POST['pid']
        item_exist =Carts.objects.filter(Product_id = product_id , Customer_id = request.session['customer']).exists()

        if not item_exist :

            cart_item = Carts(Product_id = product_id , Customer_id = request.session['customer'])
            cart_item . save()
            return redirect('customer:cart') 

        else:
            msg='item already exist'
    return render(request,'customer/productdetails.html',{'product':product_details,'msg':msg})

def customer_author(request):
    author_list = Author.objects.all()
    return render(request,'customer/author.html',{'details':author_list})


def customer_authorbook(request,pid):
    author_books = Productsss.objects.filter(author = pid)
    return render(request,'customer/authorbook.html',{'details':author_books})

def customer_bulkorder(request):
    return render(request,'customer/bulkorder.html')


def customer_shop(request):
    return render(request,'customer/shop.html')


def customer_cart(request):
    product_cart = Carts.objects.filter(Customer = request.session['customer'])
    return render(request,'customer/cart.html',{'cart_list':product_cart})
 

def customer_changepass(request):
    msg=''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if customer.cust_password == current_pass:

            if new_pass == confirm_pass:
                 customer.cust_password = new_pass
                 customer.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'

    return render(request,'customer/changepass.html',{'msg':msg})
    
def customer_profile(request):
    customer_data = Customer.objects.get(id = request.session['customer'])
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        c_name = request.POST['c_name']
        c_address = request.POST['c_address']
        c_number = request.POST['c_phone']
        c_gender = request.POST['c_gender']
        c_email = request.POST['c_email']
        c_pass = request.POST['c_password']


        customer.customer_name = c_name 
        customer.address =c_address 
        customer.phone_number = c_number 
        customer.gender = c_gender
        customer.email_address = c_email 
        customer.cust_password = c_pass
        customer.save()
        msg ='Update Profile Successfully'
   
 
    return render(request,'customer/profile.html',{'msg': msg,'cust':customer_data})


def logout(request):
    del request.session['customer'] 
    request.session.flush() 
    return redirect('#')

def remove_item(request,pid):
    cart_item = Carts.objects.get(Product = pid, Customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')



def customer_about(request):
    return render(request,'customer/about.html')





def customer_checkout(request):

    return render(request,'customer/checkout.html')
def customer_myorder(request):
   
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_order = Order.objects.filter(Customer = request.session['customer'])
    return render(request,'customer/myorder.html',{'order_list':product_order,'data':cust_data})
  
def customer_test(request):
    return render(request,'customer/test.html')
def customer_userhome(request):
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_list = Productsss.objects.all()

    print(product_list)

    return render(request,'customer/userhome.html',{'data':cust_data,'products': product_list})


def order_payment(request):
    if request.method == "POST":
        c_id = request.session['c_id']
        amount = request.POST['total']
        order_recipt="order_reciptid_11"
        notes={'shipping address':'bomalahalli,bangolre'}

        products= Order.objects.filter(customer_id=request.session['c_id'],status='pending')

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        payment = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1",'notes':notes}
        )

        
        print(payment)
        return JsonResponse(payment)


def customer_wishlist(request):
    wishlist = Wishlist.objects.filter(cust = request.session['customer'])
    context ={
                 'wish_list':wishlist,
    }
    
    return render(request,'customer/wishlist.html',context)

def addtowishlist(request,pid):
    msg =""
    product_details = Productsss.objects.get(id=pid)
    product_exist = Wishlist.objects.filter(Product = pid,Customer = request.session['customer']).exists()
    if not product_exist:
        wish = Wishlist.objects.filter(Customer_id =request.sesssion['customer'],Product_id=pid)
        wish.save()
    else:
        msg ='Item already in wishlist'
    context ={
        'pdetail':product_details,
        'msg':msg
    }
    return render(request,'customer/productdetails.html',context)

def removefromwishlist(request,pid):
    wish_item = Wishlist.objects.get(Product = pid, Customer = request.session['customer'])
    wish_item.delete()
    return redirect('customer:wishlist')



