from django.shortcuts import render
from django.shortcuts import render_to_response
from block.models import Block
from models import Article
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render_to_response("article_list.html",
                              {"articles": articles, "b": block},
                              context_instance=RequestContext(request))

@login_required
def create_article(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == 'GET':
        return render_to_response("article_create.html",
                                  {"b": block},
                                  context_instance=RequestContext(request))
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, 'Title and content cannot be empty')
            return render_to_response("article_create.html",
                                      {"b": block, "title": title, "content": content},
                                      context_instance=RequestContext(request))
        new_article = Article(block=block, owner=request.user, title=title, content=content)
        new_article.save()
        messages.add_message(request, messages.INFO, "Publish succeed!")
        return redirect(reverse("article_list", args=[block.id]))


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    return render_to_response("article_detail.html",
                              {"article": article},
                              context_instance=RequestContext(request))
