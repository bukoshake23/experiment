from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  
    url(r'^product/(?P<product_id>[0-9]+)/$', views.TypesView, name='types'),   
    url(r'^cart/$', views.CartView, name='cart'),         
    url(r'^checkout/$', views.CheckOutView, name='checkout'),    
]
