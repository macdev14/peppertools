from oscar.apps.catalogue.views import CatalogueView as Catalogue, ProductCategoryView as Category, ProductDetailView as Product
from custom_apps.analytics.models import ProductRecord
from oscar.core.loading import get_model
class CatalogueView(Catalogue):
    pass
    # template_name = 'oscar/catalogue/home.html'
    # ProductClass = get_model('catalogue', 'ProductClass')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['analytics'] = ProductRecord.objects.all()
    #     if context['analytics']:
    #         print(context['analytics'])
    #         print(context['analytics'][0].product)
    #     else:
    #         context['analytics'] = self.ProductClass.objects.all()
        
    #     #print(super().get_context_data()) 
    #     return super().get_context_data()

class ProductDetailView(Product):
    pass

class ProductCategoryView(Category):
    # template_name = 'oscar/catalogue/search/results.html'
    pass 