from email.utils import decode_rfc2231
from django.shortcuts import render,redirect
from common.models import Customer,Seller
from adbook.models import Order,Author,Productsss
from django.http import JsonResponse

# Create your views here.
def adbook_home(request):
    return render(request,'adbook/home.html')

def adbook_aboutus(request):
    return render(request,'adbook/aboutus.html')


def adbook_author(request):
    # author_data = Author.objects.get(id=request.session['author'])
    msg = ''
    if request.method == 'POST' :
        Author_name = request.POST['a_name']
        Author_image = request.FILES['a_img']
        new_author = Author(author_name = Author_name , image = Author_image )
    
        new_author.save()
        msg = 'Author added succsessfully'

    return render(request,'adbook/author.html',{'msg': msg})


def adbook_bulkorder(request):
    
    return render(request,'adbook/bulkorder.html')

    
def adbook_login(request):
    return render(request,'adbook/login.html')

 
def adbook_shop(request):
    return render(request,'adbook/shop.html')

def adbook_master(request):
    return render(request,'adbook/master.html')

def adbook_addbook(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    msg = ''
    auther=Author.objects.all()
    if request.method == 'POST' :
        product_name = request.POST['p_name']
        product_description = request.POST['p_des']
        product_number = request.POST['p_num']
        author_name =request.POST['a_name']
        language= request.POST['l_name']
        current_stock = request.POST['stock']
        product_image = request.FILES['p_img']
        price = request.POST['price']

        auth=Author.objects.get(id=author_name)
      
        
        new_product = Productsss(product_name = product_name ,
        product_description = product_description , product_number = product_number ,
        language = language,stock = current_stock ,author_id=auth.id,
        image = product_image ,price = price, seller_id=request.session['seller'])
    
        
        new_product.save()
        print(new_product)
        msg = 'Product added succsessfully'
    return render(request,'adbook/addbook.html',{'msg': msg,'data':seller_data,'author':auther})

def adbook_updatestock(request):
    msg = ''
    seller_data = Seller.objects.get(id=request.session['seller'])
    Product_data = Productsss.objects.filter(seller = request.session['seller'] )
    if request.method == 'POST':
        new_stock =request.POST['new_stock']
        product_id = request.POST['productid']
        new_price = request.POST['new_price']
        product = Productsss.objects.get(id=product_id)
        product.stock = product.stock + int(new_stock)
        product.price = new_price
        product.save()
        msg = 'stock Update succsessfully'

    context = {'prod_data':Product_data,
                    'data':seller_data,
                    'msg': msg,
                    }

    return render(request,'adbook/updatestock.html',context)
def adbook_order(request):
    
    product_order = Order.objects.filter(Customer = request.session['customer'])
    return render(request,'adbook/order.html',{'order_list':product_order})
    


def adbook_catlog(request):
    seller_products = Productsss.objects.filter(seller = request.session['seller'])
    seller_data = Seller.objects.get(id=request.session['seller'])
    context ={'products':seller_products,
                'data': seller_data,
                }
    return render(request,'adbook/catlog.html',context)


def get_stock(request):
    id=request.POST['id']
    
    product=Productsss.objects.get(id=id)
    product_name =product.product_name
    current_stock = product.stock
    price =product.price
    product_id =product.id  
    return JsonResponse({'p_name':product_name,'stock':current_stock,'p_id':product_id,'price':price})

def adbook_proddet(request,pid):

  
    product_details = Productsss.objects.get(id = pid)# fetching singledata
    
    return render(request,'adbook/proddet.html',{'product':product_details})

def adbook_delete(request,pid):
    prod_item = Productsss.objects.get(id = pid)
    prod_item.delete()
    return redirect('adbook:catlog')


 
def adbook_viewcust(request):

    cust_details=Customer.objects.all()
    return render(request,'adbook/viewcust.html',{'customer_list':cust_details})

def author_exist(request):
    author = request.POST['author']

    status = Author.objects.filter(author_name = author).exists()

    return JsonResponse({'status':status})

def book_exist(request):
    books = request.POST['bookname'] 

    status = Productsss.objects.filter(product_name = books).exists()

    return JsonResponse({'status':status})
 

   
