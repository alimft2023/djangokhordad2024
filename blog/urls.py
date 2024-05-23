from django.urls import path 
from . import views
urlpatterns = [
    path('',views.post,name="post"),
    path('contact/',views.contact,name="contact"),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('details/<int:id>',views.details,name="details"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('create/',views.create,name="create"),
    
]
