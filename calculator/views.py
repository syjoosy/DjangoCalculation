from django.shortcuts import render, redirect
from .forms import UserForm, RecieveResult
from .service import Calculator
from django.contrib import messages
import re


def to_home(request):
    return redirect('home')

def home(request):
    values = []
    vars = []
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()

            value = request.POST.get("value")
            expression = request.POST.get("expression")

            new_value = value.split(',')
            for val in new_value:
                val = val.strip()
                values.append(val)
            # print(values)
            value_of_expression = re.split('[*,+,-]',expression)
            for val in value_of_expression:
                val = val.strip()
                vars.append(val)
            new_vars = []
            for i in vars:
                if i not in new_vars:
                    new_vars.append(i)
            # print(new_vars)
            if len(new_vars) == len(values):
                expression_and_value = dict(zip(new_vars, values))
                # print(expression_and_value)
            else:
                userform = UserForm()
                messages.error(request, f"Несостыковка количества переменных и их значений")
                return render(request, 'calculator/home.html', {'form': userform})
            expression_and_values = {'expression': expression, 'variables': expression_and_value}
            # print(expression.objects.all()[0].id)
            calculator = Calculator()
            service_result = calculator.get_extension(expression_and_values)

            # messages.success(request, f"Ваша формула {expression} рассчитана! ID: {service_result['expression_id']}")
            messages.success(request, f"Ваша формула {expression} рассчитана! {service_result}")
            return redirect('id')
        else:
            userform = UserForm()

            return render(request, 'calculator/home.html', {'form': userform}, {'error': 1})
            # return HttpResponse("<h2>Hello, {0}</h2>".format(expression))
    else:
        userform = UserForm()
        return render(request, 'calculator/home.html', {'form': userform})

def ResultRecieve(request):
    if request.method == "POST":
        userrform = RecieveResult(request.POST)
        if userrform.is_valid():
            expression_id = request.POST.get("enterid")
            expression_id = {'expression_id': expression_id}
            calculator = Calculator()
            expression_result = calculator.get_result(expression_id)
            messages.success(request, f"Результат: {expression_result}")
            return redirect('id')
        else:
            userrform = RecieveResult()

            return render(request, 'calculator/home.html', {'form': userrform}, {'error': 1})
    else:
        userrform = RecieveResult()
        return render(request, 'calculator/home.html', {'form': userrform})
