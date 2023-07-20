# gve_devnet_port_schedule_temporary_enable

The Meraki Port Schedule feature is a great way to save energy and reduce our carbon footprint by automatically turning off devices at times when they are not normally used (e.g., at night).
This sample code shows a simple way to bypass the port schedule at times an exception is needed (such as a special event during the night). It allows you to remove the port schedule from tagged switch ports for 2, 4, or 6 hours.

## Contacts
* Ramona Renner

## Solution Components
* Meraki Switch
* Meraki device connected to a switch port controlled by the port schedule
* Meraki Dashboard

## Workflow

![/IMAGES/0image.png](/IMAGES/workflow.png)


## Related Sandbox Environment

This sample code can be tested using a Cisco sandbox [Meraki Enterprise](https://devnetsandbox.cisco.com/RM/Diagram/Index/e7b3932b-0d47-408e-946e-c23a0c031bda?diagramType=Topology) that contains of one MX84 security appliance and one MS225-24P switch, one MR53 AP, and one MV12 Camera. 


## Prerequisites

### Create and assign a port schedule

In case you have no port schedule configured in the network yet, please follow the instructions on the [Port Schedules Documentation Page](https://documentation.meraki.com/MS/Access_Control/Port_Schedules) to create a port schedule and apply the schedule to all switch ports preferred. 

### Add a switch port tag

Add the tag **bypass_option** to all switch ports from the last section that should be bypassed via this sample code. Therefore, follow the instructions on the [Switch Ports Page](https://documentation.meraki.com/MS/Port_and_VLAN_Configuration/Switch_Ports).   


### Meraki API Key
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).


## Installation/Configuration

1. Make sure you have [Python 3.8.0](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

2. Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html)).

3. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```

4. Clone this Github repository:  
  ```git clone [add github link here]```
  * For Github link: 
      In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
      ![/IMAGES/giturl.png](/IMAGES/giturl.png)
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it

5. Access the downloaded folder:  
    ```cd gve_devnet_port_schedule_temporary_enable```

6. Install all dependencies:  
  ```pip install -r requirements.txt```

7. Fill in your variables in the **.env** file:      
      
  ```  
    MERAKI_API_TOKEN="<Add the Meraki API key (see last section)>"
    ACCESS_PORT_SCHEDULE_NAME="<Name of the port schedule to bypass>"
    TIMEZONE="<Timezone the script is running in e.g Europe/Berlin>"
  ```

  > Note: Mac OS hides the .env file in the finder by default. View the demo folder for example with your preferred IDE to make the file visible. 

  > Note: Retrieve the organization and network ID via the interactive API documentation and the [Get Organizations Call](https://developer.cisco.com/meraki/api-v1/#!get-organizations) and [Get Organization Networks](https://developer.cisco.com/meraki/api-v1/get-organization-networks/) endpoints.

## Usage

To run the program, use the command:

```
python3 app.py
```


## Screenshots
![/IMAGES/0image.png](/IMAGES/screenshot1.png)
![/IMAGES/0image.png](/IMAGES/screenshot2.png)


## Limitations

The sample code:

* supports only one bypass and network at a time
* supports only one port schedule
* supports only Meraki Switch ports 


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.