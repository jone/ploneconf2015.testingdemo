from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf2015.testingdemo.testing import DEMO_FUNCTIONAL
from unittest2 import TestCase
import transaction


# It will be here:
# https://github.com/jone/ploneconf2015.testingdemo


class TestDemo(TestCase):
    layer = DEMO_FUNCTIONAL

    def test_demo(self):
        self.assertTrue(1)

    def grant(self, *roles):
        setRoles(self.layer['portal'], TEST_USER_ID, roles)
        transaction.commit()
