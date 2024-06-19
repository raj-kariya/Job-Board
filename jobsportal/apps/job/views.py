from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import AddJobForum
# Create your views here.

def job_detail(request, job_id):
    job = Job.objects.get(pk = job_id)
    return render(request, 'job/job_detail.html',{'job' : job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForum(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = AddJobForum()
    return render(request,'job/add_job.html', {'form' : form})