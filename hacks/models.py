from django.db import models

# Create your models here.
class Hackathon(models.Model):
	S = 'S'
	M = 'M'
	L = 'L'
	XL ='XL'
	XXL = 'XXL'
	SIZES = (
		(S, 'S'),
		(M, 'M'),
		(L, 'L'),
		(XL, 'XL'),
		(XXL, 'XXL')
		)
	name = models.CharField(max_length = 200, blank = False)
	email = models.EmailField(default = None, blank = False, primary_key = True)
	github = models.URLField(default = None, max_length = 200)
	linkedin = models.URLField(default = None, max_length = 200)
	size = models.CharField(choices = SIZES, default = L, max_length = 5)
	phone_number = models.PositiveIntegerField(blank = False)
	mac_address = models.CharField(blank = False, max_length = 20, default = None)
	hardware_required = models.TextField(null = True)
	# iot_required = models.BooleanField()

class CodeMania(models.Model):
	CSE = 'CSE'
	IT = 'IT'
	EE = 'EE'
	ECE = 'ECE'
	EEE = 'EEE'
	CE = 'CE'
	IC = 'IC'
	ME = 'ME'
	MT = 'MT'
	BRANCH = (
		(CSE, 'Computer Science and Engineering'),
		(IT, 'Information Technology'),
		(EE, 'Electrical Engineering'),
		(ECE, 'Electronics and Communication Engineering'),
		(EEE, 'Electrical and Electronics Engineering'),
		(CE, 'Civil Engineering'),
		(IC, 'Instrumentation and Control Engineering'),
		(ME, 'Mechanical Engineering'),
		(MT, 'Manufacturing Technology'),
	)
	name = models.CharField(max_length = 200)
	email = models.EmailField(default = None, blank = False, primary_key = True)
	year = models.PositiveIntegerField(default = 1, blank = False)
	phone_number = models.CharField(blank = False, max_length = 10)
	course = models.CharField(max_length = 10, blank = False, default = None)
	branch = models.CharField( max_length = 5, null = True)
	year = models.PositiveIntegerField(null = True)

