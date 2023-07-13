import os
import django

# 设置 DJANGO_SETTINGS_MODULE 环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_management_project.settings")

# 加载 Django 应用程序
django.setup()

# 在此之后可以使用 Django ORM 进行查询和操作
from django.contrib.auth.models import User

# 查询所有用户
users = User.objects.all()

# 遍历输出用户的用户名
for user in users:
    print(user.username)
