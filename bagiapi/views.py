from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from .models import (ProfileGuru, 
                    ProfileMurid, 
                    Course, 
                    Enrollment,
                    Material)
from .serializers import (ProfileGuruSerializer, 
                            ProfileMuridSerializer, 
                            CourseSerializer,
                            EnrollmentSerializer,
                          MaterialSerializer)


class ProfileGuruViewSet(ModelViewSet):
    """
    View set for course
    """

    serializer_class = ProfileGuruSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    filterset_fields = ('user',)

    def get_queryset(self):
        queryset = ProfileGuru.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__email=email)
            return queryset
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ProfileMuridViewSet(ModelViewSet):
    """
    View set for course
    """

    serializer_class = ProfileMuridSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ProfileMurid.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
        return queryset



    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


    # def get_object(self):
    #     user = self.request.query_params.get("email", None)
    #     return ProfileMurid.objects.filter(user=user)


class CourseViewSet(ModelViewSet):
    """
    View set for course
    """

    serializer_class = CourseSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Course.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
        return queryset
    
    def perform_create(self, serializer):
        teacher = self.request.user
        serializer.save(teacher=teacher)

class MaterialViewSet(ModelViewSet):
    """
    Viewset for material
    """
    serializer_class = MaterialSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    filterset_fields = ('course',)

    def get_queryset(self):
        queryset = Material.objects.all()
        course = self.request.query_params.get("course", None)
        if course is not None:
            queryset = queryset.filter(course=course)
        return queryset

    def perform_create(self, serializer):
        # course = self.request.course
        serializer.save()


class EnrollmenViewSet(ModelViewSet):
    """
    View set for enrollment
    """

    serializer_class = EnrollmentSerializer
    perimission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Enrollment.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)