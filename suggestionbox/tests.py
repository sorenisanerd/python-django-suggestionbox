from django.test import TestCase

from suggestionbox import models


class CommentTests(TestCase):
    def test_descendant_count(self):
        kwargs = {'title': 'Title', 'description': 'Description'}
        top = models.Comment(**kwargs)
        top.save()

        unrelated = models.Comment(**kwargs)
        unrelated.save()

        c_1 = models.Comment(in_reply_to=top, **kwargs)
        c_1.save()

        c_1_1 = models.Comment(in_reply_to=c_1, **kwargs)
        c_1_1.save()

        c_1_2 = models.Comment(in_reply_to=c_1, **kwargs)
        c_1_2.save()

        c_1_2_1 = models.Comment(in_reply_to=c_1_2, **kwargs)
        c_1_2_1.save()

        c_1_3 = models.Comment(in_reply_to=c_1, **kwargs)
        c_1_3.save()

        c_2 = models.Comment(in_reply_to=top, **kwargs)
        c_2.save()

        self.assertEquals(top.descendant_count(), 6)
        self.assertEquals(c_1.descendant_count(), 4)
        self.assertEquals(c_2.descendant_count(), 0)
        self.assertEquals(c_1_1.descendant_count(), 0)
        self.assertEquals(c_1_2.descendant_count(), 1)
        self.assertEquals(c_1_3.descendant_count(), 0)
