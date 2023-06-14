from django.contrib.auth.models import AbstractUser, UserManager, Permission, Group
from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TeacherManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=False)

    def create_teacher(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)


class Teacher(AbstractUser):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='teachers')
    image = models.ImageField(upload_to='teachers/%Y/%m/%d', null=True, blank=True)

    objects = TeacherManager()
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='teachers')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True,
                                              related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
