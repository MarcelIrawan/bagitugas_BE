from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (CourseViewSet,
                    ProfileGuruViewSet,
                    ProfileMuridViewSet,
                    EnrollmenViewSet)

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
router.register(r"guru", ProfileGuruViewSet, basename="profile-guru")
router.register(r"murid", ProfileMuridViewSet, basename="profile-murid")
router.register(r"enrollment", EnrollmenViewSet, basename="enrollment")

urlpatterns = [
    path("", include(router.urls))
]