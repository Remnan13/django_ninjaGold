from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime
from django.contrib import messages


# Create your views here.

def index(request):
	# request.session.clear()
	if 'goldCount' not in request.session:
		request.session['goldCount'] = 0
	if 'messages_list' not in request.session:
		request.session['messages_list'] = []
	return render(request, 'index.html')

def process_gold(request):
	event_list = request.session['messages_list']
	time = datetime.now()
	event = {}

	if request.POST['earn'] == 'reap':
		num = random.randint(50,200)
		request.session['goldCount'] += num
		if num >= 0:
			event['message'] = f"Blood flows out, gold flows in. Collected: {num} gold coins. {time}"
			event['color'] = "green"
		else:
			event['message'] = f"Whispers of failure and betrayal. Lost: {num} gold coins. {time}" 
			event['color'] = "red"


	if request.POST['earn'] == 'weave':
		num = random.randint(35,50)
		request.session['goldCount'] += num
		if num >= 0:
			event['message'] = f"Blood flows out, gold flows in. Collected: {num} gold coins. {time}"
			event['color'] = "green"
		else:
			event['message'] = f"Whispers of failure and betrayal. Lost: {num} gold coins. {time}" 
			event['color'] = 'red' 

	if request.POST['earn'] == 'summon':
		num = random.randint(-200,200)
		request.session['goldCount'] += num
		if num >= 0:
			event['message'] = f"Blood flows out, gold flows in. Collected: {num} gold coins. {time}"
			event['color'] = "green"
		else:
			event['message'] = f"Whispers of failure and betrayal. Lost: {num} gold coins. {time}" 
			event['color'] = 'red'

	if request.POST['earn'] == 'war':
		num = random.randint(-2000,2000)
		request.session['goldCount'] += num
		if num >= 0:
			event['message'] = f"Blood flows out, gold flows in. Collected: {num} gold coins. {time}"
			event['color'] = "green"
		else:
			event['message'] = f"Whispers of failure and betrayal. Lost: {num} gold coins. {time}" 
			event['color'] = 'red'

	event_list.append(event)
	request.session['messages_list'] = event_list
	print(request.session['messages_list'])
	return redirect('/')
