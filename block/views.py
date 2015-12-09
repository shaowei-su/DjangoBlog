from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Block
# Create your views here.

def block_list(request):
    blocks = Block.objects.all().order_by('-id')
    #blocks is query set
    return render_to_response('block_list.html', {'blocks':blocks})
    #{} contains parameter for rendering page