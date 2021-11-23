from oscar.apps.checkout.views import *
from oscar.apps.order.utils import OrderNumberGenerator
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse
from oscar.core.loading import get_class, get_model
from oscar.apps.checkout.forms import ShippingAddressForm as ShippingForm
from oscar.apps.address.forms import AbstractAddressForm as AbstractForm
from oscar.apps.checkout.session import CheckoutSessionMixin
from oscar.apps.basket.views import BasketView as Basket
from oscar.apps.checkout.calculators import OrderTotalCalculator
from oscar.apps.partner.strategy import Selector
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
#from django.contrib.gis.geoip import GeoIP

import os
import stripe
from oscar.core.loading import get_class
#Scaffold = get_class('adyen.scaffold', 'Scaffold')
import django
#from custom_apps.checkout.views import AbstractAddressForm
class AbstractAddressForm(AbstractForm):
    def __init__(self, *args, **kwargs):
        """
        Set fields in OSCAR_REQUIRED_ADDRESS_FIELDS as required.
        """
        super().__init__(*args, **kwargs)
        print(self.fields)
        field_names = (set(self.fields)
                       & set(settings.OSCAR_REQUIRED_ADDRESS_FIELDS))
        print(field_names)
        for field_name in field_names:
            self.fields[field_name].required = True



class ShippingAddressForm(ShippingForm):
    def __init__(self, *args, **kwargs):
      
        print(super().__init__(*args, **kwargs))
        super().__init__(*args, **kwargs)
        #self.fields.insert(0,'postcode',self.forms.EmailField(initial=str(time.time())))
    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = [
           'first_name', 'last_name',
            'postcode', 'title', 
            'line1', 'line2', 'line3', 'line4',
            'state', 'country',
            'phone_number', 'notes',
        ]


''' 

from oscar.apps.checkout.utils import CheckoutSessionData

import mercadopago
from api.tests import request

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


stripe.api_key = 'sk_test_51GlbyhHzlEOb03uFZ0ci0YJ97ma6RUitaFXosbrzvLVRN1ZIa8iMxQwNAkww2pVa6V7i0lXsOdc8k6korHzaX83V00tizaViz7'
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
@method_decorator(csrf_exempt, name='dispatch')
class PaymentDetailsView(PaymentDetailsView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        token = request.META.get('CSRF_COOKIE', None)
        if token is None:
            token = csrf._get_new_csrf_key()
            request.META['CSRF_COOKIE'] = token
            request.META['CSRF_COOKIE_USED'] = True

        
        endpoint_secret = 'whsec_Uyi1uPfd4sA2RoZIxvFZKGba3XpCsFNx'
        event = None
        payload = request.data
        sig_header = request.headers['STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            raise e
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            raise e

    # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(payment_intent)
    # ... handle other event types
        else:
            print('Unhandled event type {}'.format(event['type']))

        return JsonResponse(success=True)
     

    

    def get(self, request, *args, **kwargs):
        
        context = super(PaymentDetailsView, self).get_context_data(**kwargs)
        total = context['order_total']
        basket = context['basket']
        prod = Selector()
        prod = prod.strategy(request=request, user=context['user'])
        print("URL: "+ request.get_full_path())
        print("BASKET:")
        print(basket)
        print("CONTEXT:")
        print(context)
        print("ORDER TOTAL:")
        print("TOTAL")
        print(context['order_total'])
        
        items = {'data': []}
        print(context['shipping_address'])
        print( [prod.fetch_for_product(product=i.product).price for i in context['basket'].all_lines() ])
        print()
        #price = int(str(total.incl_tax).replace('.',''))
        for i in context['basket'].all_lines():
            tot =prod.fetch_for_product(product=i.product).price,
            print()
            print(list(tot)[0].excl_tax)
            total = list(tot)[0].excl_tax + list(tot)[0].tax
            print(total)
            total = int(str(total).replace('.',''))
            items['data'].append({
            'price_data': {
                'currency': context['order_total'].currency,
                'product_data': {
                'name': i.product.get_title() ,
                },
                'unit_amount':   total
            },   'quantity': i.quantity,
            
            })
        print(items['data'])
        #print(super().get_order_totals(basket=context,shipping_charge=10))
        urlcancel = request.build_absolute_uri(reverse('checkout:index'))
        urlsucceed = request.build_absolute_uri(super(PaymentDetailsView, self).get_success_url())[:-1]
        print(urlsucceed)
     
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'boleto'],
            
        
    
    shipping_options=[
      {
        'shipping_rate_data': {
          'type': 'fixed_amount',
          'fixed_amount': {
            'amount': 0,
            'currency': 'brl',
          },
          'display_name': 'Free shipping',
          # Delivers between 5-7 business days
          'delivery_estimate': {
            'minimum': {
              'unit': 'business_day',
              'value': 5,
            },
            'maximum': {
              'unit': 'business_day',
              'value': 7,
            },
          }
        }
      },
      {
        'shipping_rate_data': {
          'type': 'fixed_amount',
          'fixed_amount': {
            'amount': 1500,
            'currency': 'brl',
          },
          'display_name': 'Next day air',
          # Delivers in exactly 1 business day
          'delivery_estimate': {
            'minimum': {
              'unit': 'business_day',
              'value': 1,
            },
            'maximum': {
              'unit': 'business_day',
              'value': 1,
            },
          }
        }
      },
    ],
            
            
            line_items=items['data'],
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