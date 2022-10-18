from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ResumeModel, Advantage, Skill, Service, Project, FeedBack
from apps.blog.models import Article
from apps.contact.forms import ContactForm
from apps.contact.models import ContactModel


# Create your views here.

def home(request):
    cv = ResumeModel.objects.all().last()
    object_advantages = Advantage.objects.all()
    object_skills = Skill.objects.all()
    object_service = Service.objects.all()
    object_projects = Project.objects.all()
    object_feedbacks = FeedBack.objects.all()
    blog_list = Article.objects.all()

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'{obj.subject} xabaringiz muvofaqyatli jo\'natildi')
            return redirect('/#contact-sections')
    context = {'cv': cv, 'goals': object_advantages, 'obj': object_skills,
               'service': object_service, 'project': object_projects,
               "object_feedbacks": object_feedbacks, 'post': blog_list, 'form': form,
               }
    return render(request, 'index.html', context)
