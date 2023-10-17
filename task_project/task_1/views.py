from django.shortcuts import render, redirect
from load_file import read_file
from upload_file import write_file

# Create your views here.

def indexpage(request):
    return render(request, template_name='index.html')


def word_listpage(request):
    words_list = read_file()
    return render(request, template_name='words_list.html', context={'words_list': words_list})


def add_wordpage(request):
    if request.method == 'GET':
        return render(request, template_name='add_word.html')
    else:
        write_file(request.POST['word1'], request.POST['word2'])
        return redirect(add_wordpage)
