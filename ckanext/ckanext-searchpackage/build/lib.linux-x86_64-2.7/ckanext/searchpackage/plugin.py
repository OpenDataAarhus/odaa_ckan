
 
from ckan.plugins import IRoutes, implements, SingletonPlugin
 
from ckan.config.routing import SubMapper
 

 
 
   
 
class SearchPlugin(SingletonPlugin):
    
    implements(IRoutes, inherit=True)
 
    def before_map(self, map):
		
		print "WRONGE Now setup forum maping "
		map.connect("forum0","/forum0",	
		controller='ckanext.forum.controller:ForumController',
					action='loginDrupal')	
			
				
		print "WRONGE Done setup forum mapping"
		return map


 
