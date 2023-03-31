from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from bot import chatbot
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        context = {'form': form}

        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

            return HttpResponseRedirect('/')

        return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    request.user.set_unusable_password()
    logout(request)

    return HttpResponseRedirect("/")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def main(request):

    return render(request, "request_page.html")


def get_gpt_response(request):
    request_dict = request.POST.dict()

    request_text = request_dict['request_text']

    response_text = chatbot.get_gpt_resp(request_text)

    context = {'response_text': response_text, "request_text": request_text}

    return render(request, "request_page.html", context)