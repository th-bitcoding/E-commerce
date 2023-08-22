import math
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,View
from Client.models import Category
from product.forms import ProductForm
from product.models import Products
from django.urls import reverse_lazy
# Create your views here.
class CategoryCreate(TemplateView):
    template_name = 'client/category.html'

class ProductCreate(CreateView):
    form_class = ProductForm
    model = Products
    template_name='product/addproduct.html'
    success_url = reverse_lazy('product:productadd')

class ProductList(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'product/productlist.html'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Products
    # fields = '__all__'
    template_name = 'product/addproduct.html'
    success_url = reverse_lazy('product:productlist')

class ProductDelete(DeleteView):
    model = Products
    template_name ='product/productdelete.html'
    success_url = reverse_lazy('product:productlist')

def index(request):
    return render(request,'customer/customer.html')

class CustomerProductList(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'customer/customer.html'

class CustomerAddToCart(View):
    pass


from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from product.models import Products

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):
	check = request.user
	data = Products.objects.filter(owner = check)
	price =[int(i.price) for i in data]
	
	
	print('price',price)
	currency = 'INR'
	amount = price[0] *100 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['name'] = check
	
	context['callback_url'] = callback_url

	return render(request, 'client/paymentcheck.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    check = request.user
    data = Products.objects.filter(owner = check)
    price =[int(i.price) for i in data]
    price = price[0]*100
	# only accept POST request.
    if request.method == "POST":
        try:
		
			# get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
            	'razorpay_order_id': razorpay_order_id,
            	'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
				params_dict)
            if result is not None:
                amount = price # Rs. 200
                try:

					# capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
                    return render(request, 'client/paymentsuccess.html')
                except:

					# if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

				# if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

			# if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
	# if other than POST request is made.
        return HttpResponseBadRequest()

