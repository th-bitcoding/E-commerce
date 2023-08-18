from django.urls import path,include
from Client import views
app_name = 'client'
urlpatterns = [

    path('',views.index,name='index'),
    path('add/',views.ClientCreate.as_view(),name='add'),
    path('category/',views.CategoryCreate.as_view(),name='category'),
    path('categorylist/',views.CategoryView.as_view(),name='categorylist'),

]