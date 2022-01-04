from django.db import models

class Platforma():
    NETFLIX, APPLE, AMAZON, CANAL_PLUS, HBO, YOUTUBE, TV, INNE = 0,1,2,3,4,5,6,7
    PLATFORMA = ((NETFLIX,'Netflix'),(APPLE,'Apple'),(AMAZON,'Amazon'),(CANAL_PLUS,'Canal +'),
                 (HBO,'HBO'),(YOUTUBE,'YouTube'),(TV,'TV'),(INNE,'Inne'))

class Serial(models.Model):

    title = models.CharField(max_length=255)
    rok_produkcji = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    ilosc_sezonow = models.PositiveSmallIntegerField()
    moja_ocena = models.PositiveSmallIntegerField()
    data_obejrzenia = models.DateField()
    gdzie_obejrzano = models.PositiveSmallIntegerField(choices=Platforma.PLATFORMA, default=8)
    # image = models.ImageField(upload_to="film/images/%Y/%m/%d/", null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.rok_produkcji}"

    class Meta:

        verbose_name = "seriale"
        verbose_name_plural = "seriale"
        unique_together = [['title', 'rok_produkcji']]
