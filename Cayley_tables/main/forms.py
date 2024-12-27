from django import forms


class InputForm(forms.Form):
    base = forms.IntegerField(label='Введите основание системы счисления', min_value=2, max_value=36)
    size = forms.IntegerField(label='Введите размер матрицы', min_value=2, max_value=100)
