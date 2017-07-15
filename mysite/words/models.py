from django.db import models


# Create your models here.
class Rack(models.Model):
	entered_word = models.CharField(max_length=7)

	def __str__(self):
		return self.entered_word