from django.db import models
from base.models import User
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    no_of_copies = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    no_of_days = models.IntegerField(default=15)
    book_image = models.ImageField(upload_to='book_images', blank=True,null=True)


class BookRequest(models.Model):
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    status = models.CharField(max_length=10,choices=(('Pending','Pending'),('Accepted','Accepted'),('Rejected','Rejected'),('Closed','Closed')),default="Pending")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
