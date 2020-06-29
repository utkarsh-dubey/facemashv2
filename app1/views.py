from django.shortcuts import render
from random import randint
from app1.models import dataBase,dataBase2


def index(request):

	return render(request,'index.html')

def boys(request):

	a = randint(1, 103)
	b = randint(1, 103)
	while a==b:
		b = randint(1,103 )
	filepath = "/static/boys/"+str(a)+".jpg"
	filepath2 = "/static/boys/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}

	left = dataBase2.objects.get(id=a)
	right = dataBase2.objects.get(id=b)
	left.selected = left.selected+1
	right.selected = right.selected+1


	left.save()
	right.save()

	winner_number = 105
	winner =''
	loser=''
	if 'first' in request.POST:
		winner='first'
		winner_number=request.POST['first']
		winner_number=winner_number[winner_number.index('c')+7:winner_number.index('.')]
		loser='second' 
	elif 'second' in request.POST:
		winner='second'
		winner_number=request.POST['second']
		winner_number=winner_number[winner_number.index('c')+7:winner_number.index('.')]
		loser='first'


	winner = dataBase2.objects.get(id=winner_number)
	winner.voted=winner.voted+1
	
	winner.save()

		
	
	return render(request,'boy.html',args)


def home(request):
	
	
	a = randint(1, 123)
	b = randint(1, 123)
	while a==b:
		b = randint(1,123 )
	filepath = "/static/girls/"+str(a)+".jpg"
	filepath2 = "/static/girls/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}

	left = dataBase.objects.get(id=a)
	right = dataBase.objects.get(id=b)
	left.selected = left.selected+1
	right.selected = right.selected+1


	left.save()
	right.save()

	winner_number = 124
	winner =''
	loser=''
	if 'first' in request.POST:
		winner='first'
		winner_number=request.POST['first']
		winner_number=winner_number[winner_number.index('c')+8:winner_number.index('.')]
		loser='second' 
	elif 'second' in request.POST:
		winner='second'
		winner_number=request.POST['second']
		winner_number=winner_number[winner_number.index('c')+8:winner_number.index('.')]
		loser='first'


	winner = dataBase.objects.get(id=winner_number)
	winner.voted=winner.voted+1
	
	winner.save()

		
	return render(request,'girls.html',args)

def rankings(request):

	sortedList = []
	data = {}
	for i in range(1, 123):
		item = dataBase.objects.get(id=i)
		if item.selected == 0:
			item.votePer = 0.0
		else:
			item.votePer = item.voted/item.selected

		if(item.votePer>1.0):
			item.votePer=0.85
		data[i]=item.votePer
	
	sortedList = sorted(data.items() , key=lambda t : t[1], reverse=True)
	args = {}
	temp=[]
	for i in sortedList[:10]:
		temp.append(i[0])
	for i in range(len(temp)):
		temp[i]="/static/girls/"+str(temp[i])+".jpg"

	args["data"]=temp	
	

	return render(request, 'ranking.html', args)
	

def ranking2(request):

	sortedList = []
	data = {}
	for i in range(1, 103):
		item = dataBase2.objects.get(id=i)
		if item.selected == 0:
			item.votePer = 0.0
		else:
			item.votePer = item.voted/item.selected

		if(item.votePer>1.0):
			item.votePer=0.85
		data[i]=item.votePer
	
	sortedList = sorted(data.items() , key=lambda t : t[1], reverse=True)
	args = {}
	temp=[]
	for i in sortedList[:10]:
		temp.append(i[0])
	for i in range(len(temp)):
		temp[i]="/static/boys/"+str(temp[i])+".jpg"

	args["data"]=temp

	return render(request,'ranking2.html',args)