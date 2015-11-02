from django import forms
from hacks.models import Hackathon, CodeMania

class HackathonForm(forms.ModelForm):
	class Meta:
		model = Hackathon
		fields = '__all__'

	def send_email(self):
		# send email using the self.cleaned_data dictionary
		pass

class CodeManiaForm(forms.ModelForm):
	class Meta:
		model = CodeMania
		fields = '__all__'

	def send_email(self):
		pass