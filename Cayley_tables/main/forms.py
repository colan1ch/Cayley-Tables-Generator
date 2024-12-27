from django import forms


class InputForm(forms.Form):
    base = forms.IntegerField(label='Введите основание системы счисления', max_value=36, min_value=2)
    nums = forms.CharField(label='Введите множество через пробелы', max_length=100)
