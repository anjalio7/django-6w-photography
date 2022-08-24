from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from .import models
import json


from .models import portofolia, user, photography_type
# Create your views here.

def index (request):
    typCount = models.photography_type.objects.all().count()
    portcount = models.portofolia.objects.all().count()
    bookCount = models.booking_details.objects.all().count()
    return render(request,'sliced/home.html', {'typCount': typCount, 'portcount': portcount
    , 'bookCount': bookCount})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "sliced/login.html", {
                "message": "Invalid username and/or password."
        })
        else:
                return render(request, "sliced/login.html", {
                "message": "Invalid username and/or password."
        })
    else:
        return render(request, "sliced/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def addtypes_views(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']

        a = models.photography_type(photography_name = name, photography_price = price)
        a.save()
        return HttpResponseRedirect(reverse('types'))
    else:
        return render(request, "sliced/addtypes.html")

def types(request):
    values = models.photography_type.objects.all()
    print(len(values))
    return render(request, 'sliced/types.html', {'topic': values})

def deletetypes(request, type):
    types = models.photography_type.objects.get(id = type)
    types.delete()
    return HttpResponseRedirect(reverse('types'))

def edittypes(request, type):
    types = models.photography_type.objects.get(id = type)
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']

        types.photography_name = name
        types.photography_price = price
        types.save()
        return HttpResponseRedirect(reverse('types'))
    else:
        return render(request, 'sliced/edittypes.html', {'data': types})

def addportofoli(request):
    data = models.photography_type.objects.all()
    print(data)
    if request.method == 'POST':
        typeName = request.POST['name']
        files = request.FILES.getlist('img1')
        if len(files) != 5:
            return render(request, 'sliced/addportofoli.html', {'message': 'Please upload 5 images', 'data': data})
        else:
            selType = models.photography_type.objects.get(id = typeName)
            img1 = files[0]
            img2 = files[1]
            img3 = files[2]
            img4 = files[3]
            img5 = files[4]
            title = request.POST['title']
            cover = request.FILES['cover']
            a = models.portofolia(photography_id = selType, img1 = img1, img2 = img2, img3 = img3, img4 = img4, img5 = img5, title = title, coverImage = cover)
            a.save()
            # return render(request, 'sliced/addportofoli.html', {'data': data})
            return HttpResponseRedirect(reverse('viewPortfolio'))

    else:
        return render(request, 'sliced/addportofoli.html', {'data': data})


def viewPortfolio(request):
    data = models.portofolia.objects.all()
    return render(request, 'sliced/view-portfolio.html', {'data':data})

def deleteimg(request, type):
    port = models.portofolia.objects.get(id = type)
    port.delete()
    return HttpResponseRedirect(reverse('viewPortfolio'))

def editimg(request, type):
    port = models.portofolia.objects.get(id = type)
    data = models.photography_type.objects.all()
    print(port.photography_id.id)
    if request.method == 'POST':
        typeName = request.POST['name']
        title = request.POST['title']
        files = request.FILES.getlist('img1')
        cover = request.FILES.get('cover')
        if cover is not None:
            port.coverImage = cover
    
        selType = models.photography_type.objects.get(id = typeName)
        if len(files) > 0:
            for i in range(len(files)):
                exec(f'port.img{i+1} = files[i]')
        port.photography_id = selType
        port.title = title
        port.save()
        return HttpResponseRedirect(reverse('viewPortfolio'))

    else:
        return render(request, 'sliced/editportofolio.html', {'port': port, 'data': data})



def detailPortfolio(request, id):
    data = portofolia.objects.get(id = id)
    return render(request, 'sliced/detailPortfolio.html', {'data': data})


def allBookings(request):
    bookData = models.booking_details.objects.all()
    return render(request, 'sliced/bookings.html', {'bookData': bookData})

def changeStatus(request, id, status):
    data = models.booking_details.objects.get(id = id)
    data.status = status
    data.save()
    return HttpResponseRedirect(reverse('allBooking'))