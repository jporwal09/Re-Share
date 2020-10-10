from django.forms import ModelForm
from .models import Topic,Material

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ['name']

		


class MaterialForm(ModelForm):
	class Meta:
		model = Material
		fields= ['url','desc'] 
