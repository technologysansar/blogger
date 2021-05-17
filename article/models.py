from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib .auth.models import User

from django.utils.timezone import now
# Create your models here.
       

class Laptop(models.Model):
    product_id = models.AutoField
    product_model = models.CharField(max_length=500, default="")
    product_brand = models.CharField(max_length=500, default="")
    titel = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='article/images', default="")
    date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=500, default="", null="True")
    description = models.TextField(max_length=1000,default="")
    product_des = RichTextUploadingField()
    views = models.IntegerField(default=0)    

    def __str__(self):
        return self.product_model 
class Blog(models.Model):
    blog_id = models.AutoField
    product_name = models.CharField(max_length=500, default="")
    titel = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='article/images', default="")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000,default="")
    product_des = RichTextUploadingField()
    pub_date = models.DateField()
    views = models.IntegerField(default=0)    

    
    def __str__(self):
        return self.titel   


class Mobile(models.Model):
    product_id = models.AutoField
    product_model = models.CharField(max_length=500, default="")
    product_brand = models.CharField(max_length=500, default="")
    titel = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='article/images', default="")
    price = models.CharField(max_length=500, default="", null="True")
    product_des =models.TextField(max_length=1000,default="")
    product_detail =RichTextUploadingField(default="") 
    views = models.IntegerField(default=0)   
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.product_brand   +  '  MODEL   '  +   self.product_model


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True, default="")
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=70, default="")
    message = models.TextField(max_length=500, default="")


    def __str__(self):
        return self.firstname    


class Subscribe(models.Model):
    Email = models.EmailField( null="True", blank="False")

    def __str__(self):
        return self.Email
        
    

      


