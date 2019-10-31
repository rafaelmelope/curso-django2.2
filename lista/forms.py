from django.forms import ModelForm
from .models import Lista # Importar Models Lista

class CadastrarForm(ModelForm):
    class Meta:
        model = Lista
        fields = ["title", "created_date", "expire_date"]