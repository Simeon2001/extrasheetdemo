from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

# Create your models here.
class User (AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(2017-12-2)
    mobile_number = models.IntegerField(default=0)
  
#profile
class Profile (models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
        )
        
    INTEREST = (
        ('Science','Science'),
        ('Technology','Technology'),
        ('Programming','Programming'),
        ('Entertainment','Entertainment'),
        ('Body care','Body care'),
        ('Fashion','Fashion'),
        ('Gaming','Gaming'),
        ('Memes','Memes'),
        ('Gadget','Gadget'),
        ('Computer','Computer'),
        ('Music','Music'),
        ('Design','Design'),
        ('Business','Business'),
        ('Collaboration','Collaboration'),
        ('Health','Health'),
        ('Interior_design ','Interior_design '),
        ('Sport','Sport'),
        ('Food_and_drinks','Food_and_drinks'),
        ('Nature','Nature'),
        ('Photography','Photography'),
        ('Celebrities','Celebrities'),
        ('Movies','Movies'),
        ('Education','Education'),
        ('Innovation','Innovation'),
        ('Drawing','Drawing'),
        ('Animals','Animals'),
        
        )
    profile_image = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    name = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extrasheet_name')
    school_name = models.CharField(max_length=30)
    
    gender = models.CharField(max_length=10,choices=GENDER,default='Others')
    major_courses = models.CharField(max_length=20)
    minor_courses = models.CharField(max_length=20)
    personal_interest= models.CharField(max_length=50,choices=INTEREST)
    skills_you_have = models.CharField(max_length=40)
    skills_you_like_to_have = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=30)
    spoken_languages = models.CharField(max_length=50 ,default="English Language")
    heros_or_rolemodels = models.CharField(max_length=30)
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    
    def get_absolute_url(self):
        return reverse('Home/')
    
    def __str__(self):
        return self.name.username
        
#club
class Club (models.Model):
    club_image = models.ImageField(upload_to='club_image/',
    default='images/def.jpg',
    blank=True,
    null=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='extrasheet_club')
    club_name = models.CharField(max_length=40)
    niche = models.CharField(max_length=18)
    about_club = models.TextField(max_length=58)
    join = models.ManyToManyField(User,related_name='join',blank=True)
    def __str__(self):
        return self.club_name

#club_insight
class Club_in (models.Model):
    club = models.ForeignKey(Club, null=True,on_delete=models.CASCADE,related_name='club_update')
    text = models.TextField(max_length=20000)
    
    upload_file = models.ImageField(upload_to='files/',blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__ (self):
        return self.text
        
#club_forum
class Club_fo (models.Model):
    club = models.ForeignKey(Club, null=True,on_delete=models.CASCADE,related_name='club_comment')
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='forum_name',default=1)
    text = models.TextField(max_length=1000)
    
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    def get_absolute_url(self):
        return reverse('Home/')
    
    def __str__(self):
        return self.text
        
#club reply        
class Club_re (models.Model):
    club = models.ForeignKey(Club_fo, null=True,on_delete=models.CASCADE,related_name='club_reply')
    text = models.TextField(max_length=1000)
    
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.text
        
class Notify(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
 related_name='notify',
 db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj',on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True)
    
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,
 db_index=True)