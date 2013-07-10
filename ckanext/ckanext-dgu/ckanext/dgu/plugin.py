import os

from logging import getLogger
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IMiddleware
from ckan.plugins import IAuthFunctions
from ckan.plugins import ISession
from ckanext.dgu.authentication.drupal_auth import DrupalAuthMiddleware

class DrupalAuthPlugin(SingletonPlugin):
    '''Reads Drupal login cookies to log user in.'''
    implements(IMiddleware,    inherit=True)

    def make_middleware(self, app, config):
        return DrupalAuthMiddleware(app, config)
