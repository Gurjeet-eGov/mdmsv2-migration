import json
from localisation import SchemaProcessor
import migrate_localisations

OUTPUT_FILE_PATH = "MDMS_Localizations.json"
TENANT = "pg"
SCHEMA_PATH = "schema/pqm.json"
MODULE_CODE = "rainmaker-workbench"
LOCALE = "en_IN"

loc_obj=SchemaProcessor(path=SCHEMA_PATH)
loc_obj.generateLocalisations(module=MODULE_CODE, locale=LOCALE)

with open(OUTPUT_FILE_PATH, 'w') as file:
    file.write(json.dumps(loc_obj.LocalisationsList))

"""
by default it takes port-forward url, ensure to port-forward localization service
"""

migrate_localisations.upsert_localisation(OUTPUT_FILE_PATH, TENANT)

