# -*- coding: utf-8 -*-
from collections import defaultdict
import unittest
from wikipedia import wikipedia

from mock_data import wikipedia_api_request


class TestLangLinks(unittest.TestCase):
    def setUp(self):
        self.wiki = wikipedia.Wikipedia("en")
        self.wiki._query = wikipedia_api_request

    def test_langlinks_count(self):
        page = self.wiki.page('Test_1')
        self.assertEqual(len(page.langlinks), 3)

    def test_langlinks_titles(self):
        page = self.wiki.page('Test_1')
        self.assertEqual(
            list(sorted(map(lambda s: s.title, page.langlinks.values()))),
            ['Test 1 - ' + str(i + 1) for i in range(3)]
        )

    def test_langlinks_lang_values(self):
        page = self.wiki.page('Test_1')
        self.assertEqual(
            list(sorted(map(lambda s: s.lang, page.langlinks.values()))),
            ['l' + str(i + 1) for i in range(3)]
        )

    def test_langlinks_lang_keys(self):
        page = self.wiki.page('Test_1')
        self.assertEqual(
            list(sorted(page.langlinks.keys())),
            ['l' + str(i + 1) for i in range(3)]
        )

    def test_langlinks_urls(self):
        page = self.wiki.page('Test_1')
        self.assertEqual(
            list(sorted(map(lambda s: s.url, page.langlinks.values()))),
            [("https://l" + str(i + 1) + ".wikipedia.org/wiki/Test_1_-_" +
              str(i + 1)) for i in range(3)]
        )
