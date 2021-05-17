from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [  

    path("", views.index, name="index"),
    path("contact/", views.contact, name="Contact"),
    


    path("subscribe/", views.subscribe, name="Subscribe"),    
   
   


    path("search/", views.search, name="Search"),
    path("search/searchblogdetail/<int:id>", views.searchblogdetail, name="View"),
    path("search/searchmobiledetail/<int:id>", views.searchmobiledetail, name="View"),
    path("search/searchlaptopdetail/<int:id>", views.searchlaptopdetail, name="View"),
        
    
    path("mobilecat/", views.mobilecat, name="MobilCategory"),
    path("mobilecat/mobiledetail/<int:id>", views.mobiledetail, name="View"),

    path("laptopcat/", views.laptopcat, name="Laptopcat"),    
    path("laptopcat/laptopdetail/<int:id>", views.laptopdetail, name="View"),

    path("blog/", views.blog, name="Blog"),
    path("blog/blogview/<int:id>", views.blogview, name="BlogView"),    



    path("dellview/", views.dellview, name="Dellview"),
    path("dellview/delldetail/<int:id>", views.delldetail, name="Delldetail"),
    
    path("appleview/", views.appleview, name="Appleview"),
    path("appleview/appledetail/<int:id>", views.appledetail, name="appledetail"),
   
    path("lenevoview/", views.lenevoview, name="Lenevoview"),
    path("lenevoview/lenevodetail/<int:id>", views.lenevodetail, name="lenevodetail"),
    
    path("acerview/", views.acerview, name="Acerview"),
    path("acerview/acerdetail/<int:id>", views.acerdetail, name="Acerdetail"),
   
    path("msiview/", views.msiview, name="Msivew"),
    path("msiview/msidetail/<int:id>", views.msidetail, name="msidetail"),




    path("applemview/", views.applemobileview, name="Mobileview"),
    path("applemview/applemobiledetail/<int:id>", views.applemobiledetail, name="Mobiledetail"),
    
    path("miview/", views.mimobileview, name="Mobileview"),
    path("miview/mimobiledetail/<int:id>", views.mimobiledetail, name="Mobiledetail"),
    
    path("nokiaview/", views.nokiamobileview, name="Mobileview"),
    path("nokiaview/nokiamobiledetail/<int:id>", views.nokiamobiledetail, name="Mobiledetail"),
    
    
    path("oppoview/", views.oppomobileview, name="Mobileview"),
    path("oppoview/oppomobiledetail/<int:id>", views.oppomobiledetail, name="Mobiledetail"),
    
    path("samsungview/", views.samsungmobileview, name="Mobileview"),
    path("samsungview/samsungmobiledetail/<int:id>", views.samsungmobiledetail, name="Mobiledetail"),
    
    path("vivoview/", views.vivomobileview, name="Mobileview"),
    path("vivoview/vivomobiledetail/<int:id>", views.vivomobiledetail, name="Mobiledetail"),
    
    

  




        

]

