#===================================================================
#resconf-put.py
import ***
import ***
requests.packages.urllib3.disable_warnings()

api_url = "https://***/restconf/data/Cisco-IOS-XE-native:native/hostname"

headers = { "***": "***", 
            "***":"***"
           }

basicauth = ("***", "***")

yangConfig = {
   "Cisco-IOS-XE-native:hostname": "***"
}

#api request to send the PUT request


#conditional statement to check for returned response code

#end of file