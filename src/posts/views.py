from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
import json
    
    
def home(request):
    context = {'form': PostForm()}     
    return render(request, 'posts/index.html', context)
    
    
    
def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}
        
        post = Post(text=post_text, author=request.user)
        post.save()
        
        response_data['text'] = post.text
        #response_data['author'] = str(post.author.username)
        response_data['author'] = post.author.username
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'nothing here': 'Error'}), content_type='application/json')   
    
    
    
    
    
    
# def home(request):
    # if request.method == 'POST':
        # post_text = request.POST['post_text']
        # form = PostForm(request.POST)
        # if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()
    # else:
        # form = PostForm()      
    # return render(request, 'posts/index.html', context)

    
    
# def create_post(request):
    # if request.method == 'POST':
        # post_text = request.POST.get('the_post')
        # response_data = {}

        # post = Post(text=post_text, author=request.user)
        # post.save()

        # response_data['result'] = 'Create post successful!'
        # response_data['postpk'] = post.pk
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username

        # return HttpResponse(
            # json.dumps(response_data),
            # content_type="application/json"
         # )
    # else:
        # return HttpResponse(
            # json.dumps({"nothing to see": "this isn't happening"}),
            # content_type="application/json"
         # )