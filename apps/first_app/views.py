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
	event = {
		# 'message': "",
		# 'color': ""
	}

	if request.POST['earn'] == 'reap':
		request.session['num'] = random.randint(50,200)
		request.session['goldCount'] += request.session['num']
		now = datetime.now()
		if request.session['num'] >= 0:
			event['message'] = str(f"Blood flows out, gold flows in. Collected: {{int(request.session.num)}} gold coins. {{request.session.now}}")
			event['color'] = 'green'
		else:
			event['message'] = str("Whispers of failure and betrayal. Lost: "+request.session['num']+" gold coins. ") 
			event['color'] = str('red')


	if request.POST['earn'] == 'weave':
		request.session['num'] += random.randint(35,50)
		request.session['goldCount'] += request.session['num']
		now = datetime.now()
		if request.session['num'] >= 0:
			messages.success(request, "Blood flows out, gold flows in. Collected: "+str(request.session['num'])+" gold coins. ")
		else:
			messages.warning(request, "Whispers of failure and betrayal. Lost: "+str(request.session['num'])+" gold coins. ") 

	if request.POST['earn'] == 'summon':
		request.session['num'] += random.randint(-200,200)
		request.session['goldCount'] += request.session['num']
		now = datetime.now()
		if request.session['num'] >= 0:
			messages.success(request, "Blood flows out, gold flows in. Collected: "+str(request.session['num'])+" gold coins. ")
		else:
			messages.warning(request, "Whispers of failure and betrayal. Lost: "+str(request.session['num'])+" gold coins. ") 

	if request.POST['earn'] == 'war':
		request.session['num'] += random.randint(-2000,2000)
		request.session['goldCount'] += request.session['num']
		now = datetime.now()
		if request.session['num'] >= 0:
			messages.success(request, "Blood flows out, gold flows in. Collected: "+str(request.session['num'])+" gold coins. ")
		else:
			messages.warning(request, "Whispers of failure and betrayal. Lost: "+str(request.session['num'])+" gold coins. ") 
	event_list.append(event)
	request.session['messages_list'] = event_list
	print(request.session['messages_list'])
	return redirect('/')
