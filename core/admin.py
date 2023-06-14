from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models.teachers import Direction, Teacher


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'direction')
    list_filter = ('is_staff', 'is_superuser', 'direction')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'direction', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'direction', 'image'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
