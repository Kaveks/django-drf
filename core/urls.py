"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,)
# create API schema
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #rest_framework  authentication system
     # Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api-auth/', include('rest_framework.urls')),
        #json web tokens
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("admin/", admin.site.urls),
    path("api/",include('Blog_api.urls', namespace='Blog_api')),
    path("api/user/",include('users.urls', namespace='users')),
    path("",include('Blog.urls', namespace='Blog')),
    
    # create API schema
    path('docs/', include_docs_urls(title='BlogAPI')),# api docuentation
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)