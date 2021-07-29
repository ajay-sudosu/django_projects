from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.db.models import Avg


from . models import Product, Review


class ProductDetailView(DetailView):
	"""Detail view for product"""
	model = Product
	template_name = 'app/detail.html'

	def get_context_data(self, **kwargs):
		"""Overwriting the get context data method to return the average of rating"""
		context = super(ProductDetailView,self).get_context_data(**kwargs)
		context['average'] = Product.objects.aggregate(
			avg_price=Avg('review__rating')
		)
		return context