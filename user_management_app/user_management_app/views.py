from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
import logging

logger = logging.getLogger(__name__)

# 在适当的位置添加日志记录语句
logger.debug('Debug message')
logger.info('Info message')
logger.error('Error message')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, email=email)
            user.set_password(password)  # 对密码进行哈希处理
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = 'password_reset_done'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = 'password_reset_complete'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

def home_view(request):
    signup_url = reverse('signup')
    login_url = reverse('login')
    context = {
        'signup_url': signup_url,
        'login_url': login_url
    }
    return render(request, 'home.html', context)

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

def user_profile(request):
    return render(request, 'user_profile.html')

def password_change(request):
    return render(request, 'password_change.html')


