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

import meraki
import os
from dotenv import load_dotenv

load_dotenv()

class Meraki_API():

    def __init__(self):
        self.BASE_URL = "https://api.meraki.com/api/v1"
        self.DASHBOARD = meraki.DashboardAPI(
                            api_key=os.environ['MERAKI_API_TOKEN'],
                            base_url=self.BASE_URL,
                            print_console=False,
                            suppress_logging=True)


    def get_organizations(self):
        response = self.DASHBOARD.organizations.getOrganizations()
        return response


    def get_networks(self, orgID):
        response = self.DASHBOARD.organizations.getOrganizationNetworks(
            orgID, total_pages='all'
        )
        return response


    def get_port_schedules(self, network_id):
        response = self.DASHBOARD.switch.getNetworkSwitchPortSchedules(
            network_id
        )
        return response

    
    def list_switch_ports(self, serial):

        response = self.DASHBOARD.switch.getDeviceSwitchPorts(
            serial
        )

        return response


    def enable_switch_port(self, serial, port_id):

        response = self.DASHBOARD.switch.updateDeviceSwitchPort(
            serial, port_id,  
            enabled=True, 
            poeEnabled=True, 
            portScheduleId=None, 
        )

        print(response)


    def attach_switch_port_schedule(self, serial, port_id, port_schedule):
        
        response = self.DASHBOARD.switch.updateDeviceSwitchPort(
            serial, port_id,  
            portScheduleId=port_schedule, 
        )

        print(response)


    def list_device_of_network(self, network_id):

        response = self.DASHBOARD.networks.getNetworkDevices(
            network_id
        )

        return response