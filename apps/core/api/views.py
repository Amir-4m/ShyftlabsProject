from rest_framework import viewsets, mixins

from apps.core.api.serializers import StudentSerializer, StudentCourseSerializer, CourseSerializer
from apps.core.models import Student, Course, StudentCourse
from apps.core.utils.paginations import CustomPagination


class StudentViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentSerializer
    pagination_class = CustomPagination

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        instance.student_courses.all().update(is_active=False)


class CourseViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Course.objects.filter(is_active=True)
    pagination_class = CustomPagination
    serializer_class = CourseSerializer


class StudentCourseViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = StudentCourse.objects.select_related('course', 'student').filter(is_active=True)
    pagination_class = CustomPagination
    serializer_class = StudentCourseSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
