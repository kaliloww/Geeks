from django.urls import path 
from posts.views import hello, get_index, get_contacts, get_about , get_post , update_post , delete_post

urlpatterns = [
path ("hello/", hello, name ="hello-view"),
path ("", get_index, name ="index-page"),
path ("contacts/",get_contacts, name ="endpoint-contact"),
path ("about/", get_about, name="get-about"),
path ("get_post/", get_post , name="get-post"),
path ("update/", update_post, name="update-post"),
path ("delete/", delete_post, name="delete-post"),
]      
