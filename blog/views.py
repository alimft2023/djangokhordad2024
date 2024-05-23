from django.shortcuts import render,redirect
from .models import Post
from .forms import PostCreateForm,PostUpdateForm
# Create your views here.
def post(request):
    p=Post.objects.all()
    return render(request,'blog/post.html',{'p':p})
def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def details(request,id):
    p=Post.objects.get(pk=id)
    return render(request,'details.html',{'p':p})

def delete(request,id):
    Post.objects.get(pk=id).delete()
    return redirect('home')

def update(request,id):
    p=Post.objects.get(pk=id)
    if request.method=="POST":
        form=PostUpdateForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            
        return redirect('post')
    elif request.method=="GET":
        form=PostUpdateForm(instance=p)
        return render(request,'update.html',{'form':form})
    
def create(request):
    if request.method=="POST":
        form=PostCreateForm(request.POST)
        if form.is_valid():
            t=form.cleaned_data['title']
            b=form.cleaned_data['body']
            c=form.cleaned_data['created']
            p=Post.objects.create(title=t,body=b,created=c)
            p.save()
            return redirect('post')
    elif request.method=="GET":
        form=PostCreateForm()
        return render(request,'create.html',{'form':form})

