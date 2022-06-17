from django.urls import path, include
from .views import index_page, about, contact, services, rooms, manage_room

#My urls and their views
app_name = "index"

urlpatterns = [
    path("", index_page, name="homeview"),
    path("about/", about, name="aboutview"),
    path("contact/", contact, name="contactview"),
    path("service/", services, name='serviceview'),
    #path("rooms/", rooms, name='roomsview'),
    path("manage_room/", manage_room, name='manageview'),
    
]