from rest_framework import serializers

from apps.core.models import Student, Course, StudentCourse


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('is_active',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('is_active',)


class StudentCourseSerializer(serializers.ModelSerializer):
    course_data = CourseSerializer(read_only=True, source='course')
    student_data = StudentSerializer(read_only=True, source='student')

    class Meta:
        model = StudentCourse
        fields = '__all__'
        read_only_fields = ('is_active',)
