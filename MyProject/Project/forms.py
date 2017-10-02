from django import forms
from Project.models import Account, ReserveParking
from django.forms import ModelForm, widgets
from django.core import validators
from django.contrib.admin import widgets





SLOT_CHOICES = ( (x,x) for x in range(1,29)


	)

# # class NewLogin(forms.ModelForm):

# 	Username = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder ' : 'Username'}), label = '')
# 	Password = forms.CharField(widget = forms.PasswordInput(attrs = {'class ': 'form-control', 'placeholder' : 'Password'}), label = '')

# 	class Meta():
# 		model = Account
# 		fields = ["Username", "Password"]

# class NewReserveParking(forms.ModelForm):

# 	Slot_no = forms.CharField( widget = forms.Select(choices = SLOT_CHOICES, attrs= {'class' : 'form-control', 'placeholder ' : 'Slot Number'}), label = 'Slot Number')
# 	Time_in = forms.DateTimeField()

	# class Meta():

	# 	model = ReserveParking
	# 	fields = ['Slot_no', 'Time_in']
	#  def __init__(self, *args, **kwargs):
 #        super(MyForm, self).__init__(*args, **kwargs)
 #        self.fields['mydate'].widget = widgets.AdminDateWidget()
 #        self.fields['mytime'].widget = widgets.AdminTimeWidget()
 #        self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()




		
class NewAccount(forms.ModelForm):


	Username = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder ' : 'Username'}), label = '')
	Password = forms.CharField(widget = forms.PasswordInput(attrs = {'class ': 'form-control', 'placeholder' : 'Password'}), label = '')
	Verify_Password = forms.CharField(widget = forms.PasswordInput(attrs = {'class ': 'form-control', 'placeholder' : 'Confirm Password'}), label = '')
	# Gender = forms.ChoiceField(choices = GENDER_CHOICES, widget = forms.RadioSelect( attrs = {'display' : 'inline-block'}))
	Fname = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'First Name'}), label = '')
	Lname = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Last Name' }), label = '')
	Email = forms.EmailField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Email' }), label = '')
	Address = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Address' }), label = '')
	# Contactno = forms.CharField(widget = forms.NumberInput(attrs = {'class' :'form-control', 'placeholder' : 'Contact Number'}), label = '')


	def clean(self):
		Password = self.cleaned_data.get('Password', None)
		Verify_Password = self.cleaned_data.get('Verify_Password', None)
		if (Password == Verify_Password):
			return self.cleaned_data
		else:
			raise forms.ValidationError('Password mismatch')



	class Meta():
		model = Account
		fields = '__all__'


