
""" Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

from datetime import datetime, timedelta

class Utils():

    @staticmethod
    def get_bypass_end_time(hours):
        
        bypass_end = datetime.now() + timedelta(hours=hours)
        bypass_end_hour = "{0:0>2}".format(str(bypass_end.hour))
        bypass_end_min = "{0:0>2}".format(str(bypass_end.minute))

        bypass_end_time = bypass_end_hour+":"+bypass_end_min

        return bypass_end_time


    @staticmethod
    def retrieve_dropdown_content(meraki_api):

        dropdown_content = meraki_api.get_organizations()
        
        for orga in dropdown_content:
            orga_id = orga['id']
            orga.update([("networks", meraki_api.get_networks(orga_id))])

        return dropdown_content


    @staticmethod
    def get_names(filter_orga_id, filter_network_id, dropdown_content):

        for orga in dropdown_content:
            orga_id = orga['id'] 

            if filter_orga_id == orga_id:
                orga_name = orga['name']

                for network in orga['networks']:
                    network_id = network['id']  
                    
                    if network_id == filter_network_id:
                        network_name = network['name']
                        return orga_name, network_name


