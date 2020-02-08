from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html',{})

def contact(request):

	if request.method == "POST":
		name = request.POST['message-name']
		email = request.POST['message-email']
		message = request.POST['message']

		# send_mail(
		#     'Email From'+name,
		#     message,
		#     email,
		#     ['jasir@rootstalkacademy.com'],
		#     fail_silently=False,
		# )
		return render(request,'contact.html',{'message_name' : name})
	else:
		return render(request,'contact.html',{})
