from django import forms


class InputForm(forms.Form):
    size = forms.IntegerField(label='Введите порядок группоида', min_value=2, max_value=36)
