
from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('details/',views.news_details, name='details'),
    path('year/<int:year>', views.news_year, name='news'),
    path('register/',views.register, name='add'),
    path('advise/',views.advise, name='advise'),
    path('addUser/', views.addUser, name='addUser'),
    path('predict/', views.predict, name='predict'),
    path('learn/', views.learn, name='learn'),
	path('login/', views.login_action, name='login'),

]