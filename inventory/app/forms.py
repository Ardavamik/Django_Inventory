from django import forms
from .models import Item, Room

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'demirbas_no', 'allocated_room','bakanlik_adi',
            'daire_adi',
            'malzeme_adi',
             'kiymet',
            'ayniyat_no',
            'fatura_no',
            'status',]


# It is for disabling editable fields in the update form. You can use this form for updating the item details.
#If any specific fields need to be disabled for the update form, you can override the __init__ method and set the disabled attribute for those fields. 
# For example, if you want to disable the 'demirbas_no' field in the update form, you can do it like this:
'''
class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'allocated_room','bakanlik_adi',
            'daire_adi',
            'malzeme_adi',
             'kiymet',
            'ayniyat_no',
            'fatura_no',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["bakanlik_adi"].disabled = True
        self.fields["daire_adi"].disabled = True
        self.fields["kiymet"].disabled = True
        self.fields["ayniyat_no"].disabled = True
        self.fields["fatura_no"].disabled = True
'''

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']


# It is for disabling editable fields in the update form. You can use this form for updating the room details.
'''
class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
            self.fields["room_name"].disabled = True
'''            