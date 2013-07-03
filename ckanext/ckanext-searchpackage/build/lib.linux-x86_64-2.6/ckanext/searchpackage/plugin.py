import ckan.plugins as p

 
from pprint import pprint   
  
class SearchPlugin(p.SingletonPlugin):
	
	  
	p.implements(p.IPackageController, inherit=True)
	
	def before_search( self, searchparams):
		 
		
		if searchparams.get('sort') in (None, 'rank'):		
			searchparams['sort'] =  'title_string asc' #'score desc, title asc'
		return searchparams
	
	
	
	 

 
 
