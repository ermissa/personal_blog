from django.db import models

class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    pub_date = models.DateTimeField('date published')
    post_image = models.ImageField(upload_to="static/images")
    post_author = models.CharField(max_length=100)

    def __str__(self):
        return self.post_body

class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment_text = models.TextField()
    def __str__(self):
        return self.comment_text


class Categories(models.Model):
    CategoryName = models.CharField(max_length=100)
class CategoryPost():
    postID = models.ForeignKey(Posts,on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Categories,on_delete=models.CASCADE)