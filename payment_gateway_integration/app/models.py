from django.db import models

class Payment(models.Model):

	name=models.CharField(max_length=100)
	amount=models.IntegerField()
	payment_id=models.CharField(max_length=100,default=None)
	paid=models.BooleanField(default=False)

	def __str__(self):
		return self.name