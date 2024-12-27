from django.shortcuts import render, redirect
from .forms import InputForm


def input_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            base = form.cleaned_data['base']
            size = form.cleaned_data['size']
            # nums = [int(x, base) for x in nums.split(';')]
            return redirect('result_view', base=base, size=size)
    else:
        form = InputForm()

    return render(request, "home_page.html", {'form': form})


def result_view(request, base, size):
    # b = int(base)
    # s = int(size)
    table = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            table[i][j] = i + j
    indices = list(range(size))
    return render(request, 'table.html', {'base': base, 'size': size, 'table': table, 'indices': indices})
