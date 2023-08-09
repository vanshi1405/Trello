from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router= DefaultRouter()
router.register("org",viewset=OrganizationViewset)
router.register("board",viewset=BoardViewset)
router.register("location",viewset=LocationViewset)
router.register("profile",viewset=ProfileViewset)
router.register("card",viewset=CardViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
]
