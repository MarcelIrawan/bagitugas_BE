from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import (CourseViewSet,
                    ProfileGuruViewSet,
                    ProfileMuridViewSet,
                    EnrollmenViewSet,
                    MaterialViewSet)

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
router.register(r"guru", ProfileGuruViewSet, basename="profile-guru")
router.register(r"murid", ProfileMuridViewSet, basename="profile-murid")
router.register(r"enroll", EnrollmenViewSet, basename="enroll")
router.register(r"material", MaterialViewSet, basename="material")

urlpatterns = [
    path("", include(router.urls)),
    # re_path("^users/(?P<email>.+)/$", MaterialViewSet.as_view({'get': 'list'})),
]