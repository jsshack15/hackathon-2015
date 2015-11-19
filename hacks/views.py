from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from hacks.models import Hackathon, CodeMania, SendRSVP, RSVPConfirmation
from hacks.forms import HackathonForm
from .forms import HackathonForm, CodeManiaForm

import json

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseForbidden

# Create your views here.

class HackathonView(generic.View):
	def get(self, request):
		form = HackathonForm
		template_name = 'index.html'
		return render(request, template_name)

	# def post(self, request):
	# 	try:
	# 		# f = HackathonForm(request.POST)
	# 		# f.save()
	# 		name = request.POST.get('name', None)
	# 		email = request.POST.get('email',None )
	# 		phone_number = request.POST.get('phone_number', None)
	# 		github = request.POST.get('github', None)
	# 		linkedin = request.POST.get('linkedin', None)
	# 		hardware_required= request.POST.get('hardware_required', None)
	# 		mac_address= request.POST.get('mac_address', None)
	# 		size = request.POST.get('size', None)
	# 		Hackathon.objects.create(name = name, email=email, phone_number=phone_number, github=github, linkedin=linkedin, hardware_required = hardware_required, mac_address=mac_address, size=size)
	# 		plaintext = get_template('registration_email.txt')
	# 		htmly     = get_template('registration_email.html')

	# 		d = Context({ 'name': request.POST.get('name', None) })

	# 		subject, from_email, to = 'JSS Hackathon 2015', 'Hackathon 2015<mmil@jssaten.ac.in>', request.POST.get('email', )
	# 		text_content = plaintext.render(d)
	# 		html_content = htmly.render(d)
	# 		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# 		msg.attach_alternative(html_content, "text/html")
	# 		msg.send()
	# 		# send_mail('Hackathon-2015', 'Here is the message.', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', ['deshrajdry@gmail.com'], fail_silently=False)
	# 		return HttpResponse(json.dumps({"event":1}), content_type="application/json")
	# 	except Exception as e:
	# 		return HttpResponse(json.dumps(e), content_type="application/json")

class CodeManiaView(generic.View):
	def get(self, request):
		form = CodeManiaForm
		template_name = 'codemania.html'
		return render(request, template_name, {'form':form})

	# def post(self, request):
	# 	try:
	# 		name = request.POST.get('name', None)
	# 		email = request.POST.get('email',None )
	# 		phone_number = request.POST.get('phone_number', None)
	# 		year = request.POST.get('year', None)
	# 		course= request.POST.get('course', None)
	# 		branch= request.POST.get('branch', None)
	# 		CodeMania.objects.create(name = name, email=email, phone_number=phone_number, year=year, course=course, branch = branch)
	# 		plaintext = get_template('codemania_registration_email.txt')
	# 		htmly     = get_template('codemania_registration_email.html')

	# 		d = Context({ 'name': name})

	# 		subject, from_email, to = 'CodeMania-2015', 'Hackathon 2015 <mmil@jssaten.ac.in>', email
	# 		text_content = plaintext.render(d)
	# 		html_content = htmly.render(d)
	# 		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# 		msg.attach_alternative(html_content, "text/html")
	# 		msg.send()
	# 		# send_mail('Hackathon-2015', 'Here is the message.', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', ['deshrajdry@gmail.com'], fail_silently=False)
	# 		return HttpResponse(json.dumps({"event":1}), content_type="application/json")
	# 	except Exception as e:
	# 		return HttpResponse(json.dumps(e), content_type="application/json")

def handler404(request):
	response = render_to_response('404.html', {},
								  context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('500.html', {},
								  context_instance=RequestContext(request))
	response.status_code = 500
	return response

def problems(request):
	return render_to_response('problems.html')

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)

class sendRSVP(LoginRequiredMixin, generic.View):
	def get(self, request):
		template_name = 'send_rsvp.html'
		return render(request, template_name, )

	def post(self, request):
		import uuid
		emails = request.POST.get('emails', None)
		emails = emails.replace('\r','')
		emails = emails.split('\n')
		plaintext = get_template('rsvp_confirmation_mail.txt')
		htmly     = get_template('rsvp_confirmation_mail.html')
		for email in emails:
			if email is not None or email is not "":
				uid = uuid.uuid4()
				SendRSVP.objects.create(email = email, uid = uid)
				d = Context({ 'uid': uid})
				subject, from_email, to = 'Confirmation: Hackathon-2015 ', 'Hackathon 2015 <mmil@jssaten.ac.in>', email
				text_content = plaintext.render(d)
				html_content = htmly.render(d)
				msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
		return HttpResponse(json.dumps({"Event":"Email Sent to selected list of participants"}), content_type="application/json")

class RSVP(generic.View):
	def get(self, request, uid = None):
		template_name = 'rsvp_view.html'
		uid = str(request.get_full_path()).split('/')[-1]
		if RSVPConfirmation.objects.filter(sent_rsvp__uid = uid):
			return render(request, 'already_confirmed.html', )
		else:
			return render(request, template_name, {'uid': uid})


	def post(self, request, uid):
		uid = str(request.get_full_path()).split('/')[-1]
		if RSVPConfirmation.objects.filter(sent_rsvp__uid = uid).count() == 1:
			return HttpResponseForbidden()
		else:
			college = request.POST.get('college', '')
			status = request.POST.get('status', False)
			rsvp_obj = SendRSVP.objects.filter(uid = str(uid))[0]
			RSVPConfirmation.objects.create(status = status, college = college, sent_rsvp = rsvp_obj)
			return HttpResponse(json.dumps({"event":1}), content_type="application/json")

