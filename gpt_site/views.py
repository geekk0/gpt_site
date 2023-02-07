from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from bot import chatbot


def main(request):

    return render(request, "base.html")


def get_gpt_response(request):
    # print(request.POST)
    request_dict = request.POST.dict()

    request_text = request_dict['request_text']

    response_text = chatbot.get_gpt_resp(request_text)

    print(response_text)

    context = {'response_text': response_text}

    return render(request, "base.html", context)