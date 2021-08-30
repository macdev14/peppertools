from oscar.apps.checkout.views import *
from oscar.apps.order.utils import OrderNumberGenerator
from django.shortcuts import redirect
from django.urls import reverse
''' 

from oscar.apps.checkout.utils import CheckoutSessionData

import mercadopago

class IndexView(IndexView):
    template_name = 'oscar/checkout/checkout.html'
    sdk = mercadopago.SDK("TEST-6269231610656614-063013-3e38194ef7ea8f9aba82897db528cd75-426029374")
    preference_data = {
        "items": []
    }


class ShippingAddressView(ShippingAddressView):
    template_name = 'oscar/checkout/checkout.html'
    sdk = mercadopago.SDK("TEST-6269231610656614-063013-3e38194ef7ea8f9aba82897db528cd75-426029374")
    preference_data = {
        "items": []
    }
'''


#from django.contrib.gis.geoip import GeoIP

import os
import stripe
from oscar.core.loading import get_class
#Scaffold = get_class('adyen.scaffold', 'Scaffold')
import django
stripe.api_key = 'sk_test_51GlbyhHzlEOb03uFZ0ci0YJ97ma6RUitaFXosbrzvLVRN1ZIa8iMxQwNAkww2pVa6V7i0lXsOdc8k6korHzaX83V00tizaViz7'
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PaymentDetailsView(PaymentDetailsView):
    
    def post(self, request, *args, **kwargs):
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
            'price_data': {
                'currency': 'BRL',
                'product_data': {
                'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return redirect(session.url, code=303)
    

    def get(self, request, *args, **kwargs):
        context = super(PaymentDetailsView, self).get_context_data(**kwargs)
        total = context['order_total']
        basket = context['basket']
        print(basket.item)
        print(context)
        urlcancel = request.build_absolute_uri(reverse('checkout:index'))
        urlsucceed = request.build_absolute_uri(super(PaymentDetailsView, self).get_success_url())[:-1]
        print(urlsucceed)
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'boleto'],
            line_items=[{
            'price_data': {
                'currency': 'BRL',
                'product_data': {
                'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url=urlsucceed,
            cancel_url=urlcancel,

        )
        return redirect(session.url, code=303)
    
    def get_context_data(self, **kwargs):
        
        
        '''
        g = GeoIP()
        cod = g.country_code(get_client_ip(self.request))
        print(cod)
        cod = g.country_info(get_client_ip(self.request))
        print(cod)
        '''
        
       
        context = super(PaymentDetailsView, self).get_context_data(**kwargs)
        order_number = OrderNumberGenerator()
        
        obj = context['basket']
        userid = context['user'].id
        client_email = context['user'].email
        total = context['order_total']
        print(context['user'])
        print(context)
        
       
        
        #print(order_number)

        '''
        self.scaffold = Scaffold()
        order_number = order_number.order_number(obj)
        print(order_number)
        form_action_url = self.scaffold.get_form_action(self.request)
        payment_data = {'order_number': order_number, 'client_id' : userid, 'client_email': client_email, 'currency_code':total.currency, 'amount': total.incl_tax, 'shopper_locale': django.utils.translation.get_language(),
        'country_code': 'BRA'
        }
        
        form_fields = self.scaffold.get_form_fields(self.request, payment_data)
        context['form_fields'] = form_fields
        '''
        
        return context