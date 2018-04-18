from django.db import models
from django.template.defaultfilters import slugify
class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    pub_date = models.DateTimeField('date published')
    #post_image = models.ImageField(upload_to="static/images")#
    post_author = models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs): #We overrided save function to create slug field with post_title field automaticaly.#
        if not self.id:
            # Newly created object, so set slug
            self.s = slugify(self.post_title)
        super(Posts, self).save(*args, **kwargs)

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