from django.shortcuts import render


# My views.
def index_page(request):
    return render(request, "index/home.html")

def about(request):
    return render(request, "index/about2.html")

def contact(request):
    return render(request, "index/contact2.html")

def services(request):
    return render(request, "index/services.html")

def rooms(request):
    return render(request, "index/rooms.html")

def manage_room(request):
    return render(request, "index/admin.html")