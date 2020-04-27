
from django.urls import path, include
from .views import HelloApiView, HelloViewSets
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', HelloViewSets, basename= "hello_viewsets")

urlpatterns = [
    path('hello-api/', HelloApiView.as_view()),
    path('', include(router.urls))

]
