from django.forms import ModelForm
from .models import Serial

class SerialForm(ModelForm):
    class Meta:
        model = Serial
        fields = ['title', 'rok_produkcji', 'ilosc_sezonow', 'moja_ocena',
                  'data_obejrzenia', 'gdzie_obejrzano']