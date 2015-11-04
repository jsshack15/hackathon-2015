from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy

from hacks.models import Hackathon
from hacks.forms import HackathonForm
from .forms import HackathonForm, CodeManiaForm

import json

# Create your views here.

class HackathonView(generic.View):
	def get(self, request):
		form = HackathonForm
		template_name = 'index.html'
		return render(request, template_name)

	def post(self, request):
		try:
			f = HackathonForm(request.POST)
			f.save()
			return HttpResponse(json.dumps({"event":1}), content_type="application/json")
		except Exception as e:
			return HttpResponse(json.dumps(e), content_type="application/json")

# class CodeManiaView(CreateView):
# 	template_name = 'index.html'
# 	form_class = CodeManiaForm
# 	success_url = '/'

# 	def form_valid(self, form):
# 		return super(CodeManiaView, self).form_valid(form)

