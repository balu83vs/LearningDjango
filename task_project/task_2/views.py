from django.shortcuts import render, redirect, HttpResponse
from .models import Notes, NoteUsers
from .forms import UserRegForm, UserLogForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.  
USERS = NoteUsers.objects.all()


def add_user(request):
    if request.method == 'POST':
        reg_form = UserRegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/login/')
            # обработка успешного сохранения
    else:
        reg_form = UserRegForm()
    return render(request, 'reg.html', {'reg_form': reg_form})


def login_page(request):
    if request.method == 'POST':
        log_form = UserLogForm(request.POST)
        if log_form.is_valid():
            user = log_form.cleaned_data['username']
            password = log_form.cleaned_data['password']
            curent_user = authenticate(request, username=user, password=password)
            if curent_user is not None:
                login(request, curent_user)    
                return redirect('/notes/')
            else:
                return redirect('/reg/')
    else:
        log_form = UserLogForm()
    return render(request, 'login.html', {'log_form': log_form})  



def notespage(request):
    try:
        notes = Notes.objects.filter(username_id=request.user)
        return render(request, template_name='notes.html', context={'notes': notes})
    except TypeError:
        return redirect('/login/')
        


def add_notepage(request):

    if request.user not in USERS:
        return redirect('/login/')
    else:
        if request.method == "GET":
            return render(request, "add_note.html")
        else:
            notes = Notes()
            if request.POST['note-text'] is None:
                return HttpResponse("<h3>Заметка не может быть пустой</h3>") 
            else:
                notes.new_note(request.POST['note-text'], request.user)  
                return HttpResponse("<h3>Заметка добавлена</h3>")

def logoutpage(request):
    logout(request)
    return redirect('/login/')            
              

        