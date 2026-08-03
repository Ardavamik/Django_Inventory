from django import forms
from .models import Item, Room

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'demirbas_no', 'room']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']