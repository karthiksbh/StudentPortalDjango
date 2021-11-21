from django.shortcuts import render, redirect
from django.views import View
from .forms import Studentprofile, User_Register, Todo_Form
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import StudentProfile, todo_list
from django.db.models import Q

# Create your views here.


def main_page(request):
    return render(request, 'main.html')


@login_required
def home(request):
    return render(request, 'home.html')


class RegisterUserView(View):
    def get(self, request):
        form = User_Register()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = User_Register(request.POST)
        if form.is_valid():
            messages.success(request, 'You Have Registered Successfully')
            form.save()

        form = User_Register()

        return render(request, 'register.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile_updated = False
        profile_there = StudentProfile.objects.filter(user=user)
        profile_updated = StudentProfile.objects.filter(Q(user=user)).exists()
        print(profile_updated)
        if(profile_updated == False):
            return render(request, 'noprofile.html')
        else:
            return render(request, 'profile.html', {'profile_there': profile_there})


def enter_profile(request):
    return render(request, 'enterprofile.html')


@method_decorator(login_required, name='dispatch')
class StudentPro(View):
    def get(self, request):
        form = Studentprofile()
        return render(request, 'enterprofile.html', {'form': form})

    def post(self, request):
        form = Studentprofile(request.POST)
        if form.is_valid():
            user = request.user
            student_name = form.cleaned_data['student_name']
            class_student = form.cleaned_data['class_student']
            student_email = form.cleaned_data['student_email']
            mobile_number = form.cleaned_data['mobile_number']
            school = form.cleaned_data['school']
            city = form.cleaned_data['city']
            studentprofile = StudentProfile(
                user=user, student_name=student_name, class_student=class_student, student_email=student_email, mobile_number=mobile_number, school=school, city=city)

            studentprofile.save()

            profile_there = StudentProfile.objects.filter(user=user)

        return render(request, 'profile.html', {'profile_there': profile_there})


def edit_profile(request, profile_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            todo = StudentProfile.objects.get(pk=profile_id, user=user)
            form = Studentprofile(request.POST or None, instance=todo)

            if form.is_valid():
                form.save()
                messages.info(request, ('Profile has been Edited!'))

            form = Studentprofile()

            return render(request, 'editprofile.html', {'form': form})

        else:
            user = request.user
            todo = StudentProfile.objects.get(pk=profile_id, user=user)
            form = Studentprofile(request.POST or None, instance=todo)

            return render(request, 'editprofile.html', {'form': form})


class AddTodo(View):
    def get(self, request):
        user = request.user
        form = Todo_Form()
        alllist = todo_list.objects.filter(user=user)

        return render(request, 'todo.html', {'form': form, 'alllist': alllist})

    def post(self, request):
        form = Todo_Form(request.POST)

        if form.is_valid():
            user = request.user
            desc = form.cleaned_data['desc']
            todoone = todo_list(
                user=user, desc=desc)

            todoone.save()

        messages.success(request, 'Todo Has Been Added Successfully')

        form = Todo_Form()

        alllist = todo_list.objects.filter(user=user)

        return render(request, 'todo.html', {'form': form, 'alllist': alllist})


def delete(request, todo_id):
    if request.user.is_authenticated:
        user = request.user
        todo = todo_list.objects.get(pk=todo_id, user=user)
        todo.delete()
        messages.success(request, ('Todo Has Been Deleted!'))
    return redirect('todo')


def done_todo(request, todo_id):
    if request.user.is_authenticated:
        user = request.user
        todo = todo_list.objects.get(pk=todo_id, user=user)
        todo.done = True
        todo.save()
    return redirect('todo')


def notdone_todo(request, todo_id):
    if request.user.is_authenticated:
        user = request.user
        todo = todo_list.objects.get(pk=todo_id, user=user)
        todo.done = False
        todo.save()
    return redirect('todo')


def edit(request, todo_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            todo = todo_list.objects.get(pk=todo_id, user=user)
            form = Todo_Form(request.POST or None, instance=todo)

            if form.is_valid():
                form.save()
                messages.success(request, ('Todo Has Been Edited!'))

            return redirect('todo')

        else:
            user = request.user
            todo = todo_list.objects.get(pk=todo_id, user=user)
            form = Todo_Form(request.POST or None, instance=todo)

            alllist = todo_list.objects.filter(user=user)
            return render(request, 'todo.html', {'form': form, 'alllist': alllist})


def change_password(request):
    return render(request, 'changepassword.html')


def class9(request):
    return render(request, 'class9.html')


def class8(request):
    return render(request, 'class8.html')


def class10(request):
    return render(request, 'class10.html')


def class1112(request):
    return render(request, 'class1112.html')


def videos(request):
    return render(request, 'videos.html')


def vid9(request):
    return render(request, 'vid9.html')


def vid8(request):
    return render(request, 'vid8.html')


def vid10(request):
    return render(request, 'vid10.html')


def vid1112(request):
    return render(request, 'vid1112.html')


def pdfs(request):
    return render(request, 'pdfs.html')


def passsuccess(request):
    return render(request, 'paschangecon.html')
