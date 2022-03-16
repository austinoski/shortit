from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import ShortItForm
from .customs import generate_unique_key


class HomeView(View):
    form = ShortItForm
    template_name = "app/index.html"

    def get(self, request, format=None):
        context_data = self.get_context_data(request)
        form = self.form()
        context_data["form"] = form
        return render(request, self.template_name, context_data)
    
    def post(self, request, format=None):
        form = self.form(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                self.save_to_session(request, form.cleaned_data)
            context_data = self.get_context_data(request)
            return render(request, self.template_name, context_data)

        # if form not valid make a get request
        form = self.form()
        context_data = self.get_context_data(request)
        return redirect(reverse_lazy("homepage"), args=[context_data])
    
    def get_context_data(self, request):
        context_data = {}
        context_data["shortit"] = dict(request.session).values()
        return context_data
    
    def save_to_session(self, request, cleaned_data):
        cleaned_data["key"] = generate_unique_key(cleaned_data["url"])
        # if custom_text is provided use custom_text as session key
        session_key = cleaned_data["key"]
        if len(cleaned_data["custom_text"]) > 0:
            session_key = cleaned_data["custom_text"]
        request.session[session_key] = cleaned_data
