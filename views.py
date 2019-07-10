import requests
from django.http import HttpResponse
from django.shortcuts import render

blog_posts = [
		{
			"filename": "blog/disroot.html",
			"title": "Disroot.org",
			"date": "June 24, 2019",
			"hook" : "disroot",
		},
		{
			"filename": "blog/elevator.html",
			"title": "Spotted in an elevator",
			"date": "June 01, 2019",
			"hook" : "elevator",
		},
		{
			"filename": "blog/openwireless.html",
			"title": "Open Wireless",
			"date": "June 24, 2019",
			"hook" : "openwireless",
		},
		
	]

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
    
def blog_post(request):
    for blog_post in blog_posts:
	    content = open(blog_post['filename']).read()
    
	    main_data = {
	    		'title' : blog_post['title'],
	    		'blog_class' : 'active',
	    		'copy_year' : '2019',
	    		'content' : content,
	    
	    }
	    return render(request, 'base.html', main_data)
    
    
