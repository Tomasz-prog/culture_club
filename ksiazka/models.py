from django.db import models


class Ksiazka(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rok_wydania = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    moja_ocena = models.PositiveSmallIntegerField()
    data_przeczytania = models.DateField()
    image = models.ImageField(upload_to="film/images/%Y/%m/%d/", null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "książka"
        verbose_name_plural = "książki"
        unique_together = [['title', 'rok_wydania']]
