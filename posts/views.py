from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def hello(request):
    # mylist  = [1,2,3,4]
    body = "<h1>Hello<h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Geek Test</title>
    #     </head>
    #     <body>

    #         <h1>Зaголовок первого уровня</h1>
    #         <p>Параграф</p>

    #     </body> 
    #     </html>
    #  """
    headers = {"names": "Alex"}

# "Content-Type":"applivcation/vnd.ms-excel",
# "Content-Dispasition": "attachment"} 
    return HttpResponse( body,headers=headers,status=300)

def get_index(request):
    posts = Post.objects.filter(status = True)
    
    context  = {
        "title" : "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)
    
    # # print (request.__dict__)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else :
    #     return HttpResponse("Не тот метод запроса")
def get_about(reguest):
    return render(reguest, "posts/about.html", context=None )


def get_contacts(reguest):
   return render(reguest, "posts/contacts.html" , context=None )



# новые три поста 
def get_post(reguest):
    return render(reguest, "posts/post_detail.html", context=None)

def update_post (reguest):
    return render(reguest,"posts/post_update.html", context=None)

def delete_post (reguest):
    return render(reguest,"posts/post_create.html", context=None)