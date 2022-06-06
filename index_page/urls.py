from django.urls import path, include
from .views import index_page, about, contact, services

#My urls and their views
urlpatterns = [
    path("", index_page),
    path("about/", about),
    path("contact/", contact),
    path("services/", services),
]