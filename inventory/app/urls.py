from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('app/', views.app, name='app'),
    path('app1/', views.app1, name='app1'),     
    path('app/item_details/<int:id>', views.item_details, name='item_details'),
    path('app/add_item/', views.add_item, name='add_item'),
    path('app/update_room/<int:id>', views.update_room, name='update_room'),
    path('app1/room_details/<int:id>', views.room_details, name='room_details'),
    ]