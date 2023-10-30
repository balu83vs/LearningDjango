from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from .models import Notes, NoteUser
from .forms import UserRegForm, UserLogForm, AddNoteForm

from django.shortcuts import HttpResponse

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