from rest_framework.routers import DefaultRouter
from lectures import views
from django.urls import include, path, re_path

## 자동으로 2개의 동작을 구현한 URL 을 만들어준다
lecture_list = views.LectureViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

## 자동으로 2개의 동작을 구현한 URL 을 만들어준다
professor_list = views.ProfessorViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

router = DefaultRouter()
router.register('/lecture', views.LectureViewSet)
router.register('/professor', views.ProfessorViewSet)

urlpatterns = [
    # path('', views.api_root),
    # path('lecture-list/', lecture_list),
    # path('professor-list/', professor_list),
    path('lecture-manager', include(router.urls))    
]