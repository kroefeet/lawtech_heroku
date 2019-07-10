import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime

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

copy_year = datetime.datetime.now()	

def contact_me(request):
  
    main_data = {
    		'contact_class' : 'active',
    		'copy_year' : copy_year.year,
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
    
    main_data = {
    		'home_class' : 'active',
    		'copy_year' : copy_year.year,
     }
    return render(request, 'index.html', main_data)
    
def projects(request):
    
    main_data = {
    		'projects_class' : 'active',
			'copy_year' : copy_year.year,
      }
    return render(request, 'projects.html', main_data)
    
def blog(request):
        
    main_data = {
    		'blog_class' : 'active',
    		'blog_posts' : blog_posts,
    		'copy_year' : copy_year.year,
    }
    return render(request, 'blog.html', main_data)
    

	
    