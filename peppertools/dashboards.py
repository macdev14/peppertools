from controlcenter import Dashboard, widgets
from pepperadmin.models import Cadastro_OS


class ModelItemList(widgets.ItemList):
    model = Cadastro_OS
    list_display = ('Cliente__nome', 'Numero_Os')

class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )