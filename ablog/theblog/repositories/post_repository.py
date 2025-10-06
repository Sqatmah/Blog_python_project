from theblog.models import Post
from django.shortcuts import get_object_or_404



class PostRepository:



    def get_all_posts(self):
        return Post.objects.all().order_by('-post_date')



    def get_post_by_id(self, post_id):
        return get_object_or_404(Post, id=post_id)



    def create_post(self, title, title_tag, author, body):
        post = Post(title=title, title_tag=title_tag, author=author, body=body)
        post.save()
        return post
    


    def update_post(self, post_id, title=None, title_tag=None, body=None):
        post = self.get_post_by_id(post_id)
        if title:
            post.title = title
        if title_tag:
            post.title_tag = title_tag
        if body:
            post.body = body
        post.save()
        return post
    


    def delete_post(self, post_id):
        post = self.get_post_by_id(post_id)
        post.delete()
        return True



