from random import randint
from django.shortcuts import render, redirect
from .forms import InputForm


def associate_check(table):
    n = len(table)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                ab = table[a][b]
                ab_c = table[ab][c]
                bc = table[b][c]
                a_bc = table[a][bc]
                if ab_c != a_bc:
                    return False
    return True


def neutral_element_search(table):
    n = len(table)
    for i in range(n):
        if table[i] == list(range(n)) and all(table[x][i] == x for x in range(n)):
            return i  # возвращаем номер нейтрального элемента
    return -1  # нет нейтрального элемента


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
    tables = []
    reports = []
    table = [
        [1, 0, 1],
        [0, 1, 2],
        [2, 2, 1]
    ]
    report = {
        'associate': associate_check(table),
        'neutral': neutral_element_search(table)
    }
    tables.append(table)
    reports.append(report)
    # table2 = [[0] * size for _ in range(size)]
    # for i in range(size):
    #     for j in range(size):
    #         table2[i][j] = randint(0, size - 1)
    table2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 2]
    ]
    report2 = {
        'associate': associate_check(table2),
        'neutral': neutral_element_search(table2)
    }
    tables.append(table2)
    reports.append(report2)
    data = [
        (table, report),
        (table2, report2)
    ]
    context = {
        'size': size,
        'data': data
    }
    return render(request, 'table.html', context)
