from django import forms
from employee.models import Employee
class EmployeeForms(forms.ModelForm):
	class Meta:
		model=Employee
		fields="__all__"
class leaveForms(forms.ModelForm):
	class Meta:
		model=Employee
		fields="__all__"
class emptimeForms(forms.ModelForm):
	class Meta:
		model=Employee
		fields="__all__"
