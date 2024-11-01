from django.http import HttpResponse
from bboard.models import Bb

def index(request):
    s = 'Обьявления\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s+= bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, charset='utf-8')