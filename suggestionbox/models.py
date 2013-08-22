from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.timezone import now

class SuggestionManager(models.Manager):
    def get_query_set(self):
        return super(SuggestionManager, self).get_query_set().filter(in_reply_to=None)

class Comment(models.Model):
    author = models.ForeignKey(auth_models.User, blank=True, null=True)
    title = models.CharField(max_length="200")
    description = models.TextField()
    created_at = models.DateTimeField()
    in_reply_to = models.ForeignKey("Comment", blank=True, null=True, related_name='children')
    top_of_tree = models.ForeignKey("Comment", blank=True, null=True, related_name='related')

    def __unicode__(self):
        return 'author=%r, title=%r, description=%r' % (self.author, self.title, self.description)

    def most_recent_comment(self):
        if self.related.count():
            return self.related.order_by('created_at')[0]
        else:
            return None

    def descendant_count(self):
        if self == self.top_of_tree:  # Easy case
            return self.related.count() - 1
        else:
            return (self.children.count() + 
                    sum(map(lambda x:x.descendant_count(), self.children.all())))

    def save(self):
        if self.pk is None:
            self.created_at = now()

        ptr = self
        while ptr.in_reply_to is not None:
            ptr = ptr.in_reply_to

        # This ensures that the first time a top-level comment is saved,
        # its top_of_tree attribute can be saved correctly.
        if ptr == self:
            super(Comment, self).save()

        self.top_of_tree = ptr
        return super(Comment, self).save()

    objects = models.Manager()
    suggestions = SuggestionManager()
