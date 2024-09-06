from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from mediflow.apps.users.forms.login_form import CustomLoginForm


class MyLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))



class MyLogoutView(LogoutView):
    next_page = reverse_lazy("login")