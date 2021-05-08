from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	phone = models.CharField(max_length=12)
	desc = models.TextField()
	date = models.DateField()
	def __str__(self):
		return self.name


class Help(models.Model):
	name = models.CharField(max_length=122,default='SOME STRING')
	city = models.CharField(max_length=122,default='SOME STRING')
	state = models.CharField(max_length=122,default='SOME STRING')
	phone = models.CharField(max_length=12,default='SOME STRING')
	plasma = models.BooleanField(default=False)
	bed = models.BooleanField(default=False)
	oxygen = models.BooleanField(default=False)
	date = models.DateField()

	def __str__(self):
		return self.name
	
class Plasma(models.Model):
	name = models.CharField(max_length=122,default='SOME STRING')
	city = models.CharField(max_length=122,default='SOME STRING')
	state = models.CharField(max_length=122,default='SOME STRING')
	phone = models.CharField(max_length=12,default='SOME STRING')
	date = models.DateField()
	def __str__(self):
		return self.name

class Bed(models.Model):
	name = models.CharField(max_length=122,default='SOME STRING')
	city = models.CharField(max_length=122,default='SOME STRING')
	state = models.CharField(max_length=122,default='SOME STRING')
	phone = models.CharField(max_length=12,default='SOME STRING')
	date = models.DateField()
	def __str__(self):
		return self.name

class Oxygen(models.Model):
	name = models.CharField(max_length=122,default='SOME STRING')
	city = models.CharField(max_length=122,default='SOME STRING')
	state = models.CharField(max_length=122,default='SOME STRING')
	phone = models.CharField(max_length=12,default='SOME STRING')
	date = models.DateField()
	def __str__(self):
		return self.name	

class nHelp(models.Model):
	name = models.CharField(max_length=122,default='SOME STRING')
	city = models.CharField(max_length=122,default='SOME STRING')
	state = models.CharField(max_length=122,default='SOME STRING')
	phone = models.CharField(max_length=12,default='SOME STRING')
	plasma = models.BooleanField(default=False)
	bed = models.BooleanField(default=False)
	oxygen = models.BooleanField(default=False)
	date = models.DateField()

	def __str__(self):
		return self.name

