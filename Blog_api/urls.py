from django.urls import path
from .import  views
 
app_name="Blog_api"
''' when utilizing generic vie '''
urlpatterns = [
    # '''  via id '''
    path("",views.PostList.as_view(),name="blog_list"),
    path("<int:pk>/" ,views.PostDetail.as_view(), name="blog"),
    path('search/', views.PostListFilter.as_view(), name='post_search'),
     # Post Admin URLs
    path('admin/create/',views.CreatePost.as_view(), name='create-post'),
    path('admin/edit/post_detail/<int:pk>/', views.AdminPostDetail.as_view(), name='admin-detail-post'),
    path('admin/edit/<int:pk>/', views.EditPost.as_view(), name='edit-post'),
    path('admin/delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
 ]
''' when utilizing viewsets '''
# from .views import PostList
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls