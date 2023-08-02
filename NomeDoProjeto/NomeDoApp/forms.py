from django.forms import ModelForm
from .models import Pessoas
	
class PessoasForm(ModelForm):
	class Meta:
		model = Pessoas
		fields = "__all__"