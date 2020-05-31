from django.contrib import admin
from django.urls import path,include
from todolist_application import views as todolist_views
from user_application import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index,name='index'),
    path('todolist/',include('todolist_application.urls')),
    path('account/',include('user_application.urls')),
    path('contact-us',todolist_views.contact,name='contact'),
    path('about-us',todolist_views.about,name='about'),  
]