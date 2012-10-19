"""Base module for unittesting"""

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import unittest2 as unittest


class PlonethemeFourteamworkLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import plonetheme.fourteamwork
        self.loadZCML(package=plonetheme.fourteamwork)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plonetheme.fourteamwork:default')

    def tearDownZope(self, app):
        """Tear down Zope."""


FIXTURE = PlonethemeFourteamworkLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="PlonethemeFourteamworkLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="PlonethemeFourteamworkLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
