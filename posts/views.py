from django.shortcuts import render, redirect
from .forms import PostForm
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request, 'post.html', {'form': post_form})        
