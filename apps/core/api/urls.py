from rest_framework import routers
from .views import CourseViewSet, StudentCourseViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('student-courses', StudentCourseViewSet, basename='student-course-api')
router.register('students', StudentViewSet, basename='students-api')
router.register('courses', CourseViewSet, basename='courses-api')
urlpatterns = []
urlpatterns += router.urls
