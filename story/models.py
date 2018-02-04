from django.db import models


class Story(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Page(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    reason = models.CharField(max_length=140, null=True,blank=True)


    def __str__(self):
        return self.title

class Option(models.Model):
    choice = models.CharField(max_length=150)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='current_page')
    nextpage = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='next_page')


    def __str__(self):
        return self.choice

