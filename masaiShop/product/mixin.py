from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login')
                            )
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
    