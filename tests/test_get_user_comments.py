import pytest
import unittest

from search_hn import SearchHN

class GetUserComments(unittest.TestCase):
    def setUp(self):
        self.hn = SearchHN()

    def test_get_user_comments(self):
        comments = (
            self.hn.comments()
            .author("nicolashahn")
            .max_hits_per_page()  # 1000 items per query max
            .get()
        )
        assert(len(comments)>0)
