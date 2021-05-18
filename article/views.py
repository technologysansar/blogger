from django.shortcuts import render
from math import ceil
# import the logging library
import logging
from .import views
import json
from django.contrib import messages
from django.http import JsonResponse
# Get an instance of a logger
# Create your views here.
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Mobile, Laptop, Blog, Contact, Subscribe

from sendgrid.helpers.mail import Mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import random
from sendgrid import SendGridAPIClient
from django.core import mail
from django.shortcuts import render, redirect
from blogger.settings import EMAIL_HOST_USER 
logger = logging.getLogger(__name__)
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
# Create your views here.


def index(request):		
	#for Slider
	nokia = Mobile.objects.filter(product_brand="Nokia").order_by('-id')[:2]
	sam = Mobile.objects.filter(product_brand="Samsung").order_by('-id')[:2]
	laptop1 = Laptop.objects.all().order_by('-id')[1:2]
	#for body
	mobile = Mobile.objects.all().order_by('-id')[:9]
	laptop = Laptop.objects.all().order_by('-id')[:6]
	#for Blog
	blog = Blog.objects.filter(product_name="Processor").order_by('-id')[:1]
	blog1 = Blog.objects.filter(product_name="Mobile").order_by('-id')[:2]
	blog2 = Blog.objects.filter(product_name="Laptop").order_by('-id')[:1]


	return render(request, 'article/index.html',{'nokia':nokia,'sam':sam, 'laptop1':laptop1, 
		'mobile': mobile, 'laptop':laptop,
		'blog':blog, 'blog1':blog1, 'blog2':blog2}) 
def contact(request):

    thank = False

    if request.method=="POST":
          
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message)
        contact.save()
        thank = True 
        return render(request, 'article/contact.html',{'thank': thank})
    return render(request, 'article/contact.html')	
def mobilecat(request):
	mobilecat = Mobile.objects.all().order_by('-id')
	
	return render(request, 'article/mobilecat.html',{'mobilecat':mobilecat})
def mobiledetail(request, id):

	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()    
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()	
	views = Mobile.objects.filter(id = id)[0]
	views.views = views.views +1
	views.save()
	mobile = Mobile.objects.filter().order_by('-id')[0:5]
	return render(request, 'article/detailview/mobiledetail.html', {'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6, 'view':views,'item':mobile})
def laptopcat(request):
	laptopcat = Laptop.objects.all().order_by('-id')
	return render(request, 'article/laptopcat.html',{'laptopcat':laptopcat})
def laptopdetail(request, id):	
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id = id)[0]
	views.views = views.views +1
	views.save()
	laptop = Laptop.objects.filter().order_by('-id')[0:5]
	return render(request, 'article/detailview/laptopdetail.html', {'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':laptop})
def blog(request):	
	blog = Blog.objects.all().order_by('-id')[0:5]
	
	return render(request, 'article/blog.html',{'blog':blog})
def blogview(request, id):	
	blog = Blog.objects.filter(id = id)[0]
	blog.views = blog.views +1
	blog.save()

	blog2 = Blog.objects.all().order_by('-id')[0:10]
	
	context = {'view':blog,'item':blog2}
	
	return render(request, 'article/detailview/blogview.html',  context )
						
def dellview(request):	
	dellview = Laptop.objects.filter(product_brand="Dell").order_by('-id')
	return render(request, 'article/laptopviews/dellview.html', {'view':dellview})
def delldetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	dell = Laptop.objects.filter(product_brand="Dell").order_by('-id')[0:5]
	return render(request, 'article/laptopviews/delldetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':dell})
def appleview(request):	
	appleview = Laptop.objects.filter(product_brand="Apple").order_by('-id')
	return render(request, 'article/laptopviews/appleview.html', {'view':appleview})
def appledetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	apple = Laptop.objects.filter(product_brand="Apple").order_by('-id')[0:5]
	return render(request, 'article/laptopviews/appledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':apple})
def acerview(request):	
	acerview = Laptop.objects.filter(product_brand="Acer").order_by('-id')
	return render(request, 'article/laptopviews/acerview.html', {'view':acerview})
def acerdetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	acer = Laptop.objects.filter(product_brand="Acer").order_by('-id')[0:5]
	return render(request, 'article/laptopviews/acerdetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':acer})
def lenevoview(request):	
	lenevoview = Laptop.objects.filter(product_brand="Lenevo").order_by('-id')
	return render(request, 'article/laptopviews/lenevoview.html', {'view':lenevoview})
def lenevodetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	lenevo = Laptop.objects.filter(product_brand="Lenevo").order_by('-id')[0:5]
	return render(request, 'article/laptopviews/lenevodetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':lenevo})
def msiview(request):	
	msiview = Laptop.objects.filter(product_brand="MSI").order_by('-id')
	return render(request, 'article/laptopviews/msiview.html', {'view':msiview})
def msidetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="MSI").count()
	views = Laptop.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	msi = Laptop.objects.filter(product_brand="MSI").order_by('-id')[0:5]
	return render(request, 'article/laptopviews/appledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':views,'item':msi})
def applemobileview(request):	
	view = Mobile.objects.filter(product_brand="Apple").order_by('-id')
	return render(request, 'article/mobileviews/applemview.html', {'view':view})
def applemobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	apple = Mobile.objects.filter(product_brand="Apple").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/applemobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'item':apple})	
def mimobileview(request):	
	view = Mobile.objects.filter(product_brand="MI").order_by('-id')
	return render(request, 'article/mobileviews/miview.html', {'view':view})
def mimobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	mi = Mobile.objects.filter(product_brand="MI").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/mimobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'item':mi})
def nokiamobileview(request):	
	view = Mobile.objects.filter(product_brand="Nokia").order_by('-id')
	return render(request, 'article/mobileviews/nokiaview.html', {'view':view})
def nokiamobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	nokia = Mobile.objects.filter(product_brand="Nokia").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/nokiamobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'nokia':nokia})
def oppomobileview(request):	
	view = Mobile.objects.filter(product_brand="Oppo").order_by('-id')
	return render(request, 'article/mobileviews/oppoview.html', {'view':view})
def oppomobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	oppo = Mobile.objects.filter(product_brand="Oppo").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/oppomobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'item':oppo})
def samsungmobileview(request):	
	view = Mobile.objects.filter(product_brand="Samsung").order_by('-id')
	return render(request, 'article/mobileviews/samsungview.html', {'view':view})
def samsungmobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	samsung = Mobile.objects.filter(product_brand="Samsung").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/samsungmobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'item':samsung})
def vivomobileview(request):	
	view = Mobile.objects.filter(product_brand="Vivo").order_by('-id')
	return render(request, 'article/mobileviews/vivoview.html', {'view':view})			
def vivomobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	views = Mobile.objects.filter(id =id)[0]
	views.views = views.views +1
	views.save()
	vivo = Mobile.objects.filter(product_brand="Vivo").order_by('-id')[0:5]
	return render(request, 'article/mobileviews/vivomobiledetail.html',{'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':views,'item':vivo})
def search(request):
	if request.method=="POST":
		srch = request.POST['srh']

		if srch:
			
			laptop = Laptop.objects.filter(Q(product_model__icontains =srch) |
										  Q(titel__icontains=srch) |
										  Q(product_brand__icontains=srch)
										  )
			mobile = Mobile.objects.filter(Q(product_model__icontains =srch) |
										  Q(titel__icontains=srch) |
										  Q(product_brand__icontains=srch)
										  )
			blog = Blog.objects.filter(Q(product_name__icontains =srch) |
										  Q(titel__icontains=srch) 										  
										  )
			
			if laptop:
				return render(request,'article/search.html',{'laptop':laptop})
			
			if mobile:
				return render(request,'article/search.html',{'mobile':mobile})
			if blog:
				return render(request,'article/search.html',{'blog':blog})
			else:
				messages.error(request,'Does Not Match')		
		else:
			messages.warning(request,'Type For Search ')
	return render(request,'article/search.html')				
def searchblogdetail(request, id):	
	blogview = Blog.objects.filter(id = id)[0]
	blog = Blog.objects.all().order_by('-id')
	return render(request, 'article/detailview/blogview.html', {'view':blogview,'item':blog})
def searchmobiledetail(request, id):
	count1 = Mobile.objects.filter(product_brand="Nokia").count()
	count2 = Mobile.objects.filter(product_brand="Samsung").count()
	count3 = Mobile.objects.filter(product_brand="Oppo").count()
	count4 = Mobile.objects.filter(product_brand="Apple").count()
	count5 = Mobile.objects.filter(product_brand="MI").count()
	count6 = Mobile.objects.filter(product_brand="Vivo").count()
	mobileview = Mobile.objects.filter(id = id)[0]
	mobile = Mobile.objects.filter().order_by('-id')[0:5]
	return render(request, 'article/detailview/searchmobiledetail.html', {'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,
		'count6':count6,'view':mobileview,'item':mobile})
def searchlaptopdetail(request, id):
	count1 = Laptop.objects.filter(product_brand="Apple").count()
	count2 = Laptop.objects.filter(product_brand="Dell").count()
	count3 = Laptop.objects.filter(product_brand="Acer").count()
	count4 = Laptop.objects.filter(product_brand="Lenevo").count()
	count5 = Laptop.objects.filter(product_brand="Msi").count()	
	laptopview = Laptop.objects.filter(id = id)[0]
	laptop = Laptop.objects.filter().order_by('-id')[0:5]
	return render(request, 'article/detailview/searchlaptopdetail.html', {'count1':count1,
		'count2':count2,'count3':count3,'count4':count4,'count5':count5,'view':laptopview,'item':laptop})	
def subscribe(request):
	if request.method == 'POST':
		contact = request.POST.get('email', '')
		
		
		if not (Subscribe.objects.filter(Email=contact).exists()):
			contact=Subscribe(Email=contact)
			contact.save()
			
			
			messages.success(request, ' Thank you for subscribing')
			return redirect('index')
		
		else:
			
			messages.success(request, 'Your email address is already exists')
			return redirect('index')
	return render(request, 'article/index.html')							

	
       
		
		
	   	

