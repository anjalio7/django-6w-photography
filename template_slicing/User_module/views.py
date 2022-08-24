from email import message
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from sliced.models import reviews, user, photography_type, portofolia, booking_details

from datetime import date

from django.contrib.auth.decorators import login_required

def index(request):
    imgData = portofolia.objects.order_by('?').first()
    # print(imgData)
    return render(request, 'User_module/main.html', {'img': imgData})

# Start login
def login_user(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index") )

        else:
            return render(request, "User_module/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "User_module/login.html")

# End login

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register1(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "User_module/register.html", {
                "message": "Passwords must match."
            })


        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
            print(users)
        except ValidationError as v:
                return render(request, 'User_module/register.html', {'message': 'Characters must be greater than 3.'})
        except IntegrityError:
            return render(request, "User_module/register.html", {
                "message": "Username already taken."
            })
        
        return render(request, 'User_module/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "User_module/register.html")


def portfolios(request, id):
    selType = photography_type.objects.get(id = id)
    print(selType.photography_name)
    data = portofolia.objects.filter(photography_id = selType)
    return render(request, 'User_module/portfolio.html', {'pdata': data})

def detailPortfolios(request, id):
    data = portofolia.objects.get(id = id)
    commentData = reviews.objects.filter(photography_id = data)
    return render(request, 'User_module/detailPortfolios.html', {'pdata': data, 'comData': commentData})

@login_required(login_url='/logins')
def addComments(request, id):
    selPort = portofolia.objects.get(id = id)
    if request.method == 'POST':
        commt = request.POST['commnt']
        
        a = reviews(userId = request.user, photography_id = selPort, comments = commt)
        a.save()
    data = portofolia.objects.get(id = id)
    commentData = reviews.objects.filter(photography_id = data)
    return render(request, 'User_module/detailPortfolios.html', {'pdata': data, 'comData': commentData})


@login_required(login_url='/logins')
def deleteComment(request, id, cid):
    selCom = reviews.objects.get(id = cid)
    selCom.delete()
    data = portofolia.objects.get(id = id)
    commentData = reviews.objects.filter(photography_id = data)
    return render(request, 'User_module/detailPortfolios.html', {'pdata': data, 'comData': commentData})


@login_required(login_url='/logins')
def bookType(request, id):
    selType = photography_type.objects.get(id = id)
    today = date.today()
    
    if request.method == 'POST':
        bookDate = request.POST['bookDate']
        print(bookDate)
        address = request.POST['address']
        bookData = booking_details.objects.filter(photography_ids = selType, booking_date = bookDate, user_id = request.user)
        if len(bookData) > 0:
            return render(request, 'User_module/booking.html', {'msg': 'Booking can\'t be made for same day.'})
        else:          

            a = booking_details(user_id = request.user, photography_ids = selType, booking_date = bookDate, address = address)
            a.save()
            return HttpResponseRedirect(reverse('allBookings'))
    else:
        return render(request, 'User_module/booking.html', {'selType': selType})


@login_required(login_url='/logins')
def allBookings(request):
    bookData = booking_details.objects.filter(user_id = request.user)
    return render(request, 'User_module/allBookings.html', {'bookData': bookData})