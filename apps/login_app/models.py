from __future__ import unicode_literals

from django.db import models
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
	def registerValidation(self, postData):
		results = {'status': True, 'errors': []}
		user = []
		now = datetime.now()
		if not postData ['name'] or len(postData ['name']) < 2:
			results['status'] = False
			results['errors'].append('Name must be at least 3 characters long.')
		if not postData ['alias'] or len(postData ['alias']) < 3:
			results['status'] = False
			results['errors'].append('Alias must be at least 3 characters long.')
		if not postData ['pw'] or len(postData ['pw']) < 8 or postData['pw'] != postData['confirmpw']:
			results['status'] = False
			results['errors'].append('Please confirm password is at least 8 characters long and matches your confirmation.')
		if results['status'] == True:
			user = User.objects.filter(alias = postData['alias'])
		if len(user) != 0:
			results['status'] = False
			results['errors'].append('Alias already exists. Please choose a different one, or Log In.')
		# if not postData ['birthdate'] or postData ['birthdate'] == now.day():
		# 	results['status'] = False
		# 	results['errors'].append('Birthdate may not be empty or equal to the current day.')
		return results

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
		user = User.objects.create(name = postData['name'], alias = postData['alias'], email = postData['email'], password = postData['pw'], birthdate = postData['birthdate'])
		return user

	def loginValidation(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['email']) < 3:
			results['status'] = False
			results['errors'].append('Please register first!')
		else:
			user = User.objects.filter(email = postData['email'])
			if len(user) <=0:
				results['status'] = False
				results['errors'].append('Email does not match. Please try again!')
			elif len(postData['pw']) < 5 or postData['pw'] != user[0].password:
				results['status'] = False
				results['errors'].append('Password does not match. Please try again.')
			else:
				results['user'] = user[0]
		return results

class User(models.Model):
	name = models.CharField(max_length=20)
	alias = models.CharField(max_length=30)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add = True)
	birthdate = models.DateField()	
	objects = UserManager()
