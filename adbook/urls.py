from django.urls import path
from . import views
urlpatterns = [
    path('home',views.adbook_home,name='home'),
    path('aboutus',views.adbook_aboutus,name='aboutus'),
    path('author',views.adbook_author,name='author'),
    path('book',views.adbook_book,name='book'),
    path('explore',views.adbook_explore,name='explore'),
    path('login',views.adbook_login,name='login'),
    path('register',views.adbook_register,name='register')
    
    
]
