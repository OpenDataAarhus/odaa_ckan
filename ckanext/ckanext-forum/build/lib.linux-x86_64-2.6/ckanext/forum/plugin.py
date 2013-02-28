import logging
import ckan.new_authz as authz

from ckan.plugins import IRoutes, implements, SingletonPlugin
from ckan.controllers.package import PackageController
from ckan.config.routing import SubMapper
from pylons import session, c

log = logging.getLogger(__name__)


class ForumPlugin(SingletonPlugin):
    implements(IRoutes, inherit=True)

    def before_map(self, map):

		if (authz.auth_is_registered_user()):	
			with SubMapper(map, controller='forum') as m:
				m.connect('forum', '/forum1', action='read')
		else:
			with SubMapper(map, controller='forum') as m:
				m.connect('forum', '/forum', action='read')

		return map