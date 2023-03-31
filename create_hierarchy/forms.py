from django import forms

from create_hierarchy.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeSearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )
