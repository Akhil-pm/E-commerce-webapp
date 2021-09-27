from django.urls import path
from . import views


app_name='shop'



urlpatterns = [
      path('',views.allProdcat,name='allProdCat'),
      path('<slug:c_slug>/',views.allProdcat,name='products_by_category'),
]