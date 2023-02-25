from django.urls import path 
from posts.views import hello,get_index,get_contacts,get_about

urlpatterns = [
path ("hello/", hello,name = "hello-view"),
path ("", get_index , name = "index-page"),
path ("contacts/",get_contacts,name ="endpoint-contact"),
path ("about/", get_about,name="get-about"),
]      
