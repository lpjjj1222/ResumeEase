from django.contrib import admin

from .models import Candidate

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Candidate, CandidateAdmin)