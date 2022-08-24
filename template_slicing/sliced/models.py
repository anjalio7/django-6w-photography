from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user (AbstractUser):
    pass

class photography_type (models.Model):
    photography_name = models.CharField(max_length=50, unique=True)
    photography_price = models.IntegerField()

class portofolia(models.Model):
    photography_id = models.ForeignKey(photography_type, on_delete = models.CASCADE , related_name = 'photography_id')
    title = models.CharField(max_length=40, default=None, unique=True)
    coverImage = models.ImageField(upload_to = "image/portfolio/cover/")
    img1 = models.ImageField(upload_to =     'image/portfolio/')
    img2 = models.ImageField(upload_to =     'image/portfolio/')
    img3 = models.ImageField(upload_to =     'image/portfolio/')
    img4 = models.ImageField(upload_to =     'image/portfolio/')
    img5 = models.ImageField(upload_to =     'image/portfolio/')
    
class booking_details(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE , related_name = 'user_id')
    photography_ids = models.ForeignKey(photography_type, on_delete = models.CASCADE , related_name = 'photography_ids')
    booking_date = models.DateField()
    status = models.CharField(max_length=50, default = "pending")
    address = models.CharField(max_length=150)

class reviews(models.Model):
    photography_id = models.ForeignKey(portofolia, on_delete = models.CASCADE , related_name = 'portfolio_id')
    userId = models.ForeignKey(user, on_delete = models.CASCADE, related_name='userId', default='')
    comments = models.CharField(max_length=60)
    commentTime = models.DateTimeField(auto_now=True)



