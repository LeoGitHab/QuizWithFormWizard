from django import forms

from quiz.models import Question


class AnswerForm(forms.Form):

    class Meta:
        model = Question
        fields = ('get_answers')

    def __init__(self, pk, *args, **kwargs,):
        super(AnswerForm, self).__init__(pk, *args, **kwargs)
        # print('*******', kwargs['pk'])
        print('!!!!!!!', args)
        print('&&&&&&', kwargs)
        print('pk = ', pk)
        list_answers = Question.objects.filter(category_id=pk).first().get_answers()
        # print(list_answers)

        MyListTuples = [(str(c.id), c.content) for c in list_answers]
        print('MyListTuples = ', MyListTuples)

        content = forms.MultipleChoiceField(
            choices=MyListTuples,
            widget=forms.CheckboxSelectMultiple(),
        )

        self.fields['get_answers'] = content
        print(content)