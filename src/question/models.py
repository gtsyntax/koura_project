from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class QuestionManager(models.Manager):
	def get_queryset(self):
		return super(QuestionManager, self).get_queryset()\
											.filter(status='published')

class Question(models.Model):
	STATUS_CHOICES = (
		('draft', 'DRAFT'),
		('published', 'PUBLISHED'),
	)
	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, related_name="questions")
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
								choices=STATUS_CHOICES,
								default='draft')
	objects = models.Manager()
	active = QuestionManager() 

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




