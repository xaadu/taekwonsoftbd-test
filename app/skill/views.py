from django.shortcuts import render

from .models import myskill,ContactInfo

def home(request):
    items = myskill.objects.all()
    title = "Welcome to Sarker Majid"
    description = "Hi, I'm a professional Web Developer and Website Designer. I Design and Develop top quality, user-friendly and responsive custom websites. I'm passionate to help others . I can simplify all your professional needs at one place. I'm passionate with coding and I'm fully capable of providing reliable & great quality work. Inbox me your requests & I'll reply you promptly. If you're looking for someone who cares about your project, I will communicate with you quickly and work with you until you're 100% satisfied,"

    context = {
        "title":title,
        "description": description,
        "data":items
    }

    return render(request,"index.html",context)

def about(request):
    title = "About My Skill"
    description = """Hi, I'm a professional Web Developer and Website Designer. I Design and Develop top quality, user-friendly and responsive custom websites. I'm passionate to help others . I can simplify all your professional needs at one place. I'm passionate with coding and I'm fully capable of providing reliable & great quality work. Inbox me your requests & I'll reply you promptly. If you're looking for someone who cares about your project, I will communicate with you quickly and work with you until you're 100% satisfied,
    1.HTML
    2.CSS
    3.JavaScript
    4.jQuery
    5.Bootstrap
    6.Python
    7.Php
    8.mySql
    9.WordPress
    10.Django
    """

    context = {
        "title":title,
        "description":description,
    }

    return render(request,"about.html",context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # mydata = ContactInfo(name=name,email=email,subject=subject,message=message)

        mydata = ContactInfo()
        mydata.name = name
        mydata.email = email
        mydata.subject = subject
        mydata.message = message

        mydata.save()

    return render(request,"contact.html")