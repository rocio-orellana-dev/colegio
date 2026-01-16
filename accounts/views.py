from django.contrib.auth.views import LoginView, LogoutView

class MyLoginView(LoginView):
    template_name = 'accounts/login.html' # Aquí le indicamos el archivo que acabas de crear

class MyLogoutView(LogoutView):
    next_page = 'login'