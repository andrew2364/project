from django.db import models

class Arkans(models.Model):

    cel = models.TextField(max_length=1000)
    osnova = models.TextField(max_length=1000)
    jertva = models.TextField(max_length=1000)