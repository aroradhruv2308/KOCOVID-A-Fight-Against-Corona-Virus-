from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path("contact",views.contact, name='contact'),
    path("help",views.help, name='help'),
    path("nhelp",views.nhelp, name='nhelp'),
    path("table",views.table, name='table'),



]