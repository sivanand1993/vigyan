import requests

url="https://safeut.test.med.utah.edu/apidemo/RestService/Quote"

req=requests.get(url)
print("Status code:",req.status_code)

return_value=req.json()
print(return_value)