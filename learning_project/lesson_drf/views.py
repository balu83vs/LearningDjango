from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from .models import Notes, NoteUser
from .forms import UserRegForm, UserLogForm, AddNoteForm
from .tasks import logout_tsk

from django.shortcuts import HttpResponse

from django.http import JsonResponse

# Create your views here.

def new_user_reg(request):
    if request.method == 'POST':
        reg_form = UserRegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponse('Вы успешно прошли регистрацию')
    else:
        reg_form = UserRegForm()
        return render(request, 'reg_user.html', {'reg_form': reg_form})    


def login_user(request): 
    if request.method == 'POST':
        login_form = UserLogForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            current_user = authenticate(request, username = username, password = password)
        if current_user is not None:
            login(request, current_user)
            request.session['username'] = username
            request.session['is_authenticated'] = True
            return redirect('/notes/')
        else:
            return redirect('/reg_user/')  
    else:
        login_form = UserLogForm()
        return render(request, 'log_user.html', {'log_form': login_form})
    

def logout_page(request):
    del request.session['username']
    logout(request) 
    return redirect('/log_user/')   

def logout_page_in10min(request):
    logout_tsk.apply_async(args= [request], countdown=20)
    return HttpResponse("User Logouted") 

 
def notes_page(request):
    current_user = request.session['username']
    id_user = NoteUser.objects.filter(username=current_user).first()
    notes = Notes.objects.filter(username_id=id_user)
    return render(request, 'notes.html', {'notes': notes})    


def add_note(request):
    if request.method == 'POST':
        note = AddNoteForm(request.POST)
        note.save()
        return HttpResponse('Запись создана')
    else:
        note_form = AddNoteForm()
        return render(request, 'new_notes.html', {'note_form': note_form})
    
    
############################################################################
# представления с использованием rest_frameworks
#############################################################################

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerialiser
from .models import Notes

@api_view(['GET'])
def rest_view_notes(request):
    current_user = request.session['username']
    id_user = NoteUser.objects.filter(username=current_user).first()
    notes = Notes.objects.filter(author=id_user)
    serializer = NoteSerialiser(notes, many=True)
    return Response(serializer.data)    



#AJAX
## проверка уникальности имени пользователя в базе  
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user_exists = NoteUser.objects.filter(username=username).exists()
        return JsonResponse({'result': user_exists})
    return JsonResponse({"error": "Only GET method"}, status=405)