from django.contrib import admin
from models import Usernametw, Direct, Answer

class DirectInline(admin.StackedInline):
    model = Direct
    extra = 3
    

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3


class UserAdmin(admin.ModelAdmin):

	fieldsets = [
        (None,               {'fields': ['usertw']}),
       
        ]
	inlines = [DirectInline, AnswerInline]




admin.site.register(Usernametw, UserAdmin)


# Register your models here.
