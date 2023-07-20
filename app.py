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

from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os

from meraki_api import Meraki_API
from port_scheduler import PortSchedular
from utils import Utils


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'GET':

            return render_template('configure.html', hidden_links=True, dropdown_content = dropdown_content)

        if request.method == 'POST':
            
            orga_id = request.form.get("organizations_select")
            network_id = request.form.get("network_select")
            bypass_hours = int(request.form.get("hour_select"))

            bypass_until = Utils.get_bypass_end_time(bypass_hours)
            orga_name, network_name = Utils.get_names(orga_id, network_id, dropdown_content)

            port_schedular.schedule_port_bypass(bypass_hours, network_id)

            return render_template('feedback.html', hidden_links=False, orga_name=orga_name, network_name=network_name, bypass_until=bypass_until, port_schedule_name=ACCESS_PORT_SCHEDULE_NAME)

    except Exception as e: 
        print(e)  
        return render_template('configure.html', error=True, errormessage=e, dropdown_content = dropdown_content)


@app.route('/revert', methods=['GET', 'POST'])
def revert():
    try:
        port_schedular.revert_port_bypass()
        return redirect('/')

    except Exception as e: 
        print(e)
        if 'No job' in str(e):
            e = 'Nothing to revert. The bypass probably ended already.'  
        return render_template('configure.html', error=True, errormessage=e, dropdown_content = dropdown_content)


if __name__ == "__main__":
    
    load_dotenv()

    meraki_api = Meraki_API()
    
    dropdown_content = Utils.retrieve_dropdown_content(meraki_api)
    
    ACCESS_PORT_SCHEDULE_NAME = os.environ['ACCESS_PORT_SCHEDULE_NAME']
    TIMEZONE = os.environ['TIMEZONE']

    port_schedular = PortSchedular(meraki_api, ACCESS_PORT_SCHEDULE_NAME, TIMEZONE)

    app.run(host='0.0.0.0', port=5001, debug=True)