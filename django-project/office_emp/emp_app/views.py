from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee,Role,Department
from django.http import HttpResponse
from .forms import FilterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html',{})


@login_required(login_url='user_login')
def all_emp(request):
    emps = Employee.objects.all()
    return render(request, 'view_all_emp.html', {'emps': emps})


@login_required(login_url='user_login')
def add_emp(request):
    if request.method == 'POST':
        # Retrieve data from the submitted form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department_id = request.POST.get('dep')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role_id = request.POST.get('role')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        # Create and save the new employee object
        try:
            department = Department.objects.get(id=department_id)
            role = Role.objects.get(id=role_id)

            employee = Employee.objects.create(
                First_name=first_name,
                Last_name=last_name,
                dep=department,
                salary=salary,
                bonus=bonus,
                role=role,
                phone=phone,
                hire_date=hire_date
            )

            # Optionally, you can redirect to the employee detail page or another page
            return redirect('all_emp')

        except Department.DoesNotExist:
            return HttpResponse("Error: Department does not exist.")
        except Role.DoesNotExist:
            return HttpResponse("Error: Role does not exist.")

    else:
        # If the request method is not POST, render the add_emp template
        departments = Department.objects.all()
        roles = Role.objects.all()

        context = {
            'departments': departments,
            'roles': roles,
        }

        return render(request, 'add_emp.html', context)

@login_required(login_url='user_login')
def remove_emp(request):
    # If the form is submitted with POST, perform the removal process
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()
        return redirect('all_emp')

    # If the request method is GET, handle rendering and provide search options
    search_query = request.GET.get('search', '')
    employees = Employee.objects.filter(First_name__icontains=search_query) | Employee.objects.filter(Last_name__icontains=search_query)

    context = {'employees': employees, 'search_query': search_query}
    return render(request, 'remove_emp.html', context)

@login_required(login_url='user_login')
def filter_emp(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            selected_department = form.cleaned_data.get('department')
            
            # Filter employees based on the selected department
            if selected_department:
                employees = Employee.objects.filter(dep__name=selected_department)
            else:
                employees = Employee.objects.all()

            context = {'employees': employees, 'departments': departments, 'selected_department': selected_department, 'form': form}
            return render(request, 'filter_emp.html', context)
    else:
        form = FilterForm()

    context = {'departments': departments, 'form': form}
    return render(request, 'filter_emp.html', context)


def sign_up(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # Check if password and confirm password match
        if password != confirmpassword:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        # If both validations pass, create the user
        my_user = User.objects.create_user(username=uname, email=email, password=password)
        my_user.save()

        # Redirect to the login page after successful signup
        return redirect('user_login')

    # GET request or if there's an error, render the signup page again
    return render(request, 'signup.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('all_emp')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect.'})
        
    return render(request,'login.html',{})

def logout_page(request):
    logout(request)
    return redirect(user_login)