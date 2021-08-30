from oscar.apps.catalogue.views import CatalogueView as Catalogue, ProductDetailView as Product
from custom_apps.analytics.models import ProductRecord
class CatalogueView(Catalogue):
    template_name = 'oscar/catalogue/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['analytics'] = ProductRecord.objects.all()
        print(context['analytics'])
        #print(super().get_context_data()) 
        return super().get_context_data()

class ProductDetailView(Product):
    pass