
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


	




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image=models.ImageField(default ="default_foo.jpg", upload_to ="post_img")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
 
    

class comment (models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)


    class meta:
        ordering=["-created_on"]
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    



    class Video(models.Model):
      url = models.URLField()
      title = models.CharField(max_length=255)
      quality = models.CharField(max_length=255)

