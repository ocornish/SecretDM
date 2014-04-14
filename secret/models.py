from django.db import models
from django.contrib.auth.models import User


class Usernametw(models.Model):
	usertw = models.CharField(max_length = 15)
	def __unicode__(self):
		return self.usertw

class Direct(models.Model):
    message = models.CharField(max_length = 140)
    pub_date = models.DateTimeField('date published')
    usuario = models.ForeignKey(Usernametw)
    users = models.ForeignKey(User)
    manage = 1
    def __unicode__(self):
    	return self.message

class Answer(models.Model):
    message = models.CharField(max_length = 140)
    pub_date = models.DateTimeField('date published')
    usuario = models.ForeignKey(Usernametw)
    users = models.ForeignKey(User)
    manage = 2
    def __unicode__(self):
    	return self.message
