from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf2015.testingdemo.testing import DEMO_FUNCTIONAL
from unittest2 import TestCase
import transaction


# It will be here:
# https://github.com/jone/ploneconf2015.testingdemo


class TestDemo(TestCase):
    layer = DEMO_FUNCTIONAL

    @browsing
    def test_demo(self, browser):
        self.grant('Manager')
        folder = create(Builder('folder').titled('My Documents'))
        create(Builder('document').titled('Foo').within(folder))
        create(Builder('document').titled('Bar').within(folder))

        browser.login().open(folder, view='folder_contents')
        self.assertEquals(
            [{'': 'Foo',
              u'State': u'',
              u'Size': '0 KB',
              u'Modified': 'Oct 16,
 2015 01:29 PM',
              u'Title': 'Foo'},
             {'': 'Bar',
              u'State': u'',
              u'Size': '0 KB',
              u'Modified': 'Oct 16,
 2015 01:29 PM',
              u'Title': 'Bar'}]
            browser.css('#content table').first.dicts(head_offset=1))

    def grant(self, *roles):
        setRoles(self.layer['portal'], TEST_USER_ID, roles)
        transaction.commit()
