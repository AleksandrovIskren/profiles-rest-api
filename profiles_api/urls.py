from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


"""This is the way to register a URL for a ViewSet"""
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

"""This is the way to register a URL for a APIView"""
urlpatterns = [
                path('hello-view/', views.HelloApiView.as_view()),
                path('login/', views.UserLoginApiView.as_view()),
                path('', include(router.urls)) # This part is for the viewset
            ]
