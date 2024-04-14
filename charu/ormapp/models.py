from django.db import models
from django.contrib import admin
class Books(models.Model):
	bookno         = models.IntegerField(primary_key=True);
	bookname       = models.CharField(max_length=20);
	author         = models.CharField(max_length=20);
	pages          = models.IntegerField();
	published_date = models.DateField();
	bookprice      = models.IntegerField();
class BooksAdmin(admin.ModelAdmin):
	list_display=("bookno","bookname","author","pages","published_date","bookprice");

