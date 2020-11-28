from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import (ProfileGuru, 
                    ProfileMurid, 
                    Course, 
                    Enrollment)
from .serializers import (ProfileGuruSerializer, 
                            ProfileMuridSerializer, 
                            CourseSerializer,
                            EnrollmentSerializer)


class ProfileGuruViewSet(ModelViewSet):
    """
    View set for course
    """

    serializer_class = ProfileGuruSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ProfileGuru.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
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


class CourseViewSet(ModelViewSet):
    """
    View set for course
    """

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Course.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
        return queryset
    
    def perform_create(self, serializer):
        teacher = self.request.user
        serializer.save(teacher=teacher)


class EnrollmenViewSet(ModelViewSet):
    """
    View set for enrollment
    """

    serializer_class = EnrollmentSerializer
    perimission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Course.objects.all()
        email = self.request.query_params.get("email", None)
        if email is not None:
            queryset = queryset.filter(user__user__email=email)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)