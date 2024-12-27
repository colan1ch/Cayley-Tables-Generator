from django.shortcuts import render, redirect
from .forms import InputForm


def input_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            return redirect('result_view', size=size)
    else:
        form = InputForm()

    return render(request, "home_page.html", {'form': form})


def result_view(request, size):
    table = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            table[i][j] = i + j + 5
    indices = list(range(size))
    return render(request, 'table.html', {'size': size, 'table': table, 'indices': indices})
