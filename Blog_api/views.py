from rest_framework import generics
from Blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, IsAuthenticated, 
    IsAuthenticatedOrReadOnly, BasePermission, 
    IsAdminUser, DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
)
# Building custom permissions on rest_framework

#from snippets.permissions import IsOwnerOrReadOnly
#permission class
class PostEditingPermissions(BasePermission):
    message="Editing Post is restricted to author only!"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            ''' SAFE_METHODS in rest_framework are, GET,OPTIONS and HEAD 
                which are basically readonly permissions'''
            return True
        return obj.author==request.user
class PostList(generics.ListCreateAPIView):
    #permission_classes=[IsAdminUser]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes=[DjangoModelPermissions]
    queryset= Post.post_objects.all()
    serializer_class=PostSerializer


#Permissions vs HTTP Request

'''
Permissions  vs   HTTP request object
1) View             GET
2) delete           DELETE
3)Change            PUTPATCH
4) Add              POST
'''



class PostDetails(generics.RetrieveUpdateDestroyAPIView,PostEditingPermissions):
    permission_classes=[PostEditingPermissions]
    queryset= Post.post_objects.all()
    serializer_class=PostSerializer



"""Concrete View Classes
1) CreateAPIView
Used for create-only endpoints.

2)ListAPIView
Used for read-only endpoints to represent a collection of model instances.

3)RetrieveAPIView
Used for read-only endpoints to represent a single model instance.

4)DestroyAPIView
Used for delete-only endpoints for a single model instance.

5)UpdateAPIView
Used for update-only endpoints for a single model instance.

6)ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.

7)RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.

8)RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.

9)RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""