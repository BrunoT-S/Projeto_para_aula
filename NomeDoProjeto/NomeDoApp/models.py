from django.db import models

# Create your models here.
class Pessoas(models.Model):
	nome = models.CharField(max_length=255)
	cidade = models.CharField(max_length=255)
	criacao = models.DateTimeField(auto_now_add=True)
