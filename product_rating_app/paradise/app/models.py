from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
	"""Database Model For Product """
	name = models.CharField(max_length=100)

	def __str__(self):
		"""String Representation for product object"""
		return self.name


class Review(models.Model):
	"""Database model for review"""
	rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
	product = models.ForeignKey('Product', on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
