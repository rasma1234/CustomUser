from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    # path('custom/', CustomUserListAPIView.as_view(), name= "custom_list"),
    # path('custom/<int:pk>/', CustomUserDetailAPIView.as_view(), name= "custom_detail"), # to search with numbers
    path('post/', PostListAPIView.as_view(), name= "post_list"),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name= "post_detail"),
]
