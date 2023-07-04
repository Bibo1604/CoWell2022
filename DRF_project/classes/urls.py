from django.urls import path, include
from .views import ClassView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'classes'

urlpatterns = [
    #path('', ClassList.as_view(), name='classes-list'),
    #path('<int:pk>/', ClassDetail.as_view(), name='classes-detail'),
]
