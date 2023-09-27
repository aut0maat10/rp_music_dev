from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/v1/users/', views.UserList.as_view()),
    path('api/v1/users/<int:pk>/', views.UserDetail.as_view()),
    path('api/v1/posts/', views.PostList.as_view()),
    path('api/v1/posts/<int:pk>/', views.PostDetail.as_view()),
    path('api/v1/categories/', views.CategoryList.as_view()),
    path('api/v1/categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
