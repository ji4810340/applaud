import os
from applaud.endpoints.sales_reports import SalesReportsEndpoint
from applaud.connection import Connection

KEY_ID = "XXXXXXXXXX"
ISSUER_ID = "XXXXXX-XXXXXXX-XXXXXX-XXXXXXX"
PATH_TO_KEY = os.path.expanduser('path/to/your/key.p8')
# You can find your vendor number here [Payments and Financial Reports](https://help.apple.com/app-store-connect/#/dev3a16f3fe0)
VENDOR_NUMBER = 'XXXXXXXX'

with open(PATH_TO_KEY, 'r') as f:
    PRIVATE_KEY = f.read()

# Create the Connection
connection = Connection(ISSUER_ID, KEY_ID, PRIVATE_KEY)

r = connection.sales_reports().filter(
    report_sub_type=SalesReportsEndpoint.ReportSubType.SUMMARY, # or 'SUMMARY'
    report_type=SalesReportsEndpoint.ReportType.SALES, # or 'SALES'
    frequency=SalesReportsEndpoint.Frequency.MONTHLY, # or 'MONTHLY'
    report_date='2021-12',
    vendor_number=VENDOR_NUMBER
).get()

r.save('sales_reports.txt', decompress=True)
