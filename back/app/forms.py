from os import getenv

from django import forms

from .core.core.prompt import Prompt
from .core.core.yandex_gpt_client import YandexGPTClient
from .models import News, TestQuestion


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        content_type = cleaned_data.get('content_type')
        category = cleaned_data.get('category')
        
        # Если это статья, проверяем, что категория соответствует
        if content_type == 'article' and category != 'article':
            # Автоматически устанавливаем категорию 'article' для статей
            cleaned_data['category'] = 'article'
        
        return cleaned_data


class CreateTaskForm(forms.Form):
    selected_task = forms.CharField(widget=forms.Textarea)

    def exec(self):
        prompt = Prompt()
        selected_task = self.cleaned_data.get('selected_task')
        method = f"get_{selected_task.replace('-', '_')}_prompt"

        task_text = YandexGPTClient(
            token=getenv('OAUTH_TOKEN'),
            folder_id=getenv('FOLDER_ID')
        ).get_prompt_response_msg(
            text=getattr(prompt, method)
        )
        return {
            'task_text': task_text,
            'selected_task': selected_task
        }


class AddTaskToBaseForm(forms.Form):
    SUCCESS_MSG: str = "Задание успешно добавлено в базу данных!"
    ERROR_MSG: str = "Произошла ошибка: {error}!"

    task_text = forms.CharField(widget=forms.Textarea)
    task_answer = forms.CharField(widget=forms.Textarea)
    selected_task_answer = forms.CharField(widget=forms.Textarea)

    def mapping_tests(self, value: str) -> int:
        task_mapping = {
            'task-1-p1': 1,
            'task-2-p1': 2,
            'task-3-p1': 3,
            'task-4-p1': 4,
            'task-5-p1': 5,
            'task-6-p1': 6,
            'task-7-p1': 7,
            'task-8-p1': 8,
            'task-9-p1': 9,
            'task-10-p1': 10,
            'task-11-p1': 11,
            'task-12-p1': 12,
            'task-13-p1': 13,
            'task-14-p1': 14,
            'task-15-p1': 15,
            'task-16-p1': 16,
            'task-17-p1': 17,
            'task-18-p1': 18,
            'task-19-p1': 19,
            'task-20-p1': 20,
            'task-1-p2': 29,
            'task-2-p2': 30,
            'task-3-p2': 31,
            'task-4-p2': 32,
            'task-5-p2': 33,
        }
        return task_mapping.get(value)

    def exec(self):
        task_text = self.cleaned_data.get('task_text')
        task_answer = self.cleaned_data.get('task_answer')
        selected_task_answer = self.cleaned_data.get('selected_task_answer')
        try:
            TestQuestion.objects.create(
                test_id=0,
                order=self.mapping_tests(selected_task_answer),
                answer=task_answer,
                question_text=task_text
            )
        except Exception as e:
            msg = self.ERROR_MSG.format(error=str(e))
        else:
            msg = self.SUCCESS_MSG
        return {'info_msg': msg}
