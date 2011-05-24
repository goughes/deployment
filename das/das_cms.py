from WMCore.Configuration import Configuration

config = Configuration()

# web_server configuration
config.component_('web_server')
config.web_server.thread_pool = 30
config.web_server.socket_queue_size = 15
config.web_server.loglevel = 0
config.web_server.host = '0.0.0.0'
config.web_server.log_screen = True
config.web_server.url_base = '/das'
config.web_server.logfile = ''
config.web_server.port = 8212
config.web_server.pid = '%s/state/das/das_web_server.pid' % __file__.rsplit('/', 4)[0]
config.web_server.status_update = 3000
config.web_server.number_of_workers = 8
config.web_server.queue_limit = 20
config.web_server.adjust_input = True

# mongodb configuration
config.component_('mongodb')
config.mongodb.bulkupdate_size = 5000
config.mongodb.dburi = ['mongodb://localhost:8230']
config.mongodb.lifetime = 86400
config.mongodb.dbname = 'das'

# dasdb configuration
config.component_('dasdb')
config.dasdb.dbname = 'das'
config.dasdb.cachecollection = 'cache'
config.dasdb.mergecollection = 'merge'
config.dasdb.mrcollection = 'mapreduce'

# loggingdb configuration
config.component_('loggingdb')
config.loggingdb.capped_size = 104857600
config.loggingdb.collname = 'db'
config.loggingdb.dbname = 'logging'

# analyticsdb configuration
config.component_('analyticsdb')
config.analyticsdb.collname = 'db'
config.analyticsdb.dbname = 'analytics'
config.analyticsdb.history = 5184000

# mappingdb configuration
config.component_('mappingdb')
config.mappingdb.collname = 'db'
config.mappingdb.dbname = 'mapping'

# parserdb configuration
config.component_('parserdb')
config.parserdb.dbname = 'parser'
config.parserdb.collname = 'db'
config.parserdb.enable = True
config.parserdb.sizecap = 5242880

# das configuration
config.component_('das')
config.das.logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
config.das.logfile = ''
config.das.verbose = 0
config.das.multitask = True
config.das.error_expire = 300
config.das.parserdir = '%s/state/das' % __file__.rsplit('/', 4)[0] # area owned by _das account
config.das.services = ['dbs','phedex','dashboard','monitor','runregistry','sitedb','tier0','ip_service','combined','conddb']
