from students import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.StudentList.as_view(), name='student-list'),
    path('<int:pk>', views.StudentDetail.as_view(), name='student-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root)
])