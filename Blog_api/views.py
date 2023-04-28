from rest_framework import generics
from Blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, IsAuthenticated, 
    IsAuthenticatedOrReadOnly, BasePermission, 
    IsAdminUser, DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
)
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Building custom permissions on rest_framework

#from snippets.permissions import IsOwnerOrReadOnly
#permission class
''' can be used when you want the user to only see their items in absence of filtering '''
class PostEditingPermissions(BasePermission):
    message="Editing Post is restricted to author only!"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author==request.user
    
# Use normal view system with generic views
''' use generic view '''


"""Concrete Generic View Classes
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
class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        # user= self.request.user
        # return Post.post_objects.filter(author=user)
        return Post.post_objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        ''' view individual item via id '''
        item_id=self.kwargs['pk']
        print('itemId: ',item_id)
        return Post.post_objects.filter(id=item_id)
        

#from django_filters import rest_framework as filters
from rest_framework import filters


''''^' Starts-with search.
    '=' Exact matches.
    '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    '$' Regex search. 
'''

class PostListFilter(generics.ListAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_backends = [filters.SearchFilter]
    #filterset_fields = ('category', 'Books')
    search_fields = ['^slug']



# class CreatePost(generics.CreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


'''
Permissions  vs   HTTP request object
1) View             GET
2) delete           DELETE
3)Change            PUTPATCH
4) Add              POST
'''

''' useful functions while utilizing viewsets '''
    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #  
'''Use of viewsets'''
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset=Post.post_objects.all()
    
#     def list(self, request):
#         serializer_class=PostSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)

#     def retrieve(self ,request,pk=None):
#         post=get_object_or_404(self.queryset,pk=pk)
#         serializer_class=PostSerializer(post)
#         return Response(serializer_class.data)

'''use of model viewsets'''
# class PostList(viewsets.ModelViewSet):
#     #permission_classes=[PostEditingPermissions]
#     permission_classes = [IsAuthenticated,]#PostEditingPermissions]
#     serializer_class = PostSerializer

#       # Define Custom Queryset
#     def get_queryset(self):
#         user=self.request.user
#         ''' show only what the user has posted '''
#         return Post.post_objects.filter(author=user)
#         ''' show all post irrespective of the poster '''
#         #return Post.post_objects.all()

#     # select individual items using slug
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

  


