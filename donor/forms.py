from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset
from .models import Donors

class DonorsForm(forms.ModelForm):

	class Meta:
		model = Donors
		fields = '__all__'

	def __init__(self, *args, **kwargs):	
		self.helper = FormHelper()
		self.helper.layout = Layout( 
    		Div('category',),
    		Div(
    			Div('p_no', css_class = 'col-md-4',),
    			Div('p_name', css_class = 'col-md-4',),
    			Div('price', css_class = 'col-md-4',),
    			css_class="row",),

			Div('desc',),
			Div('img',),
			Div(
				Div('donor_name', css_class = 'col-md-6',),
    			Div('phno', css_class = 'col-md-6',),
    			css_class="row",),
			Div(
    			Div('h_no', css_class = 'col-md-4',),
    			Div('city', css_class = 'col-md-4',),
    			Div('pincode', css_class = 'col-md-4',),
    			css_class="row",),
			Div(
				Div('state', css_class = 'col-md-6',),
    			Div('country', css_class = 'col-md-6',),
    			css_class="row",),)

		super(DonorsForm, self).__init__(*args, **kwargs)

        


   









    
	
      

