import requests
from django.http import HttpResponse
from django.shortcuts import render

blog_posts = [
		{
			"filename": "blog/disroot.html",
			"title": "Disroot.org",
			"date": "June 24, 2019",
			"hook" : "disroot",
			"intro" : """
				Have you ever been interested in using common tools but with a little more privacy?
				Then you decide you don't want to put in the work to find and host different tools. What if a group 
				was already doing that for you?
  			""",
		},
		{
			"filename": "blog/elevator.html",
			"title": "Spotted in an elevator",
			"date": "June 01, 2019",
			"hook" : "elevator",
			"intro" : """
				During a recent stay at a hotel I spotted something curious in the elevator.
			"""
		},
		{
			"filename": "blog/openwireless.html",
			"title": "Open Wireless",
			"date": "June 24, 2019",
			"hook" : "openwireless",
			"intro" : """
				Have you ever been stranded somewhere and you need an internet connection?
				You and a lot of other people. Do you like organizations like Electronic Frontier Foundation, mozilla, Internet Archive?
			""",
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
    content = open('content/blog.html').read()
        
    main_data = {
    		'title' : 'Law Technology',
    		'blog_class' : 'active',
    		'copy_year' : '2019',
    		'content' : content,
    		'blog_posts' : blog_posts,
    
    }
    return render(request, 'blog.html', main_data)
    

	
    