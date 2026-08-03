from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Room, Item
from .forms import ItemForm
from .forms import RoomForm

# Create your views here.
def app(request):
    items = Item.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'items': items,
      }
    return HttpResponse(template.render(context, request))

def app1(request):
    rooms = Room.objects.all().values()
    template = loader.get_template('all_rooms.html')
    context = {
        'rooms': rooms
      }
    return HttpResponse(template.render(context, request))

def item_details(request, id):
  item = Item.objects.get(id=id)
  template = loader.get_template('item_details.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))

def room_details(request, id):
  room = Room.objects.get(id=id)
  template = loader.get_template('room_details.html')
  context = {
    'room': room,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_items')
    else:
        form = ItemForm()

    return render(request, 'add_item.html', {'form': form})

def update_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('all_rooms')
    else:
        form = RoomForm(instance=room)

    return render(request, 'update_room.html', {'form': form})

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