from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from trello1.viewsets import organization,profile,location,board,card

router= DefaultRouter()
router.register("org",viewset=organization.OrganizationViewset)
router.register("board",viewset=board.BoardViewset)
router.register("location",viewset=location.LocationViewset)
router.register("profile",viewset=profile.ProfileViewset)
router.register("card",viewset=card.CardViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
]
