import urllib2
import logging
import json

log = logging.getLogger(__name__)

class DrupalRequestError(Exception): pass

class DrupalClient(object):
	def __init__(self, drupal_settings=None):
		try:
			from pylons import config
		except ImportError:
			assert 0, 'ry the Pylons config for it.'
		domain = config.get('dgu.xmlrpc_domain')
		 
		self.drupal_url = domain

	def get_user_id_from_session_id(self, session_id):
		 
		try:
			url=self.drupal_url +  "/odaa_user/"+session_id
			log.debug('Url to check at: : %s', url) 
			
			try:
				j = urllib2.urlopen(url)
			except urllib2.URLError  as e:
				log.error("Url2 error %s " , e )
				return False
			  
			
			username = json.load(j)["username"]
		 	
			if (username <> ""):
				session = username
			else:
				return False
 
 		except Exception as e:
			raise DrupalRequestError('Drupal returned error for session_id %r: %r' % (session_id, e))
		except ProtocolError, e:
			raise DrupalRequestError('Drupal returned protocol error for session_id %r: %r' % (session_id, e))
		log.info('Obtained Drupal session for session ID %r...: %r', session_id[:4], session)
		return session
