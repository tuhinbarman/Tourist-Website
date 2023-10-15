from django.shortcuts import render
import re
from django.db.models import Q
from .models import State,Location
import openai
from . import data

# Create your views here.



def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Recommend Places in India according to the requirements provided"},
            {"role" : "system" , "content" : "Provide the answer is this format : Location, State - Details of the place" },
            {"role": "user", "content": message},  
        ]
    )
    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer

def get_image(image_message):
    response = openai.Image.create(
        prompt = image_message,
        n = 4,
        size = "256x256"
    )
    image_url = []
    print(response)
    for i in range(0,4):
        image_url.append(response.data[i].url)
    print(image_url)
    return image_url

def search(request):
    trip_type = data.trip_type
    trip_time = data.trip_time
    interests = data.Interest
    context = {
        'trip_type' : trip_type,
        'trip_time' : trip_time,
        'interests' : interests
    }

    return render(request,'search.html',context)

def results(request):
    if request.method =="POST":
        trip_type = request.POST['trip_type']
        trip_time = request.POST['trip_time']
        interests = request.POST.getlist('interests')
        interest_str = ''
        for i in range(0,len(interests)):
            interest_str += interests[i] + ' ,'

        message = 'Suggest me 4 tourist places for '+trip_type + ' trip having interests like ' + interest_str + 'during ' + trip_time
        # message =  "Recommend me  4 places to visit during winter time"
        response = get_response(message)
        # print(message)
        responses = response.split('\n\n')
        print(responses)
        split = re.split(r'\. |\n|, |: | - ', response)
        print(split)

        filter_query = Q()
        for name in split:
            filter_query |= Q(name=name)

        filtered_products = State.objects.filter( filter_query)
        # image_message = "Give me an image of Kashmir"
        # image_url = get_image(image_message)
        context = {
            'responses' : responses,
            'filtered_products' : filtered_products
        }

        return render(request,'results.html',context)

def details(request,id):
    state = State.objects.get(pk = id)
    locations = Location.objects.filter(state = state)
    message = 'create images of local cuisine of '+ state.name
    response = get_image(message)
    
    context = {
        'state' : state,
        'locations' : locations,
        'response' : response
    }
   
    return render(request,'details.html',context)

