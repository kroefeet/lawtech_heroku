import requests
from django.http import HttpResponse
from django.shortcuts import render

	

def contact_me(request):
    content = open('content/contact.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'contact_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'contact.html', main_data)


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
    return render(request, 'index.html', main_data)
    
def projects(request):
    content = open('content/projects.html').read()
    
    main_data = {
    		'title' : 'Law Technology',
    		'projects_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'projects.html', main_data)
    
def blog(request):
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
	
    content = open('content/blog.html').read()
        
    main_data = {
    		'title' : 'Law Technology',
    		'blog_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    
    }
    return render(request, 'blog.html', main_data, {'blog_posts':blog_posts})
    
def blog_post(dict):
    for blog_post in blog_posts:
	    content = open(blog_post['filename']).read()
    
	    data = {
	    		'title' : blog_post['title'],
	    		'pub_date' : blog_post['date'],
	    		'content' : content,
	    		'hook' : blog_post['hook'],
	    
	    }
	    
    
    
