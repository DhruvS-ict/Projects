url = "http://localhost:15000/"
db = 'first_demo_db_june'
username = 'admin'
password = 'admin'

import csv
import xmlrpc.client
import os

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("~~~~~~~~~~~~~~~~version :- ", version)

uid = common.authenticate(db, username, password, {})
print("~~~~~~~~~~~~~~~~uid :- ", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['parent_id', '=', 'my company(san francisco)']]])
print("~~~~~~~~~~~~~~~~partners :- ", partners_ids)

partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['parent_id', '=', 'my company(san francisco)']]])
print("~~~~~~~~~~~~~~~~partners count :- ", partners_count)

for partner in partners_ids:
    partners_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner])
    print("~~~~~~~~~~~~~~~~partners rec :- ", partners_rec)

models.execute_kw(db, uid, password, 'res.partner', 'write', [partners_ids, {
    'country_id': "US"
}])
# get record name after having changed it
models.execute_kw(db, uid, password, 'res.partner', 'name_get', [partners_ids])
