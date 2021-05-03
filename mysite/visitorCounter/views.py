from django.shortcuts import render
from .models import IPAddress
from .forms import EmailPostForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    ip_count = IPAddress.objects.all().count()
    ip_count += 50
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} recommends you read"
            message = cd['comment']
            send_mail(subject, message, 'admin@myblog.com', ('parham.ghashghaee@gmail.com',))
            sent = True
    form = EmailPostForm()
    return render(request, 'home.html', {'ip_count': ip_count,
                                         'sent': sent,
                                         'form': form
                                         })
