from django.contrib import admin
from .models import poll, question, choice

# Register your models here.
class choices_inline(admin.StackedInline):
    model = choice
    extra = 1


class polls_admin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','start_date','end_date']}),
        (None, {'fields': ['description']})
    ]
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["start_date"]
        else:
            return []


class questions_admin(admin.ModelAdmin):
    inlines = [choices_inline,]


admin.site.register(poll, polls_admin)
admin.site.register(question, questions_admin)
