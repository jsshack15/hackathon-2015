from django.db import models

# Create your models here.
class Hackathon(models.Model):
	SIZES = (
		(S, 'S'),
		(M, 'M'),
		(L, 'L'),
		(XL, 'XL'),
		(XXL, 'XXL')
		)
	name = models.CharField(max_length = 200, blank = False)
	email = models.EmailField(default = None, blank = False)
	github = models.CharField(default = None)
	linkedin = models.CharField(default = None)
	size = models.CharField(choices = SIZES, default = L)
	phone_number = models.PositiveIntegerField(blank = False)

class CodeMania(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(default = None, blank = False)
	year = models.PositiveIntegerField(default = 1, blank = False)
	phone_number = models.PositiveIntegerField(blank = False)

