from django.shortcuts import render, loader
from django.http import HttpResponse
from django.template import loader
from .models import Room, Item

# Create your views here.
def app(request):
    items = Item.objects.all().values()
    rooms = Room.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'items': items,
        'rooms': rooms
      }
    return HttpResponse(template.render(context, request))

def details(request, id):
  item = Item.objects.get(id=id)
  room = Room.objects.get(id=item.room_id)
  template = loader.get_template('details.html')
  context = {
    'item': item,
    'room': room
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

'''
def testing(request):
  mydata = Member.objects.all()
  mydata1 = Member.objects.values_list('firstname', flat=True)
  mydata2 = Member.objects.filter(firstname='Arda', id=1).values()
  mydata3 = Member.objects.order_by('firstname').values() # ascending order
  mydata4 = Member.objects.order_by('-firstname').values() # descending order
  mydata5 = Member.objects.order_by('lastname','-id').values() # ordering two values
  template = loader.get_template('template.html')
  context = {
    ## if I want to use specific variables in the template, I can pass them here as a dictionary
    'fruits': ['Apple', 'Banana', 'Cherry'],
    #'firstname': 'Arda',
    'greeting' : random.randrange(1,4),
    'mymembers': mydata5,   
  }
  return HttpResponse(template.render(context, request))
'''