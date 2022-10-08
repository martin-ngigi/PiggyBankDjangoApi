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
#             "code": "$",
#             "name": "USA"
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


