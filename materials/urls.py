from rest_framework.routers import SimpleRouter
from materials.views import CourseViewSet, LessonUpdateApiView, LessonDestroyApiView, LessonListApiView, LessonCreateApiView, LessonRetrieveApiView
from materials.apps import MaterialsConfig
from django.urls import path, include

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),
]

urlpatterns += router.urls
