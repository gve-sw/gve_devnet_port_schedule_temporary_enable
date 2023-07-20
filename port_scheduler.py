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

from apscheduler.schedulers.background import BackgroundScheduler


class PortSchedular():

    def __init__(self, meraki_api, name, timezone):
        
        self.name=name
        self.meraki = meraki_api
        self.network_id=""

        self.bypass_active = False

        self.scheduler = BackgroundScheduler(timezone=timezone)
        self.job = None
        self.scheduler.start()


    def schedule_port_bypass(self, hours, network_id):
        
        print("Bypass port schedule for: " + str(hours) + " hours.")

        if self.bypass_active:
            print("Update existing job.")
            self.job.remove()
    
        else:
            self.__bypass_port_schedule(network_id)
            
        self.job = self.scheduler.add_job(self.revert_port_bypass, 'interval', hours=hours)

        self.bypass_active = True
        

    def revert_port_bypass(self):

        print("Revering port bypass.")

        self.__revert_port_schedule_bypass()

        self.job.remove()
        
        self.bypass_active = False
        
    
    def __bypass_port_schedule(self, network_id):
        
        self.network_id = network_id
        network_devices = self.meraki.list_device_of_network(self.network_id)

        for device in network_devices:
            serial = device['serial']
            model = device['model']

            if "MS" in model:                
                device_ports = self.meraki.list_switch_ports(serial)
                
                for port in device_ports:
                    tags = port['tags']
                    
                    if 'bypass_option' in tags:
                        port_id = port['portId']
                        self.meraki.enable_switch_port(serial, port_id)


    def __revert_port_schedule_bypass(self):

        network_devices = self.meraki.list_device_of_network(self.network_id)
        
        for device in network_devices:
        
            serial = device['serial']
            model = device['model']
            
            if "MS" in model:
                device_ports = self.meraki.list_switch_ports(serial)
                
                for port in device_ports:
                    tags = port['tags']

                    if 'bypass_option' in tags:
                        port_id = port['portId']
                        port_schedule_id = self.__get_port_schedule_id(self.network_id)
                        self.meraki.attach_switch_port_schedule(serial, port_id, port_schedule_id)


    def __get_port_schedule_id(self, network_id):

        port_schedules = self.meraki.get_port_schedules(network_id)
    
        for port_schedule in port_schedules:

            if port_schedule['name'] == self.name:
                
                return port_schedule['id']



