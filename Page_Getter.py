#Gets the google page

import requests

request = requests.get("https://raw.githubusercontent.com/Chase-Warwick/CMPUT404-Lab-1/master/Page_Getter.py")
source_code = request.text

print(source_code)

source_file = open("source_code.py", 'w')
source_file.write(source_code)

request.close()
source_file.close()
