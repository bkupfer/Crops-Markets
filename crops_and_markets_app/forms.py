from django import forms
from crops_and_markets_app.models import *

# new client forum 
class ClientForm(forms.Form):
	type_of_client = forms.ModelChoiceField(queryset=TypeOfClient.objects.all(), empty_label="Tipo de cliente", widget=forms.Select(attrs={'class':'form-control input-sm'}))

	first_name = forms.CharField(label='Nombre', max_length=100)
	last_name = forms.CharField(label='Apellido', max_length=100)
	contact_number_1 = forms.IntegerField(label='Numero de contacto', required=False)
	contact_number_2 = forms.IntegerField(label='Numero de contacto 2', required=False)
	email = forms.EmailField(required=False)
	observations = forms.CharField(label='Observations', required=False, widget=forms.Textarea(attrs={'placeholder': u'Observaciones'}))

	class Meta:
		model = Client
		# exclude = ('campo_a', 'campo_b', 'campo_c')

