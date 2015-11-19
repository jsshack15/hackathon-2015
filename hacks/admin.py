from django.contrib import admin
from hacks.models import Hackathon, CodeMania, SendRSVP, RSVPConfirmation
# Register your models here.


class HackathonAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number", "github", "size", "linkedin", "mac_address", "hardware_required")


class CodeManiaAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number", "course", "branch", "year")

class SendRSVPAdmin(admin.ModelAdmin):
	list_display = ("email", "uid")

class RSVPConfirmationAdmin(admin.ModelAdmin):
	list_display = ("get_email", "college", "status")
	def get_email(self, obj):
		return obj.sent_rsvp.email
	get_email.admin_order_field  = 'sent_rsvp'

admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(CodeMania, CodeManiaAdmin)
admin.site.register(SendRSVP, SendRSVPAdmin)
admin.site.register(RSVPConfirmation, RSVPConfirmationAdmin)
