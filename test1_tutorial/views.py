from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm, UserLoginForm
from django.contrib.auth.models import User

class UserFormView(View):
    form_class = UserForm
    template_name = "registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # email = form.cleaned_data['email']
            # firstname = form.cleaned_data['firstname']
            # lastname = form.cleaned_data['lastname']

            user.set_password(password)

            user.save()

            # User authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('My_Songs:index')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "login_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            # if user is None:
            #     return redirect('register')
            # else:
            if user.is_active:
                login(request, user)
                return redirect('My_Songs:index')

        return render(request, self.template_name, {'form': form})


class UserPageView(generic.TemplateView):
    template_name = "user_page.html"


# class UpdateProfileView(View):
#     form_class = ProfileForm
#     template_name = "update_profile_form.html"
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('settings:profile')
#
#         return render(request, self.template_name, {'form': form})



