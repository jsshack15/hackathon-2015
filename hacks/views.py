from django.shortcuts import render
from .forms import HackathonForm, CodeManiaForm
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class HackathonView(CreateView):
	template_name = 'hackathon.html'
	form_class = HackathonForm
	success_url = '/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		# form.send_email()
		return super(HackathonView, self).form_valid(form)

class CodeManiaView(CreateView):
	template_name = 'codemania.html'
	form_class = CodeManiaForm
	success_url = '/'

	def form_valid(self, form):
		return super(CodeManiaView, self).form_valid(form)
