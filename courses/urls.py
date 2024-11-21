from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CourseViewSet, LessonViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('enrollments', EnrollmentViewSet)

urlpatterns = router.urls
