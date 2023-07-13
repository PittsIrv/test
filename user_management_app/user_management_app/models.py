from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_management_users',
        related_query_name='user_management_user'  # 这里设置了不同的related_query_name
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='user_management_users',
        related_query_name='user_management_user'  # 这里设置了不同的related_query_name
    )
    # Add any additional fields here

    class Meta:
        app_label = 'user_management_app'


