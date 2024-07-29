from django.contrib import admin

from .models import Candidate, Tag, Invitation, Position, Note

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    list_display = ("name", "status", "uploaded_at")
    prepopulated_fields = {"slug": ("name",)}
    fields=("name","email","phone","cv_file","tags","status","slug","uploaded_at")
    readonly_fields = ("uploaded_at",)


class TagAdmin(admin.ModelAdmin):
    list_filter = ("caption",)
    list_display = ("caption",)

class InvitationAdmin(admin.ModelAdmin):
    list_filter = ("interview_date",)
    list_display = ("interview_date", "position", "candidate")

class PositionAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title",)

class NoteAdmin(admin.ModelAdmin):
    list_filter = ("user",)
    list_display = ("user", "candidate", "text", "created_at")

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Note, NoteAdmin)


