from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('app/', views.app, name='all_items'), # all_items view is now app view
    path('app1/', views.app1, name='all_rooms'), # all_rooms view is now app1 view
    path('app/item_details/<int:id>', views.item_details, name='item_details'),
    path('app/active_items/item_details/<int:id>', views.item_details, name='item_details'),
    path('app/passive_items/item_details/<int:id>', views.item_details, name='item_details'),    
    path('app1/item_details/<int:id>', views.item_details, name='item_details'),
    path('app/add_item/', views.add_item, name='add_item'),
    path('app1/add_room/', views.add_room, name='add_room'),
    path('app/item_details/update_item/<int:id>', views.update_item, name='update_item'),
    path('app1/room_details/update_room/<int:room_id>', views.update_room, name='update_room'),
    path('app1/room_details/<int:id>', views.room_details, name='room_details'),
    path('app1/item_details/update_item/<int:id>', views.update_item, name='update_item'),
    path("app/item_details/<int:id>/warehouse/",views.move_to_warehouse, name="move_to_warehouse"),
    path("app/item_details/<int:id>/restore/", views.restore_item, name="restore_item"),
    path("active_items/", views.active_items, name="active_items"),
    path("passive_items/", views.passive_items, name="passive_items"),
    path("app/item/<int:id>/delete/", views.delete_item, name="delete_item",),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"), name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout",),
    ]