from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .forms import RegisterForm,LoginForm
from .models import Profile,Club
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from extrasheet.utils import create_notify
from .forms import ForumForm,InsightForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index (request):
    user = request.user
    current_user = request.user
    a = current_user.id
    d = []
    pr = Profile.objects.all()
    for no in pr :
        d.append(no.name_id)
        print (d)
        
    if user.is_authenticated:
        if  a in d:
            return redirect ('clubl')
        else:
            return redirect ('profile')
    
    else:    
        
        return render (request,'index.html')
        
#login
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
 
 #signup  
class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')
    
#Profile
 
class ProfilesCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        a = current_user.id
        d = []
        template = loader.get_template('extrasheet/profile.html')
        context = {'a':a}
        pr = Profile.objects.all()
        for no in pr :
            d.append(no.name_id)
        
        if not a in d:
            
            return HttpResponse(template.render(context, request))
        else:
            return redirect('clubl')
    model = Profile
    
        
    success_url = reverse_lazy('clubl')
    template_name = 'extrasheet/profile.html'
    
    fields = ['profile_image','school_name','gender','major_courses','minor_courses','personal_interest','skills_you_have','skills_you_like_to_have','hobbies','spoken_languages','heros_or_rolemodels']
    login_url = 'login' 
    def form_valid(self, form): # new
        form.instance.name = self.request.user
        return super().form_valid(form)
        
#club form

class ClubCreateView(LoginRequiredMixin,CreateView):
    model = Club
    success_url = reverse_lazy('Home/')
    template_name = 'club.html'
    fields = [
        'club_image',
        'club_name',
        'niche',
        'about_club'
        ]
    login_url = 'login' 
    def form_valid(self, form): # new
        form.instance.name = self.request.user
        return super().form_valid(form)
        
        
#filter club based on personal interest
@login_required(login_url='login')    
def club_view (request):
    current_user = request.user
    a = current_user.id
    u = Profile.objects.filter(name=request.user)
    for li in u:
        a = (li.personal_interest)
    print (a)
    print (u)
    b = a
    print (b)
    c = Club.objects.filter(niche=b)
    return render (request,'join_club.html',{'c':c})

#join 
@login_required(login_url='login')    
def join_club (request):
    club = get_object_or_404(Club,id=request.POST.get('club_id'))
    club.join.add(request.user)
    create_notify(request.user, 'join',club)
    return redirect ('clubl')

#club joined 
@login_required(login_url='login')    
def club_join (request):
    cj = request.user.join.all()
    #for club in cj:
        #print (club.club_name)
       #a=club.club_name
    #b=a
    #create_notify('you are in',cj )
    return render (request,'club_joined.html',{'cj':cj})
    
#club forum    
@login_required(login_url='login')    
def club_forum (request,pi):
    #current_user = request.user
    club  = get_object_or_404(Club,pk=pi)
    comm = club.club_comment.all()
    foru = None
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            foru = form.save(commit=False)
            foru.club = club
            foru.save()
    
    else:
	    form = ForumForm()
    return render(request,'forum.html',{'comm':comm,'form':form,'club':club})
    
#clubs    
@login_required(login_url='login')    
def clubs (request,pi):
    club  = get_object_or_404(Club,club_name=pi)
    return render (request,'cj.html',{'club':club})

#club insight    
@login_required(login_url='login')       
def club_insight (request,pi) :
    current_user = request.user
    a = current_user.id
    club  = get_object_or_404(Club,pk=pi)
    comm = club.club_update.all()
    join = club.join.all()
    j = []
    for cb in join:
        j.append(cb.id)
        
    print (j)
    if not a in j:
        return redirect ('clubl')
            
    insi = None
    if request.method == 'POST':
        form = InsightForm(request.POST,request.FILES)
        if form.is_valid():
            insi = form.save(commit=False)
            insi.club = club
            insi.save()
    else:
	    form = InsightForm()
    return render(request,'insight.html',{'comm':comm,'form':form,'club':club,'a':a,'join':join,'j':j})
    
    
#from django.http import HttpResponse
#from django.views import View

#class MyView(View):

    #def get(self, request, *args, **kwargs):
        #return HttpResponse('Hello, World!'   
    
    
    
    
    
    
    
    
    
    