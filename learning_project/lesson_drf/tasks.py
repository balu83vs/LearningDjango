from celery import shared_task

from django.contrib.auth import logout
from django.shortcuts import redirect


@shared_task(name="logout", ignore_result=False)
def logout_tsk(request):
    del request.session['username']
    logout(request) 
    return redirect('/log_user/')