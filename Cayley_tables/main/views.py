from django.shortcuts import render, redirect
from .forms import InputForm

# def index(request):
#     return render(request, 'home_page.html')


def input_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            base = form.cleaned_data['base']
            nums = form.cleaned_data['nums']
            # nums = [int(x, base) for x in nums.split()]
            return redirect('result_view', base=base, nums=nums)
    else:
        form = InputForm()

    return render(request, "home_page.html", {'form': form})


def result_view(request, base, nums):
    return render(request, 'table.html', {'base': base, 'nums': nums})
