from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router= DefaultRouter()
router.register("org",viewset=OrganizationViewset)
router.register("board",viewset=BoardViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
]
