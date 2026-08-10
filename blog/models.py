from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField()
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag, related_name="posts")


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    text = models.TextField(max_length=500)
    date = models.DateField()