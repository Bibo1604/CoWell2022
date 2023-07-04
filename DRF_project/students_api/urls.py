from django.urls import path, include
from .views import StudentView
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'students_api'

urlpatterns = [
    #path('', StudentList.as_view(), name='students-list'),
    #path('<int:pk>/', StudentDetail.as_view(), name='students-detail'),
    #path('', include(router.urls))
]

