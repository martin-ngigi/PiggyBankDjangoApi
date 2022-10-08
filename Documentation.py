#Youtube link https://www.youtube.com/watch?v=dunf5IqxRaA

# END POINTS
import json
from locale import currency

# POSTMAN APP

# CATEORY
# ----------
# 1.GET - Retrive all categories ie GET
# endpoint -> http://127.0.0.1:8000/categories/

# 2. GET - Retrive single categories ie GET
# endpoint -> http://127.0.0.1:8000/categories/1

# 3.POST-  Create category 
# endpoint -> http://127.0.0.1:8000/categories/ (Callback url)
# Then paste the following in the body after selectinG type raw and json
# {
#     "name": "Transport"
# }

# 4.PATCH Update data 
# http://127.0.0.1:8000/categories/1/
# The select PATCH and paste following in body and select raw and JSON
# {
#     "name": "Transport"
# }



# CURRENCY
# ---------
# 1. POST . i.e. create new currency
#  endpoint -> http://127.0.0.1:8000/currencies/
# in body  select body, then raw then Json
#  body ->
#         {
#             "code": "USD",
#             "name": "US Dollars"
#         }

# 2. GET - Retrieve all
# endpoint -> http://127.0.0.1:8000/currencies/

# 3. GET Retrieve single currency
# endpoint -> http://127.0.0.1:8000/currencies/2/

# 4.PATCH Update data 
# endpoint -> http://127.0.0.1:8000/currencies/2/
# The select PATCH and paste following in body and select raw and JSON
# {
#     "code": "Ksh",
#     "name": "Kenyan Currency"
# }

# 5. DELETE
# endpoint -> http://127.0.0.1:8000/currencies/2/




# TRANSACTIONS
# ---------
# 1. POST . i.e. create new transactions
#  endpoint -> http://127.0.0.1:8000/transactions/
# in body  select body, then raw then Json
#  body ->
#         {
#               "amount":1000,
#               "currency": 2,
#               "date": "2022-08-10 09:13:00",
#               "description": "Testing Kenyan currency",
#               "category": 2
#           }

# 2. GET - Retrieve all
# endpoint -> 127.0.0.1:8000/transactions/

# 3. GET Retrieve single currency
# endpoint -> 127.0.0.1:8000/transactions/1/

# 4.PATCH Update data 
# endpoint -> http://127.0.0.1:8000/transactions/2/
# The select PATCH and paste following in body and select raw and JSON
#         {
#               "amount":1000,
#               "currency": 2,
#               "date": "2022-08-10 09:13:00",
#               "description": "Testing Kenyan currency",
#               "category": 2
#           }

# 5. DELETE
# endpoint -> http://127.0.0.1:8000/transactions/2/


# AUTHENTICATION 
# --------------------
# python manage.py createsuperuser
# 1.POST - endpont -> http://127.0.0.1:8000/login/
# body , select raw, selct json and paste the following
# {
#     "username":"martin",
#     "password":"martin"
# }
# Then press send to get the authorization token ie a5af394723a8b2246606e8e408c4e6bb2216c4ae
# 2. To authenticate
# send token
# in the GET Transaction select "Authorization", In the "Type" select "API key". 
# Then insert the following
# Key -> Authorization
# Value -> Token a5af394723a8b2246606e8e408c4e6bb2216c4ae
