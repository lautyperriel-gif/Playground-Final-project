from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox_view(request):
    inbox = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'messenger/inbox.html', {'messages': inbox})

@login_required
def send_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messenger:inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/message_form.html', {'form': form})
