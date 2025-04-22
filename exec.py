from migrate_schema import *
from migrate_data import *

"""
by default the port-forward is set to true, check env_config.json
below are exmaples for how to migrate specific schema or data file, or entire folder
"""

#create_schema("schema/TL.json", tenantId="pg")
# create_all_schema("schema", tenantId="as")
# create_all_schema("schema", tenantId="as", is_portforward=False)


create_data("data/TL/TradeLicense.CalculationType.json", tenantId="pg.cityc")
#create_all_data("data/TL", tenantId="pg")
# create_all_data("data", tenantId="pg", is_portforward=False)