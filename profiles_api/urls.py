from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('helloviewset', views.HelloViewSet, basename = 'helloviewset')

urlpatterns = [
    path('helloview/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
]
