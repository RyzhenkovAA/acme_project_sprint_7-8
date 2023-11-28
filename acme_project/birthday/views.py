from django.shortcuts import get_object_or_404, render, redirect

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy
#from django.core.paginator import Paginator


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm

#def birthday(request, pk=None):
#    if pk is not None:
#        instance = get_object_or_404(Birthday, pk=pk)
#    else:
#        instance = None
#    form = BirthdayForm(
#        request.POST or None,
#        files=request.FILES or None,
#        instance=instance
#    )
#    context = {'form': form}
#    if form.is_valid():
#        form.save()
#        birthday_countdown = calculate_birthday_countdown(form.cleaned_data['birthday'])
#        context.update({'birthday_countdown': birthday_countdown})
#    return render(request, 'birthday/birthday.html', context=context)


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10 

#def birthday_list(request):
#    birthdays = Birthday.objects.order_by('id')
#    paginator = Paginator(birthdays, 10)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    context = {'page_obj': page_obj}
#    return render(request, 'birthday/birthday_list.html', context)


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


#def delete_birthday(request, pk):
#    instance = get_object_or_404(Birthday, pk=pk)
#    form = BirthdayForm(instance=instance)
#    context = {'form': form}
#    if request.method == 'POST':
#        instance.delete()
#        return redirect('birthday:list')
#    return render(request, 'birthday/birthday.html', context)


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(self.object.birthday)
        return context