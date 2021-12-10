from oscar.apps.catalogue.views import CatalogueView as Catalogue, ProductDetailView as Product
from custom_apps.analytics.models import ProductRecord
from oscar.core.loading import get_model
class CatalogueView(Catalogue):
    template_name = 'oscar/catalogue/home.html'
    ProductClass = get_model('catalogue', 'ProductClass')
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['analytics'] = ProductRecord.objects.all()
        if not context['analytics']:
            context['analytics'] = self.ProductClass.objects.all()
        print(context['analytics'])
        print(context['analytics'][0].product)
        #print(super().get_context_data()) 
        return super().get_context_data()

class ProductDetailView(Product):
    pass 