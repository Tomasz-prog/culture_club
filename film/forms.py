from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'rok_produkcji','moja_ocena',
                  'data_obejrzenia', 'gdzie_obejrzano']