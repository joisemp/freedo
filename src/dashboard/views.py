from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from datetime import date, timedelta
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render

from projects.models import Project
from tasks.models import Task
from payments.models import Payment
from clients.models import Client

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Project/task filters (can be passed via GET)
        status_filter = self.request.GET.get('status')
        try:
            task_due_days = int(self.request.GET.get('due_in', 3))
        except ValueError:
            task_due_days = 3

        if status_filter not in dict(Project.STATUS_CHOICES):
            status_filter = None

        projects = Project.objects.filter(freelancer=user)
        if status_filter:
            projects = projects.filter(status=status_filter)
        
        tasks = Task.objects.filter(
            project__freelancer=user,
            completed=False
        ).select_related('project').order_by('due_date')[:5]

        total_earnings = Payment.objects.filter(project__freelancer=user).aggregate(
            total=Sum('amount')
        )['total'] or 0

        recent_payments = Payment.objects.filter(project__freelancer=user).order_by('-date')[:5]

        # Earnings chart data
        monthly_data = (
            Payment.objects.filter(project__freelancer=user)
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        chart_labels = [m['month'].strftime('%b %Y') for m in monthly_data]
        chart_data = [float(m['total']) for m in monthly_data]

        context.update({
            'user': user,
            'ongoing_projects': projects.exclude(status='completed'),
            'upcoming_tasks': tasks,
            'total_earnings': total_earnings,
            'recent_payments': recent_payments,
            'chart_labels': chart_labels,
            'chart_data': chart_data,
            'today': date.today(),
            'project_count': projects.count(),
            'client_count': Client.objects.filter(freelancer=user).distinct().count()
        })

        return context

class DashboardFilterView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        status_filter = request.GET.get('status')
        try:
            task_due_days = int(request.GET.get('due_in', 3))
        except ValueError:
            task_due_days = 3

        if status_filter not in dict(Project.STATUS_CHOICES):
            status_filter = None

        projects = Project.objects.filter(freelancer=request.user)
        if status_filter:
            projects = projects.filter(status=status_filter)

        tasks = Task.objects.filter(
            project__freelancer=request.user,
            due_date__range=[date.today(), date.today() + timedelta(days=task_due_days)],
            completed=False
        ).order_by('due_date')[:5]

        context = {
            'ongoing_projects': projects.exclude(status='completed'),
            'upcoming_tasks': tasks,
        }

        return render(request, 'dashboard/partials/filter_results.html', context)
