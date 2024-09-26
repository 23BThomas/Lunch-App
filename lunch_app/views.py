from django.shortcuts import render
from .models import Lunch, Employee

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        balance = request.POST['balance']
        meals_taken = request.POST['meals_taken']
        meals_remaining = request.POST['meals_remaining']
        Employee.objects.create(name=name, amount=amount, balance=balance, meals_taken=meals_taken, meals_remaining=meals_remaining)
        return redirect('employee_list')
    return render(request, 'add_employee.html')

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.amount = request.POST['amount']
        employee.balance = request.POST['balance']
        employee.meals_taken = request.POST['meals_taken']
        employee.meals_remaining = request.POST['meals_remaining']
        employee.save()
        return redirect('employee_list')
    return render(request, 'edit_employee.html', {'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def redeem_lunch(request):
    balance = 100  # Replace with the actual balance value
    min_balance_required = 7
    balance_meals = balance // min_balance_required

    redeem = "No redeem available"
    if balance_meals > 0:
        redeem = "Free lunch!"

    lunch = Lunch.objects.create(balance=balance, redeemed=redeem)

    return render(request, 'redeem.html', {'balance_meals': balance_meals, 'redeem': redeem})
