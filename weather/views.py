from django.shortcuts import render
import requests
import random

def index(request):
    if request.method == 'POST':
        try:
            ct = request.POST['c'].title()
            c =('http://api.openweathermap.org/data/2.5/forecast?q={}&appid=8bb651b2fae38f17bba4e823c4eb75e9&units=metric').format(ct)
            cmap="https://www.google.com/maps/embed/v1/place?key=AIzaSyA7lDyyF5WebJYGR241iCDxl4f7mvZOy4c&q={}".format(ct)
            w = requests.get(c)
            api =w.json()
            list =[]

            for i in range(len(api['list'])):
                weather={}
                c1=random.randint(1,99)
                c2=random.randint(1,99)
                weather['name']=api['city']['name']
                weather['ab']=api['list'][i]['main']['temp']
                weather['dt'] =api['list'][i]['dt_txt']
                weather['ds'] =api['list'][i]['weather'][0]['description']
                weather['i'] ="http://www.openweathermap.org/img/w/"+api['list'][i]['weather'][0]['icon']+".png"
                weather['cl'] =api['list'][i]['clouds']['all']
                list.append(weather)

            col = '#A'+repr(c1)+'f'+repr(c2)
            print(list)
            return render(request,'weather.html',{'a':list,'color':col,'map':cmap})
        except KeyError:
            return render(request,'weather.html',{'e':"Please Enter A valid City Name!!!"})
    return render(request,'weather.html')
