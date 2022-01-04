from django.db import models
from django.contrib.auth.models import User

class Platforma():
    NETFLIX, APPLE, AMAZON, KINO, CANAL_PLUS, HBO, YOUTUBE, TV, PLAYERPL, INNE = 0,1,2,3,4,5,6,7,8,9
    PLATFORMA = ((NETFLIX,'Netflix'),(APPLE,'Apple'),(AMAZON,'Amazon'),(KINO,'Kino'),(CANAL_PLUS,'Canal +'),
                 (HBO,'HBO'),(YOUTUBE,'YouTube'),(TV,'TV'),(PLAYERPL,'Player.pl'), (INNE,'Inne'))

class Film(models.Model):

    title = models.CharField(max_length=255)
    rok_produkcji = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    moja_ocena = models.PositiveSmallIntegerField()
    data_obejrzenia = models.DateField()
    gdzie_obejrzano = models.PositiveSmallIntegerField(choices=Platforma.PLATFORMA, default=8)
    image = models.ImageField(upload_to="film/images/%Y/%m/%d/", null=True)

    def __str__(self):
        return f"{self.title} - {self.rok_produkcji}"

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "filmy"
        unique_together = [['title', 'rok_produkcji']]