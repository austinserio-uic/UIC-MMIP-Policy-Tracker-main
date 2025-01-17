from pyairtable import Table, Api, Base
import pandas as pd
import numpy as np
import os

AIRTABLE_ACCESS_TOKEN = os.environ.get("AIRTABLE_ACCESS_TOKEN")
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")

print(f"Airtable Access Token: {os.environ.get("AIRTABLE_ACCESS_TOKEN")}")

api = Api(AIRTABLE_ACCESS_TOKEN)
base = Base(api,AIRTABLE_BASE_ID)
table = base.table('Main v3')
data = table.all()
df = pd.DataFrame([c['fields'] for c in data])
# print(df.head())
df.replace(to_replace=np.nan,value="").to_json('policyTracker_latest.json',orient='records',indent=2)
