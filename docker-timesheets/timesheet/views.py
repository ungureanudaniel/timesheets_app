from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from .forms import TimesheetForm
from .models import Timesheet, Activity
from django.db.models import Q
import calendar
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# =============new timesheets view======
# @login_required
# def create_timesheet(request):

#     return render(request, template, context)


# =============list of timesheets per month view======
@login_required
def timesheet_list(request):
    # get current year and month
    current_month = timezone.now().month
    # current_year = timezone.now().year
    # Base queryset
    timesheets = Timesheet.objects.all()
    # Filter by search query
    query = request.GET.get('q', '')
    if query:
        timesheets = timesheets.filter(
            Q(activity__name__icontains=query) | Q(description__icontains=query) | Q(fundssource__name__icontains=query))

    # Filter by month
    month = request.GET.get('month', '')
    if month:
        try:
            month_date = datetime.strptime(month, "%Y-%m")
            timesheets = timesheets.filter(date__year=month_date.year, date__month=month_date.month)
        except ValueError:
            pass  # Invalid month format, ignore the filter

    # Get distinct months for the filter dropdown
    months = [(i, calendar.month_name[i]) for i in range(1, 13)]
    # Get the month and year from GET parameters if available
    try:
        month = int(request.GET.get('month', current_month))
        # year = int(request.GET.get('year', current_year))
    except Exception as e:
        messages.warning(request, e)

    template = 'timesheet/timesheets_list.html'
    # timesheets = Timesheet.objects.filter(date__year=year, date__month=month, user=request.user)
    if request.method == 'POST':
        form = TimesheetForm(request.POST)
        if form.is_valid():
            new_timesheet = form.save(commit=False)
            new_timesheet.user = request.user
            new_timesheet.save()
            messages.success(request, _('Timesheet created successfully!'))
            return redirect('timesheet_list')
        else:
            messages.success(request, _('Please make sure you filled the fields correctly!'))
    else:
        form = TimesheetForm()
    context = {
        'form': form,
        'timesheets': timesheets,
        'months': months
    }
    return render(request, template, context)
