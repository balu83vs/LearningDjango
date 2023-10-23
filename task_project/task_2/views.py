from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Notes, NoteUsers
from .forms import UserRegForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.  
USERS = NoteUsers.objects.all()

"""
def add_user(request):
    if request.method == "GET":
        return render(request, "reg.html")
    else:
        data = request.POST
        if data['username'] is None:
            return HttpResponse("<h3>Введите логин пользователя</h3>")
        elif data['first_name'] is None:
            return HttpResponse("<h3>Введите имя пользователя</h3>")
        elif data['last_name'] is None:
            return HttpResponse("<h3>Введите фамилию пользователя</h3>")
        elif data['password1'] is None or data['password2'] is None:
            return HttpResponse("<h3>Введите пароль</h3>")
        elif data['password1'] != data['password2']:
            return HttpResponse("<h3>Пароли должны совпадать</h3>")
        else:
            newuser = NoteUsers()
            newuser.create_user(data)
            return HttpResponse("<h3>Вы успешно зарегистрировались</h3>")
"""

def add_user(request):
    if request.method == 'POST':
        reg_form = UserRegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponse("<h3>Вы успешно зарегистрировались</h3>")
            # обработка успешного сохранения
    else:
        reg_form = UserRegForm()
    return render(request, 'reg.html', {'reg_form': reg_form})


def login_page(request):
    if request.user in USERS:
        return HttpResponseRedirect('/logout/')
    else:
        if request.method == "GET":
            return render(request, "login.html")
        else:
            data = request.POST
            try:
                user = authenticate(request, username=data['username'], password=data['password'])
                print(data)
                if user is None:
                    return HttpResponse("<h3>Пользователь с таким логином и паролем не найден</h3>")
                login(request, user)
                return HttpResponse("<h3>Вы успешно авторизованы</h3>")
            except KeyError:
                return HttpResponse("<h3>Заполните все поля</h3>")    


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
    return HttpResponseRedirect('/login/')            
              

        