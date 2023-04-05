from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
     
     
 
     path('shop',views.customer_shop,name='shop'),
     path('cart',views.customer_cart,name='cart'),
     path('changepass',views.customer_changepass,name='changepass'),
     path('logout',views.logout,name='logout'),
     path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),
     path('about',views.customer_about,name='about'),
     path('productdetails/<int:pid>',views.customer_productdetails,name='productdetails'),
     path('checkout',views.customer_checkout,name='checkout'),
     path('myorder',views.customer_myorder,name='myorder'),
     path('author',views.customer_author,name='author'),
     path('authorbook/<int:pid>',views.customer_authorbook,name='authorbook'),
     path('Profile',views.customer_profile,name='profile'),
     path('userhome',views.customer_userhome,name='userhome'),
     path('wishlist',views.customer_wishlist,name='wishlist'),
     path('addwish/<int:pid>',views.addtowishlist,name='addtowishlist'),
     path('removefromwishlist/<int:pid>',views.removefromwishlist,name='removefromwishlist'),
     path('shipping',views.customer_shipping,name='shipping'),
     path('razorpay_payment',views.razorpay_payment,name='razorpay_payment'),
     path("updatepayment",views.updatepayment, name="updatepayment"),
     
]
