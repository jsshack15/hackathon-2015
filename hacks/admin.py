from django.contrib import admin
from hacks.models import Hackathon, CodeMania
# Register your models here.


class HackathonAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number", "github", "linkedin", "mac_address", "hardware_required")


class CodeManiaAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number", "course", "branch", "year")

admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(CodeMania, CodeManiaAdmin)
