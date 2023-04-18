from django.urls import path
from .import  views
 
app_name="Blog_api"
urlpatterns = [
    path("<int:pk>/" ,views.PostDetails.as_view(), name="detailCreate"),
    path("", views.PostList.as_view(), name="listCreate")
 ]