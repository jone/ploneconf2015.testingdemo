from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class DemoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER)


DEMO_FIXTURE = DemoLayer()
DEMO_FUNCTIONAL = FunctionalTesting(
    bases=(DEMO_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name='ploneconf2015.testingdemo:functional')
