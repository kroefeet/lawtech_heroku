import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime

import os
mailgun_api_key = os.environ["MAILGUN_API_KEY"]


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

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    useremail = forms.EmailField(required=TRUE)

def contact_me(request):

	if request.method == 'POST':

		# create a form instance and populate it with data from the request:
		form = UserForm(request.POST)
		print(UserForm)
		# check whether it's valid:
		if form.is_valid():
            name = request.POST["username"]
            email = request.POST["useremail"]
            message = request.POST["message"]

			send_email(name,email,message)

    main_data = {
    		'contact_class' : 'active',
    		'copy_year' : copy_year.year,
    }
    return render(request, 'contact.html', main_data)


def send_email(name,email,message):

	    response = requests.post(
	        "https://api.mailgun.net/v3/mg.law.technology/messages",
	        auth=("api", "MAILGUN_API_KEY"),
	        data={
	        		  "from": email,
	              "to": "admin@law.technology",
	              "subject": "contact from law.technology",
	              "text": [name, email, message]
	              }
	              )


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
