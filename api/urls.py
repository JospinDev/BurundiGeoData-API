from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProvinceViewSet, CommuneViewSet, ZoneViewSet, QuartierViewSet

router = DefaultRouter()
router.register('provinces', ProvinceViewSet)
router.register('communes', CommuneViewSet)
router.register('zones', ZoneViewSet)
router.register('quartiers', QuartierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

