from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('logins', views.login_user, name = 'logins'),
    path('register1', views.register1, name = 'register1'),
    path('logout1', views.logout_user, name = 'logout1'),
    path('portfolios/<int:id>', views.portfolios, name = 'view-portfolios'),
    path('detailPortfolios/<int:id>', views.detailPortfolios, name = 'detailPortfolios'),
    path('addComments/<int:id>', views.addComments, name = "addComments"),
    path('deleteComment/<int:id>/<int:cid>', views.deleteComment, name = "deleteComment"),
    path('bookType/<int:id>', views.bookType, name = "bookType"),
    path('allBookings', views.allBookings, name='allBookings'),
]