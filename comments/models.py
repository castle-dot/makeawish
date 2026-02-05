from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    wish = models.ForeignKey('wishes.Wish', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.user.username} on {self.wish.title}'