from migrate_schema import *
from migrate_data import *

create_schema("schema/naljal.json", tenantId="as")
# create_all_schema("schema", tenantId="as")
# create_all_schema("schema", tenantId="as", is_portforward=False)


# create_data("data/BillingService.BusinessService.json", tenantId="pg")
# create_all_data("data", tenantId="pg")
# create_all_data("data", tenantId="pg", is_portforward=False)