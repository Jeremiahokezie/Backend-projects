from django.urls import path, include
from .views import executive1, executive2, executive3, executive4, deluxe1, deluxe2, deluxe3, deluxe4, standard1, standard2, standard3, standard4,active, record

app_name = "guests"

#my urls

urlpatterns= [
    path("", record, name="recordsview"),
    path("deluxe1/", deluxe1, name="deluxe1view"),
    path("deluxe2/", deluxe2, name="deluxe2view"),
    path("deluxe3/", deluxe3, name="deluxe3view"),
    path("deluxe4/", deluxe4, name="deluxe4view"),
    path("standard1/", standard1, name="standard1view"),
    path("standard2/", standard2, name="standard2view"),
    path("standard3/", standard3, name="standard3view"),
    path("standard4/", standard4, name="standard4view"),
    path("execute1/", executive1, name="executive1view"),
    path("execute2/", executive2, name="executive2view"),
    path("execute3/", executive3, name="executive3view"),
    path("execute4/", executive4, name="executive4view"),
    path("active/", active, name="activeguestsview")
]


