from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class Poke(models.Model):
	giver = models.ForeignKey(User, related_name = "giver")
	receiver = models.ForeignKey(User, related_name = "receiver")
	# objects = PokeManager()
