# Update OKTA prefix list from okta list

USE AT YOUR OWN RISK. THIS EXAMPLE IS PROVIDED AS IS

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Install requests python sdk : pip3 install requests
* Setup authentication as listed below
* run the script using: python3 cgxUpdateOKTA.py --prefix pOKTA --url "https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json" 

cgxUpdateOKTA.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)


Example of a run:
```
~/proj/cgxUpdateOKTA$ python3 cgxUpdateOKTA.py --prefix pOKTA --url "https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json" 
pOKTA update successfuly
```
