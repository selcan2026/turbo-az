from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('car/<int:id>/', views.car_detail, name='car_detail'),

    path('add-car/', views.add_car, name='add_car'),

    path('my-cars/', views.my_cars, name='my_cars'),

    path('edit-car/<int:id>/', views.edit_car, name='edit_car'),

    path('delete-car/<int:id>/', views.delete_car, name='delete_car'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

]
