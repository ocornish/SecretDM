from django.shortcuts import render_to_response,get_object_or_404, render
from django.contrib.auth.models import Permission, User
from django.template.context import RequestContext
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from operator import attrgetter
from itertools import chain


# Create your views here.
def home(request):
    template = "index.html"
    return render(request, template)

@login_required
def message(request):
	current_user = request.user #obtenemos id de usuario http://stackoverflow.com/questions/12615154/how-to-getting-currently-logged-user-id-in-django
	usuarios = Usernametw.objects.all()
	respuesta = Answer.objects.filter(users=current_user)
	enviado = Direct.objects.filter(users=current_user)
	result_list = sorted(chain(respuesta, enviado), key=attrgetter('pub_date')) #combine querys http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
	template = "mensajes.html"
	return render(request, template,locals())


@login_required
def messages(request, id_messages):
	current_user = request.user #obtenemos id de usuario http://stackoverflow.com/questions/12615154/how-to-getting-currently-logged-user-id-in-django
	usuarios = Usernametw.objects.all()
	user = get_object_or_404(Usernametw, pk = id_messages)
	respuesta = Answer.objects.filter(users=current_user, usuario__usertw=user)
	enviado = Direct.objects.filter(users=current_user, usuario__usertw=user)
	result_list = sorted(chain(respuesta, enviado), key=attrgetter('pub_date')) #combine querys http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
	template = "mensajes_user.html"
	return render(request, template,locals())
