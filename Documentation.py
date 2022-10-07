#Youtube link https://www.youtube.com/watch?v=dunf5IqxRaA

# END POINTS
import json


# 1. Retrive all categories ie GET
# http://127.0.0.1:8000/categories/

# 2. Retrive single categories ie GET
# http://127.0.0.1:8000/categories/1

# 3. Create category ie POST
# http://127.0.0.1:8000/categories/ (Callback url)

# Then paste the following in the body after selectin type raw and json
# {
#     "name": "Transport"
# }

# 4. Update data i.e PATCH

# http://127.0.0.1:8000/categories/1/
# The select PATCH and paste following in body and select raw and JSON
# {
#     "name": "Transport"
# }