from django.shortcuts import render,redirect
from customer.models import Orders
from customer.models import Order_detail
from common.models import Customer,Seller
from customer.models import Carts,Wishlist
from adbook.models import Order,Productsss,Author
from django.http import JsonResponse
from django.db.models import F
import razorpay
from django.conf import settings


RAZORPAY_KEY_ID ='rzp_test_kEK1aSRc2RrRUA'
RAZORPAY_KEY_SECRET = '8aOkgb8BWBesmsKnCjugCao3'

# Create your views here.

def customer_userhome(request):
  
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_list = Productsss.objects.all()

  

    return render(request,'customer/userhome.html',{'data':cust_data,'products': product_list})

def customer_productdetails(request,pid):
    msg=''
    product_details = Productsss.objects.get(id = pid)# fetching singledata
    if request.method == 'POST':
        product_id = request.POST['pid']
        quantity = request.POST['qty']
        item_exist =Carts.objects.filter(Product_id = product_id , Customer_id = request.session['customer']).exists()

        if not item_exist :

            cart_item = Carts(Product_id = product_id , Customer_id = request.session['customer'],quantity = quantity)
            cart_item . save()
            return redirect('customer:cart') 

        else:
            msg='item already exist'

    iteminwish=Wishlist.objects.filter(Product_id=pid,Customer_id=request.session['customer']).exists()   
    return render(request,'customer/productdetails.html',{'product':product_details,'msg':msg,'wish':iteminwish})

def customer_author(request):
    cust_data =  Customer.objects.get(id = request.session['customer'])

    author_list = Author.objects.all()
    return render(request,'customer/author.html',{'details':author_list,'data':cust_data})


def customer_authorbook(request,pid):
    cust_data =  Customer.objects.get(id = request.session['customer'])

    author_books = Productsss.objects.filter(author = pid)
    return render(request,'customer/authorbook.html',{'details':author_books,'data':cust_data})




def customer_shop(request):
    return render(request,'customer/shop.html')


def customer_cart(request):


    cust_data =  Customer.objects.get(id = request.session['customer'])

    product_cart = Carts.objects.filter(Customer = request.session['customer']).annotate(total = F('Product__price')*F('quantity'))
    grand_total = 0
    for product in product_cart:
        grand_total = product.total + grand_total
    request.session['grand_total'] = grand_total

    context = {
        'cart_data':product_cart,
        'grand_total':grand_total,
        'cart_list':product_cart,
        'data':cust_data
    }


    return render(request,'customer/cart.html',context)
 

def customer_changepass(request):
    cust_data =  Customer.objects.get(id = request.session['customer'])

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

    return render(request,'customer/changepass.html',{'msg':msg,'data':cust_data})

    
def customer_profile(request):
    cust_data = Customer.objects.get(id = request.session['customer'])
    
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
   
 
    return render(request,'customer/profile.html',{'msg': msg,'cust':customer_data,'data':cust_data})


def logout(request):
    del request.session['customer'] 
    request.session.flush() 
    return redirect('#')

def remove_item(request,pid):
    # cust_data =  Customer.objects.get(id = request.session['customer'])

    cart_item = Carts.objects.filter(Product = pid, Customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')

def customer_about(request):
    return render(request,'customer/about.html')

def customer_checkout(request):

    # user_id=request.session['customer']

    # od=Orders(customer_id=user_id,amount=request.session['grand_total'],status='pending')
    # od.save()
    # request.session['oid']= od.id
    # products=Carts.objects.filter(customer_id=user_id) 


    # for pro in products:

    #     print(pro.product_id)

    #     order=Order_detail(customer_id=user_id,
    #                 productid_id=pro.product_id,
    #                 price=pro.product.p_price,
    #                 quantity=pro.qty,
    #                 status="order_pending",
    #                 payment_type="Razorpay",
    #                 order_id=od.id        
    #                 )
    #     order.save()
    # products.delete()

    # name=Customer.objects.get(id=request.session['customer']).first_name
    # amount=request.session['grand_total']
    return render(request,'customer/checkout.html')
def customer_myorder(request):
    user_id=request.session['customer']
    Orders.objects.filter(customer_id=user_id,status='pending').update(status='paid')
    Order_detail.objects.filter(customer_id=user_id,status='pending').update(status='paid')
    orders=Order_detail.objects.filter(customer_id=user_id)
    return render(request,'customer/myorder.html',{'orders':orders})
   
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_order = Order.objects.filter(Customer = request.session['customer'])

    return render(request,'customer/myorder.html',{'order_list':product_order,'data':cust_data})

def customer_userhome(request):
    cust_data =  Customer.objects.get(id = request.session['customer'])
    product_list = Productsss.objects.all()

    print(product_list)

    return render(request,'customer/userhome.html',{'data':cust_data,'products': product_list})



def updatepayment(request):
    user_id=request.session['customer']
    Orders.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending').update(status="paid")
    pid=Orders.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending')
    customer_id=request.session['customer']
    products=Carts.objects.filter(customer_id=user_id) 

    for pro in products:

        print(pro.Product_id)

        order=Order_detail(customer_id=user_id,
                    productid_id=pro.Product_id,
                    price='200',
                    quantity=pro.qty,
                    status="paid",
                    payment_type="Razorpay",
                    order_id= pid.id
        )
        order.save()
        products.delete()

    Order_detail.objects.filter(customer_id=user_id, status='order_pending',order_id=request.session['oid']).update(status='paid')
    return JsonResponse({'resp':'sucsses'})


def customer_wishlist(request):
    cust_data =  Customer.objects.get(id = request.session['customer'])

    wishlist = Wishlist.objects.filter(Customer_id = request.session['customer'])
    context ={
                 'wish_list':wishlist,
                 'data':cust_data
    }
    
    return render(request,'customer/wishlist.html',context)

def addtowishlist(request,pid):
    msg =""
    product_details = Productsss.objects.get(id=pid)
    product_exist = Wishlist.objects.filter(Product = pid,Customer = request.session['customer']).exists()
    if not product_exist:
        wish = Wishlist.objects.create(Customer_id =request.session['customer'],Product_id=pid)
        return redirect('customer:productdetails',pid)
    else:
        msg ='Item already in wishlist'
        return redirect('customer:productdetails',pid) 
        

    context ={
        'pdetail':product_details,
        'msg':msg
    }
    return render(request,'customer/productdetails.html',context)

def removefromwishlist(request,pid):
    try:
        name = request.GET['page']
    except:
        name=''    

    if name=='product':
        wish_item = Wishlist.objects.get(Product_id = pid, Customer_id = request.session['customer'])
        wish_item.delete()
        return redirect('customer:productdetails',pid)
    else:
        wish_item = Wishlist.objects.get(id = pid, Customer_id = request.session['customer'])
        wish_item.delete()
        return redirect('customer:wishlist')


def customer_shipping(request):

    return render(request,'customer/shipping.html')


def razorpay_payment(request):
    # customer= request.session['customer']
    # amount = request.session['grand_total']
    # order_recipt="order_reciptid_11"
    # notes={'shipping address':'bomalahalli,bangolre'}
    # products= Orders.objects.filter(customer_id=request.session['customer'],status='pending')
    
    # client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
    # payment = client.order.create(
    #     {"amount":float(amount)*100,"currency":"INR","payment_capture":1,'notes':notes}
    # )
    # return JsonResponse(payment)

    customer= request.session['customer']
    amount = request.session['grand_total']
    order_recipt="order_reciptid_11"
    notes={'shipping address':'bomalahalli,bangolre'}
    products= Orders.objects.filter(customer_id=request.session['customer'],status='pending')
    
    client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
    payment = client.order.create(
        {"amount":float(amount)*100,"currency":"INR","payment_capture":1,'notes':notes}
    )
    return JsonResponse(payment)

    
