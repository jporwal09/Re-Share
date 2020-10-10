from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .forms import TopicForm , MaterialForm
from .models import Topic , Material
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import requests
# Create your views here.

@login_required
def userhome(request):
    context = {
        'topic': Topic.objects.all().annotate(Material_count=Count('material')).order_by('-Material_count')
    }
    if 'qname' in request.GET:
    	query = request.GET['qname']
    	print(query)
    	if query != "":
    		topicop = Topic.objects.filter(name__icontains =query).annotate(Material_count=Count('material')).order_by('-Material_count')
    		context['topicop'] = topicop
    return render(request, 'resource/userhome.html', context)

@login_required
def detail(request,topic_id):
	topic = get_object_or_404(Topic,pk=topic_id)
	return render(request,'resource/detail.html',{'topic': topic})


@login_required
def newTopic(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = TopicForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data.get('name')
				name.lower()
				if Topic.objects.filter(name=name).exists():
					messages.error(request, f'Topic Already exist')
					return HttpResponseRedirect(reverse('addtopic'))
				else:	
					user = request.user
					print(name)
					topic = Topic(name=name , user=user)
					topic.save()
					return HttpResponseRedirect(reverse('userhome'))
		else:
			form = TopicForm()
			return render(request, 'resource/addtopic.html',{'form': form})	
	else:
		return HttpResponseRedirect(reverse('login'))		


def search(request):
	context={}
	if 'qname' in request.GET:
		query = request.GET['qname']
		context={
	     'topic' : Topic.objects.filter(name__icontains =query)
		}
	return render(request, 'resource/search.html', context)


@login_required
def neawMaterial(request, topic_id):
    if request.user.is_authenticated:
        form = MaterialForm()
        context = {'topic_id': topic_id, 'form': form}
        return render(request, 'resource/addMaterial.html', context)

    return HttpResponseRedirect(reverse('home'))
	

def newMaterial(request, topic_id):
    
    if request.user.is_authenticated:
        topic = get_object_or_404(Topic, pk=topic_id)
        if request.method == "POST":
        	form = MaterialForm(request.POST)
        	if form.is_valid():
        		url= form.cleaned_data.get('url')
        		desc = form.cleaned_data.get('desc')
        		res = Material(url = url,topic = topic,user = request.user,desc=desc)
        		res.save()
        		return HttpResponseRedirect(reverse('detail', args=(topic.id,)))           
        else:
        	form = MaterialForm()
        	return render(request, 'resource/addMaterial.html',{'form': form})
            
    else:
        return HttpResponseRedirect(reverse('home'))
        
def likeview(request,pk):
    print(pk)
    post = get_object_or_404(Material , pk=pk)
    print(post.url)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args= [str(post.topic.id)]))

           
def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'resource/github.html', {'user': user})


def codef(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = ' https://codeforces.com/api/user.info?handles=%s' % username
        response = requests.get(url)
        print(response.json())
        user = response.json()
    return render(request, 'resource/cf.html', {'user': user})  
