from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), #atilsamancioglu.com/tweetapp/
    path('addtweet/',views.addtweet,name='addtweet') #atilsamancioglu.com/tweetapp/addtweet
]
