from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('form',views.formpage),
    path('shop',views.shop),
    path('process',views.formpageprocess),
    path('savesession',views.saveSessionData),
    path('getsession',views.getSessionData),
    path('getsession2',views.getSessionData),
    path('removesession',views.deleteSessionData),
    path('login',views.login),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),

    path('maildemo',views.mailsenddemo),

    path('add-student',views.addstudentform),
    path('add-student-process',views.addstudentformprocess),

]