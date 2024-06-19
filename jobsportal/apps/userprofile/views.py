from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Userprofile
# Create your views here.
@login_required
def dashboard(request):
    user_profile = request.user.Userprofile
    return render(request, 'userprofile/dashboard.html', {'userprofile' : user_profile})