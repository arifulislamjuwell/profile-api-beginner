
from django.urls import path, include
from .views import HelloApiView, HelloViewSets, ProfileViewSet, UserLoginApiView, UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', HelloViewSets, basename= "hello_viewsets")
router.register('profile', ProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('hello-api/', HelloApiView.as_view()),
    path('login/',UserLoginApiView.as_view()),
    path('', include(router.urls))

]
