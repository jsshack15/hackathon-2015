from django import forms
from hacks.models import Hackathon, CodeMania

class HackathonForm(forms.ModelForm):
    model = Hackathon

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class CodeMainaForm(forms.ModelForm):
	model = CodeMania

	def send_email(self):
		pass