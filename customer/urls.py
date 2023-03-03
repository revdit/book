from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
     
     path('custhome',views.customer_custhome,name='custhome'),
     path('bulkorder',views.customer_bulkorder,name='bulkorder'),
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
     path('test',views.customer_test,name='test'),
     path('userhome',views.customer_userhome,name='userhome'),
     path('order_payment',views.order_payment,name='order_payment'),
     path('wishlist',views.customer_wishlist,name='wishlist'),
     path('addwish/<int:pid>',views.addtowishlist,name='addtowishlist'),
     path('remove_wishlist/<int:pid>',views.removefromwishlist,name='removefromwishlist'),












     



     







     
    
]
