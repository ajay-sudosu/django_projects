from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

def home(request):
	if request.method == "POST":
		if request.POST.get('city'):
			city = request.POST.get('city')
			url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=81ec41c83c9d3897f2f610e25b403671'
			data = requests.get(url).json()
			temp = data.get('main').get('temp')-273 
			real_temp = "{0:.2f}".format(temp)
			context = {
			'city':data.get('name'),
			'temp':real_temp,
			'pressure':data.get('main').get('pressure'),
			'humidity':data.get('main').get('humidity'),
			'country':data.get('sys').get('country'),
			'description':data.get('weather')[0].get('description')
						}
			return redirect(request,'app/weather.html',context)
		else:
			return redirect('home')

	else:
		return render(request,'app/home.html')
		