"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students_api.views import StudentView
from classes.views import ClassView
from teachers.views import TeacherView, CustomUserCreate
from subjects.views import SubjectView

router = DefaultRouter()

router.register('classes', ClassView)
router.register('students', StudentView)
router.register('teachers', TeacherView)
router.register('subject', SubjectView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    # path('', views.api_root),
    # path('', include('students_api.urls', namespace='students')),
    # path('', include('teachers.urls', namespace='teachers')),
    # path('', include('classes.urls', namespace='classes')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
