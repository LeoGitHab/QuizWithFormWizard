from django.http import HttpRequest
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView

from quiz.forms import AnswerForm
from quiz.models import Category, Question


def category_list(request: HttpRequest):
    context = {
        'categories': Category.objects.all()
    }

    for category in context['categories']:
        ticks = [tick.id for tick in Question.objects.filter(category_id=category.pk)]
        category.possible_ticket_numbers = str(ticks)
        category.save()

    return render (request, 'start.html', context=context)


class TicketsWizard(SessionWizardView):
    form_list = []
    template_name = 'ticket.html'
    # category = Category.objects.get(id=pk)

    def get_form_list(self):
        # pk = self.request.GET['pk']
        # print('pk = ', pk)

        form_list = super().get_form_list()
        queryset = Question.objects.filter(category_id=1).first().all()
        print('queryset = ', queryset)

        for num, item in enumerate(queryset):
            form_list[num] = AnswerForm

        return form_list


    def done(self, form_list, **kwargs):
        _form_data = [form.cleaned_data for form in form_list]
        # _form_data =  [{'get_answers': ['1', '4']}, {'get_answers': ['2', '3']}]
        print('_form_data = ', _form_data)
        return render(self.request, 'no_tickets.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
