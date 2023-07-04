from django.urls import path
from django.views.generic import TemplateView

app_name = 'students'

urlpatterns = [
    path('', TemplateView.as_view(template_name="students/index.html"))
]