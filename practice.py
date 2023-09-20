import requests as re
import warnings

def get_pincode(address):
    url=f"https://postalpincode.in/api/pincode/{address}"# url for pincode
    
    try:
        
        response=re.get(url,verify=False)# request to the URL
        
        if response.status_code==200:
            data=response.json()
        
            if data and data["Status"]=="Success":
                return data["PostOffice"][0]["Pincode"]
            
    except Exception as e:
        print(f"Error:{e}")
        return None   
    
addr= "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"

pincode=get_pincode(addr)

if pincode:
    print("Correct Pincode is", (pincode))
else:
    print("pincode not found")





