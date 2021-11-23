from django.shortcuts import render, redirect
from django.views.generic import DetailView
from post.models import Post, Comment


class DetailView(DetailView):
    template_name = 'details.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular'] = Post.objects.filter(is_active=True).order_by('-total_view')[:6]
        self.object.total_view += 1
        self.object.save()
        context['latest_news'] = Post.objects.filter(is_active=True).order_by('-id')[:6]
        context['comment'] = Comment.objects.filter(post=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            comment = request.POST.get('comment')
            Comment.objects.create(
                post=self.object,
                name=name,
                mobile=mobile,
                message=comment
            )
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return redirect('login')
