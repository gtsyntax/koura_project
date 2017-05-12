from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=300)
	image = models.ImageField(upload_to='post_images/', null=True, blank=True,
		height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=250)
	width_field = models.IntegerField(default=100)
	slug = models.SlugField(max_length=300, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, related_name="questions")
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('question:detail', kwargs={"slug":self.slug})



@receiver(pre_save, sender=Question)
def pre_save_question_receiver(sender, instance, *args, **kwargs):
	slug = slugify(instance.title)
	instance.slug = slug


class Answer(models.Model):
	question = models.ForeignKey(Question, related_name="answers")
	user = models.ForeignKey(User, related_name="answers")
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return 'Answer by {} on {}'.format(self.user, self.question)




