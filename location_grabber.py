#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests 
import json

# retrieve location data from ip address
def grab_location(unique_df):
    results = []
    for i in unique_df[0]:
        try:
            ip_address = str(i)
            # URL to send the request to
            request_url = 'https://geolocation-db.com/jsonp/' + ip_address
            # send request and decode the result
            response = requests.get(request_url)
            result = response.content.decode()
            # clean the returned string so it just contains the dictionary data for the IP address
            result = result.split("(")[1].strip(")")
            # convert this data into a dictionary
            result  = json.loads(result)
            # append dictionary to the list
            results.append(result)
            return results
        except:
            pass
        