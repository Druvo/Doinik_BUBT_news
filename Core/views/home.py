"""Core > views > index.py"""
# PYTHON IMPORTS
# DJANGO IMPORTS
from django.views.generic import TemplateView
# Apps Import
from post.models import Post, Category
class HomePageView(TemplateView):
    """Home page view"""

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context['latest_news'] = Post.objects.filter(is_active=True).order_by('-id')[:6]
        context['cse_news'] = Post.objects.filter(category__name="CSE")
        context['civil_news'] = Post.objects.filter(category__name="CIVIL")
        context['eee_news'] = Post.objects.filter(category__name="EEE")
        context['category'] = Category.objects.all()
        context['hot'] = Post.objects.filter(is_hot=True)
        context['popular'] = Post.objects.filter(is_active=True).order_by('-total_view')[:6]
        return context
