from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index,name="home"),
    path('login', views.login_view,name="login"),
    path('logout', views.logout_view, name = "logout"),
    path('addtypes', views.addtypes_views, name = "addtypes"),
    path('types',views.types,name="types"),
    path('deletetypes/<int:type>', views.deletetypes, name = "deletetypes"),

    path('types/<int:type>', views.edittypes, name= "edittypes"),
    path('addportfoli', views.addportofoli, name= "addportfoli"),
    path('view-portfolio', views.viewPortfolio, name = "viewPortfolio"),
    path('deletePortfolio/<int:type>', views.deleteimg, name = "deletePortfolio"),

    path('editPortfolio/<int:type>', views.editimg, name= "editPortfolio"),
    path('detailPortfolio/<int:id>', views.detailPortfolio, name= "detailPortfolio"),
    path('allBooking', views.allBookings, name= "allBooking"),
    path('changeStatus/<int:id>/<str:status>', views.changeStatus, name= "changeStatus"),
]