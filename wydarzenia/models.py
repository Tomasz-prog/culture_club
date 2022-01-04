from django.db import models

class type_event():
    PRYWATNE, ZAWODOWE, KODOWANIE = 0,1,2
    TYPE_EVENT = ((PRYWATNE, 'Prywatne'), (ZAWODOWE, 'zawodowe'), (KODOWANIE, 'programowanie'))

class Event(models.Model):

    title = models.TextField()
    data_wydarzenia = models.DateField()
    miejsce = models.CharField(max_length=255)
    osoby = models.CharField(max_length=500)
    rodzaj = models.PositiveSmallIntegerField(choices=type_event.TYPE_EVENT, default=0)

    def __str__(self):
        return f"{self.data_wydarzenia} - {self.miejsce}"

