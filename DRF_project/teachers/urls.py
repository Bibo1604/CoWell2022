from django.urls import path, include
from .views import CustomUserCreate, TeacherView

app_name = 'teachers'

urlpatterns = [
    #path('register/', CustomUserCreate.as_view(), name='create_user'),
    #path('', TeacherList.as_view(), name='teachers-list'),
    #path('<int:pk>/', TeacherDetail.as_view(), name='teachers-detail'),
]