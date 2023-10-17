from django.shortcuts import render, redirect

# Create your views here.

posts = [
    {
        'Title': 'Test_title',
        'Description': 'Test_description',
        'Author': 'Test_author',
        'Date': 'Test_date'
    }
]

def indexpage(request):
    return render(request, template_name='index.html', context={'articles': posts, 'page': 'index'})

def aboutpage(request):
    return render(request, template_name='about.html', context={'page': 'about'})

def contactpage(request):
    if request.method == 'GET':
        return render(request, template_name='contact.html', context={'page': 'contact'})
    else:
        with open("D:\py_learning\learning_django\django_stepik\stepik_django_test_1\mainapp\message_result.txt", "a") as message_file:
            message_file.writelines(f'{request.POST["name"]}, {request.POST["email"]}, {request.POST["subject"]}, {request.POST["message"]}\n')
        return redirect(contactpage)