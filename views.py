import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')


def contact_me(request):
    content = open('content/contact.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'contact_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'base.html', main_data)


def github_api(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/kroefeet/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
    
def home(request):
    content = open('content/index.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'home_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'base.html', main_data)
    
def projects(request):
    content = open('content/projects.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'projects_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'base.html', main_data)
    
def blog(request):
    content = open('content/blog.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'blog_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'base.html', main_data)
    
    
