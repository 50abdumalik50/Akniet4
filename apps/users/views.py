# from django.views.generic import CreateView
# from django.urls import reverse_lazy
# from django.contrib.auth import get_user_model
# from apps.users.forms import UserFrom
#
#
# from django.views.generic import UpdateView
# from django.shortcuts import redirect
#
# User = get_user_model()
#
#
# class SignUpView(CreateView):
#     model = User
#     form_class = UserFrom
#     success_url =  reverse_lazy('login')
#     template_name = 'signup.html'
#
# class UpdateView(UpdateView):
#     model = User
#     form_class = UserForm
#     template_name = 'user_update.html'
#     success_url = reverse_lazy('login')
#
#         def get_object(self, queryset=None):
#             return self.request.user
#
#         def dispatch(self, request, *args, **kwargs):
#             if not request.user.is_authenticated:
#                 return redirect('login')
#             return super().dispatch(request, *args, **kwargs)

