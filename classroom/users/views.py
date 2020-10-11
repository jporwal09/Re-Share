from django.shortcuts import render , redirect ,get_object_or_404
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from resource.models import Material


# Create your views here.

def home(request):
	return render(request, 'users/home.html')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if(form.is_valid()):
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})			

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def diffprofile(request,user_id):
    id = request.user.id
    print(id)
    if id==user_id:
       return redirect('profile')
    else:
        ogi = user_id
        if user_id != 1:
            user_id=user_id-11
        pro = get_object_or_404(Profile,pk=user_id)
        user = get_object_or_404(User, pk = ogi)
        op = Material.objects.filter(user= user).order_by('-created')
        
        return render(request, 'users/newpp.html',{'used':pro , 'Material':op})
        

    

    






"""else:
        if user_id != 1:
        user_id = user_id-11
        pro = get_object_or_404(Profile,pk=user_id)
        print(pro.user.username)
        return render(request, 'users/newpp.html',{'used':pro})"""    