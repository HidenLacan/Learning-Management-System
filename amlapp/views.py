from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomUserLoginForm
from .models import CustomUser
from django.contrib.auth import login
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def aboutus(request):
    return render(request,'about.html')


class HomeView(View):
    def get(self,request):
        return render(request,'home.html')


@login_required(login_url="login/")
def dashboard(request):
    return render(request,'dashboard.html', {'user':request.user})

    
class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user  = form.save()
        login = (self.request,user)
        return super(RegisterView,self).form_valid(form)


class CustomLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
        