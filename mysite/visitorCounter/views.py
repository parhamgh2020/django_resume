from django.shortcuts import render
from .models import IPAddress, MyResume
from .forms import EmailPostForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    ip_count = IPAddress.objects.all().count()
    obj, _ = MyResume.objects.get_or_create(id=1)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} recommends you read"
            message = f" name: {cd['name']} \n email: {cd['email']} \n comment: {cd['comment']}"
            send_mail('from resume site', message, 'admin@myblog.com', ('parham.ghashghaee@gmail.com',))
            sent = True
    else:
        send_mail('you have visitor', f'visit number: {ip_count}', 'admin@myblog.com', ('parham.ghashghaee@gmail.com',))
    form = EmailPostForm()
    return render(request, 'home.html', {'ip_count': ip_count,
                                         'sent': sent,
                                         'form': form,
                                         'obj': obj
                                         })
