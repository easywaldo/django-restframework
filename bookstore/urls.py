from rest_framework.routers import DefaultRouter
from bookstore import views
from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('/author', views.AuthorViewSet)

urlpatterns = [
    path('bookstore-sample/', views.get_book_sample),
    path('bookstore_manage', include(router.urls))
]