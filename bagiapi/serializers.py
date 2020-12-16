from rest_framework import serializers

from .models import (CustomUser,
                     ProfileGuru,
                     ProfileMurid,
                     Course,
                     Enrollment,
                     Material)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['id','email']

class ProfileGuruSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileGuru
        fields = '__all__'
        # fields = ['id','user','nama','nuptk','institusi']

class ProfileMuridSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileMurid
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):

    # course = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Material
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # teacher = UserSerializer(many=False)
    teacher = serializers.StringRelatedField(read_only=True)
    # material = MaterialSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ('teacher','judul','deskripsi','reward','created_at','updated_at','student','material')


class EnrollmentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Enrollment
        fields = '__all__'


