from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

# def home(request, template = 'index.html'):
# 	return render(request, template, {})

# class HackathonView(generic.Views):
# 	def get(self, request):
# 		"""
# 		Hackathon Home page view
# 		"""
# 		template = 'index.html'
# 		return render(request, template, {})

# 	def post(self, request):

from .forms import HackathonForm, CodeManiaForm
from django.views.generic.edit import FormView

class HackathonView(FormView):
    template_name = 'hackathon.html'
    form_class = HackathonForm
    # success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)

class CodeManiaView(FormView):
	template_name = 'codemania.html'
	form_class = CodeManiaForm

	def form_valid(self, form):
		