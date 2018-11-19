from django.forms import ModelForm 
from collection.models import Cheese

class CheeseForm(ModelForm):
    class Meta:
        model = Cheese
        fields = ('name', 'description',)