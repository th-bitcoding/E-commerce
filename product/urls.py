from django.urls import path,include
from product import views
app_name = 'product'
urlpatterns = [

    path('',views.index,name='index'),
    path('productadd',views.ProductCreate.as_view(),name='productadd'),
    path('productlist',views.ProductList.as_view(),name='productlist'),
    path('productupdate/<int:pk>/',views.ProductUpdate.as_view(),name='productupdate'),
    path('productdelete/<int:pk>/',views.ProductDelete.as_view(),name='productdelete'),
    path('customerproduct/',views.CustomerProductList.as_view(),name='customerproduct'),


]