from django.urls import path
from . import views
app_name= 'adbook'
urlpatterns = [
    path('home',views.adbook_home,name='home'),
    path('aboutus',views.adbook_aboutus,name='aboutus'),
    path('addbook',views.adbook_addbook,name='addbook'),
    path('author',views.adbook_author,name='author'),
    path('proddet/<int:pid>',views.adbook_proddet,name='proddet'),
    path('shop',views.adbook_shop,name='shop'),
    path('master',views.adbook_master,name='master'),
    path('updatestock',views.adbook_updatestock,name='updatestock'),
    path('order',views.adbook_order,name='order'),
    path('catlog',views.adbook_catlog,name='catlog'),
    path('delete/<int:pid>',views.adbook_delete,name='delete'),
    path('viewcust',views.adbook_viewcust,name='viewcust'),
    path('get_stock',views.get_stock,name='get_stock'),
    

    # path('get_author',views.get_author,name='get_author'),



]
