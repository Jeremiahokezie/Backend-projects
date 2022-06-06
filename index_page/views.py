from django.shortcuts import render

# My views.
def index_page(request):
    return render(request, "index_page/index_page.html")

def about(request):
    return render(request, "index_page/about.html")

def contact(request):
    return render(request, "index_page/contact.html")

def services(request):
    return render(request, "index_page/services.html")