from django.contrib import admin
from teachers.models import NewTeacher
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class TeacherAdminConfig(UserAdmin):
    model = NewTeacher
    search_fields = ('email', 'username', 'name',)
    list_filter = ('email', 'username', 'name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewTeacher, TeacherAdminConfig)