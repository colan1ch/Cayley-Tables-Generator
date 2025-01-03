from random import randint
from django.shortcuts import render, redirect
from .forms import InputForm
import json


def generate_all_combinations(input_list):
    n = int(len(input_list)**0.5)
    result = []

    def backtrack(current_list, index):
        if index == len(input_list):
            result.append(current_list[:])
            return

        if input_list[index] == -1:
            for i in range(n):
                current_list[index] = i
                backtrack(current_list, index + 1)
        else:
            current_list[index] = input_list[index]
            backtrack(current_list, index + 1)

    backtrack([-1] * len(input_list), 0)
    return result


def list_to_table(lst):
    size = int(len(lst)**0.5)
    table = [[0] * size for _ in range(size)]
    for i in range(size**2):
        table[i // size][i % size] = lst[i]
    return table


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
            table_data = json.loads(request.POST.get('table_data', '[]'))
            return redirect('result_view', size=size, table_data=json.dumps(table_data))
    else:
        form = InputForm()
    return render(request, "home_page.html", {'form': form})


def result_view(request, size, table_data):
    table_data = json.loads(table_data)
    unknown_nums_count = table_data.count(-1)
    tables_count = size ** unknown_nums_count
    print(table_data)
    if tables_count < 10:
        tables_list = generate_all_combinations(table_data)
        data = []
        for lst in tables_list:
            table = list_to_table(lst)
            data.append((table, {'associate': associate_check(table), 'neutral': neutral_element_search(table)}))
    context = {
        'size': size,
        'data': data
    }
    return render(request, 'table.html', context)
