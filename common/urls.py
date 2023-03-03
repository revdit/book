from django.urls import path
from . import views
app_name= 'common'
urlpatterns = [

    path('custlogin',views.common_custlogin,name='custlogin'),
    path('commonhome',views.common_commonhome,name='commonhome'),
    path('custreg',views.common_custreg,name='custreg'),
    path('adminlog',views.common_adminlog,name='adminlog'),
    path('adminreg',views.common_adminreg,name='adminreg'),
    path('master',views.common_master,name='master'),
    






]