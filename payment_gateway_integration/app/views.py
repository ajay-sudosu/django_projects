from django.shortcuts import render,redirect
from .models import Payment
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# importing razorpay module
import razorpay

# view to render payment detail page
@csrf_exempt
def home(request):
	return render(request,'app/home.html')

# view to render payment gateway page
@csrf_exempt
def payment(request):
	client = razorpay.Client(auth=("rzp_test_rrM8437MCvKP9g", "TTQXTD4jfic8pjeWzlhhOKy0"))
	if request.method=='POST':
		name=request.POST.get('name')
		amount = int(request.POST.get('amount'))*100
		payment = client.order.create(dict(amount=amount, currency='INR',payment_capture='1'))
		coffee=Payment(name=name,amount=amount,payment_id=payment.get('id'))
		coffee.save()
		return render(request,'app/payment.html',{'payment':payment})
	return render(request,'app/payment.html')

# view to render after success payment page
@csrf_exempt
def success(request):
	if request.method=="POST":
		details=request.POST
		print(details)
		order_id=""
		for key,val in details.items():
			if key == 'razorpay_order_id':
				order_id=val
				break
		user=Payment.objects.filter(payment_id=order_id).first()
		user.paid=True
		user.save()
		messages.success(request,f'Payment successful !!!')
	return render(request,'app/success.html')
