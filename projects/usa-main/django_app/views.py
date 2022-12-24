from django.shortcuts import render, redirect
import re
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User 
from django_app import serializers
from django.core.paginator import Paginator
from django_app import models
#
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import MyPostSerializer, ProfileModelSerializer 
from rest_framework import permissions #повторно вызвался
from rest_framework.parsers import MultiPartParser, FormParser #для загрузки картинок
#парсинг
import requests
from bs4 import BeautifulSoup
# доступ к файлам
from django.core.files.storage import FileSystemStorage
#чат
from django.contrib.auth import login
from .forms import SignUpForm


def index(request):
    context={}

    print("index")
    return render(request=request, template_name = 'build/index.html', context=context, status=status.HTTP_200_OK)


# @api_view(http_method_names=["POST", "GET", "PUT"])
# @permission_classes([AllowAny])
def frontpage(request):
    print('frontpage')
    return render(request, 'django_app/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user =form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'django_app/signup.html', {'form': form})


@api_view(http_method_names=["POST", "GET", "PUT"])
@permission_classes([AllowAny])
def parsing_exchange(request): 
    context={}
    #url = "https://jusan.kz/exchange-rates"
    url = "https://www.mig.kz/"

    # verify=False

    headers={
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

    }


    
    req = requests.get(url, headers=headers)
    src= req.text
    # # print(src)

    # with open ("parse.html", "w", encoding="utf-8") as file:
    #     file.write(src)

    # with open ("parse.html", encoding="utf-8") as file:
    #     read = file.read()

        # print(read)


    soup = BeautifulSoup(src, "lxml")
    currency = soup.find_all(class_="currency")
    buy_delta_positive = soup.find_all(True, {'class':['buy', 'delta-positive']})

    sell_delta_positive = soup.find_all(True, {'class':['sell', 'delta-positive']})

    # for item in currency:
    #     print(item.text)

    # for item in buy_delta_positive:
    #     print(item.text)
   
    # for item in sell_delta_positive:
    #     print(item.text)
    newArr = []

    for i in range(len(sell_delta_positive)):
     
        newArr.append({"currency": currency[i].text, "buy_delta_positive":buy_delta_positive[i].text, "sell_delta_positive": sell_delta_positive[i].text})



    return Response( {'data': newArr}, status=status.HTTP_200_OK)
    

@api_view(http_method_names=["POST", "GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile(request): 
    
    
    try:
        if request.user.pk:
            if request.method == "GET":
                
                # User.objects.filter(username = username).exists()
                # obj_user = User.objects.filter(pk = request.user.pk)

                obj_user = User.objects.get(pk = request.user.pk)
             
                serialized_obj_user = serializers.UserModelSerializer(instance=obj_user, many= False).data
                
                

                return Response( {"profile": {"user": serialized_obj_user}},  status=status.HTTP_200_OK)
            if request.method == "PUT":

                email_change = request.data.get("emailChange")
                print(email_change) 
                

                obj_user = User.objects.get(pk = request.user.pk)
                print(obj_user.email)
                print(obj_user)
                if(obj_user.email != email_change):
                    print("изменил")
                    obj_user.email = email_change

                    # User.objects.update_or_create(                        
                    # )
                    obj_user.save()

                    return Response( {"profile": {"email": email_change}},  status=status.HTTP_200_OK)

                print("не изменил")
             
                return Response( {"profile": {"email": "Без изменений"}},  status=status.HTTP_200_OK)

            if request.method == "POST":

                cover = request.data['cover']
                print(cover)
                obj_profile = models.Profile.objects.get(pk=request.user.pk)
                obj_profile.objects.create(avatar=cover)
                obj_profile.save()
          

        else:
            if request.method == "GET":
                return Response( {"profile": {"user": "тест"}},  status=status.HTTP_200_OK)

    except Exception as error:
        print (error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# parser_classes = (MultiPartParser, FormParser)
# @api_view(http_method_names=["POST", "GET", "PUT"])
# @permission_classes([IsAuthenticated])

# def profile_avater(request, format=None):
#     print (request.data)
#     # serializer =  serializers.ProfileModelSerializer(data=request.data)
#     # if serializer.is_valid():
#     #     serializer.save()
#     PostSerializer
#     return Response( {"profile": {"user": "serializer.data"}},  status=status.HTTP_200_OK)
#     # else:
#     #     return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["POST", "GET", "PUT", "DELETE"])    
@permission_classes([IsAuthenticated])
def videos(request):
    if request.method == "GET":
        print(request)

        currentPage = int(request.GET.get("currentPage" ))
        pageSize = int(request.GET.get("pageSize"))
        categoryid = int(request.GET.get("categoryid"))


        print("categoryid")
        print(categoryid)

        print("currentPage")
        print(currentPage)

        print("pageSize")
        print(pageSize)

        if categoryid > 0:
            print("есть категория")
            obj_videos = models.youtube_video.objects.filter(category_id = categoryid)
            serialized_obj_videos = serializers.VideoModelSerializer(instance=obj_videos, many=True).data
            paginator_obj = Paginator(serialized_obj_videos, pageSize)
            currentPage = paginator_obj.get_page(currentPage).object_list

        else:
            print("нет категории")

            obj_videos = models.youtube_video.objects.all()
            serialized_obj_videos = serializers.VideoModelSerializer(instance=obj_videos, many=True).data

            paginator_obj = Paginator(serialized_obj_videos, pageSize)

            currentPage = paginator_obj.get_page(currentPage).object_list

        obj_category = models.youtube_video_category.objects.all()
        serialized_obj_videos_category = serializers.VideoCategoryModelSerializer(instance=obj_category, many=True).data



        return Response( {"videos": currentPage, "conterVideos": obj_videos.count(), "categoryVideos": serialized_obj_videos_category }, status=status.HTTP_200_OK)


# @api_view(http_method_names=["POST", "GET", "PUT", "DELETE"])    
# @permission_classes([IsAuthenticated])
# def 


@api_view(http_method_names=["POST", "GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def users(request):
    if request.method == "GET":
        print(request)



        currentPage = int(request.GET.get("currentPage" ))
        pageSize = int(request.GET.get("pageSize"))

        print("currentPage")
        print(currentPage)

        print("pageSize")
        print(pageSize)

        obj_users = User.objects.all()
        serialized_obj_users = serializers.UserModelSerializer(instance=obj_users, many=True).data

        paginator_obj = Paginator(serialized_obj_users, pageSize)

        currentPage = paginator_obj.get_page(currentPage).object_list
        
        

        return Response( {"datausers": {"users": currentPage, "countUser": obj_users.count()}},  status=status.HTTP_200_OK)

# login react
@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def registration(request):
    if request.method == "POST":
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        # print(f"\nGET {request.GET}")
        # print(f"POST {request.POST}")
        # print(f"data {request.data}")
        # print(f"FILES {request.FILES}\n")

        print(username)
        print(password)

        if username and password:

            if User.objects.filter(username = username).exists():

                return Response( {"errormessage": "пользователь уже существует" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                User.objects.create_user(
                    username=username,                    
                    password=password
                )

                return Response( {"user":  username},  status=status.HTTP_201_CREATED)
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
        # if username and password:

        #     print("ok")
        #     usernamenew = User.objects.get(username = username)
        #     print(usernamenew)

        #     if usernamenew:
        #         return Response( data={"user": usernamenew.username, "message": "Пользователь уже существет с таким логином"},  status=status.HTTP_400_BAD_REQUEST)

              
        #         # User.objects.create_user(
        #         #     username=username,                    
        #         #     password=password
        #         # )
        #         #return Response( {"user": usernamenew["username"]},  status=status.HTTP_200_OK)

        #     else:
        #         return Response( {"user":  usernamenew.username},  status=status.HTTP_200_OK)

         

                
                
        #     return Response(status=status.HTTP_201_CREATED)
           
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





class MyProfilePhoto(APIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileModelSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   

   

    def post(self, request, *args, **kwargs):
        usern=request.user  

        avatar = request.data['avatar']
        print(avatar)

        my_profile_obj = models.Profile.objects.get(user=usern)

        if my_profile_obj.avatar:
        
            fs = FileSystemStorage()
            fs.delete(my_profile_obj.avatar.path)          
        

        my_profile_obj.avatar = avatar
        my_profile_obj.save()

        obj_user = User.objects.get(pk = usern.pk)
        serialized_obj_user = serializers.UserModelSerializer(instance=obj_user, many= False).data

        return Response( {"profile": {"user": serialized_obj_user}},  status=status.HTTP_200_OK)




# картинка

class MyPostViewSet(APIView):    
    queryset = models.MyPost.objects.all()    
    serializer_class = MyPostSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   

    def get(self, request, *args, **kwargs):

        print(request.query_params.get("postid"))

        postid = int(request.query_params.get("postid"))
        if request.query_params.get("pageSize"):
            pagesize = int(request.query_params.get("pageSize"))
        if request.query_params.get("currentPage"):
            currentpage = int(request.query_params.get("currentPage"))

        if(postid > 0):
            print(postid)
            obj_post = models.MyPost.objects.get(pk = postid )
            serialized_obj_post = serializers.MyPostSerializer(instance=obj_post, many=False).data


            return Response( {"post": serialized_obj_post,}, status=status.HTTP_200_OK)

        obj_posts = models.MyPost.objects.all()
        serialized_obj_posts = serializers.MyPostSerializer(instance=obj_posts, many=True).data

        paginator_obj = Paginator(serialized_obj_posts, pagesize)

        currentPage = paginator_obj.get_page(currentpage).object_list

       
        



        return Response( {"posts": currentPage, "conterPosts": obj_posts.count()}, status=status.HTTP_200_OK)
            

        

        
        # print(request.data['postid'])
        # postid = request.data['postid']

        return Response( {"posts": {"postid": postid}},  status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        usern=request.user        
        
        print(request.data['title'])
        print(request.data['description'])
        print(request.data['image_url'])
        # print(request.data["image"])

        # print(request.post)

        # print(img)

        
        image_url = request.data['image_url']
        # print(avatar)
        
        # title = request.data['title']
        # description = request.data['description']

        # models.MyPost.objects.create(creator=usern, title=title, description=description, image_url = image_url)
        
        # models.MyPost.objects.update_or_create(creator=usern, title=title, description=description, image_url = image_url)

        # myobject = models.MyPost.objects.get(creator=usern)

        # myobject.image_url = image_url
        # myobject.save()


        my_profile_obj = models.MyPost.objects.get(creator=usern)
        my_profile_obj.image_url = image_url
        my_profile_obj.save()

        # created = models.MyPost.objects.update(creator=usern, image_url = image_url)


        # post, created = models.MyPost.objects.get_or_create(creator=usern, title=title, description=description, image_url = image_url)



        # obj, created = models.MyPost.update_or_create(
        # creator=usern, title=title, description=description,image_url=image_url,
        # defaults={'creator': usern, 'title':title, 'description': description, 'image_url': image_url},
        # )


        # if created:
        #     print("пост добавлен")
        # else:
        #     print("пост уже есть")
        #     print(post["title"])
        #     print(post.title)     


        

     
        return Response( {"profile": {"user": "тест"}}, status=status.HTTP_200_OK)
 
    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)


