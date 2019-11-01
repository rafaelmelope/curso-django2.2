from django.forms import ModelForm
from .models import Lista # Importar Models Lista

class CadastrarForm(ModelForm):
    class Meta:
        model = Lista
        # fields = ["title", "created_date", "expire_date"]
        fields = ["title", "expire_date"]
        labels = {
            'title': ('Produto'),
            'expire_date': ('Data de Validade'),
        }