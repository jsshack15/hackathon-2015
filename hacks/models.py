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
	size = models.CharField(default = None, max_length = 5)
	phone_number = models.CharField(max_length = 13)
	mac_address = models.CharField(blank = False, max_length = 20, default = None)
	hardware_required = models.TextField(null = True, blank = True)
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
	phone_number = models.CharField(max_length = 13)
	year = models.CharField(max_length = 10, default = None, null = True)
	course = models.CharField(max_length = 10, blank = False, default = None)
	branch = models.CharField( max_length = 5, null = True)

class SendRSVP(models.Model):
	email = models.EmailField(default = None, blank = False)
	uid = models.CharField(max_length = 200, default = None)

class RSVPConfirmation(models.Model):
	sent_rsvp = models.ForeignKey(SendRSVP)
	status = models.BooleanField(default = False)
	college = models.CharField(default = None, max_length = 500)
