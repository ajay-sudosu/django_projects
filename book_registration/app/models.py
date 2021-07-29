from django.db import models
from PIL import Image


class User(models.Model):
	book_name=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	genere=models.CharField(max_length=100)
	language=models.CharField(max_length=100)
	image=models.ImageField(default='default.jpg',upload_to='book_image')

	def __str__(self):
		return self.book_name
	