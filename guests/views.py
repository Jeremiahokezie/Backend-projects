from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Guest


#My views
def deluxe1(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/deluxeguest1.html")

def deluxe2(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/deluxeguest2.html")

def deluxe3(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/deluxeguest3.html")

def deluxe4(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/deluxeguest4.html")

def executive1(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/executiveguest1.html")

def executive2(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/executiveguest2.html")

def executive3(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/executiveguest3.html")

def executive4(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/executiveguest4.html")

def standard1(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/standardguest1.html")

def standard2(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/standardguest2.html")

def standard3(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/standardguest3.html")

def standard4(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        occupation = request.POST.get("Occupation")
        roomcategory = request.POST.get("Room_Category")
        roomtype = request.POST.get("Room_Type")
        roomnumber = request.POST.get("Room_Number")
        amount = request.POST.get("Amount_Paid")
        nights = request.POST.get("Number_of_Nights")
        start = request.POST.get("Start_Date")
        end = request.POST.get("End_Date")
        new_guest = Guest(Name=name, Email=email, Occupation=occupation, Room_Category=roomcategory, Room_Type=roomtype, Room_Number=roomnumber, Amount_Paid=amount, Number_of_Nights=nights, Start_Date=start, End_Date=end)
        new_guest.save()
        return redirect("guests:recordsview")
    return render(request, "guests/standardguest4.html")

def active(request):
    guests = Guest.objects.all().values()
    

    context = {
        "guest":guests,
        
    }
    return render(request, "guests/activeguests.html", context)

def record(request):
    return render(request, "guests/record.html")



