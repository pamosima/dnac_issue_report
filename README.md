# Cisco DNA Center Issue Report via Webex or SMS

This is a Python application that utilizes the Cisco DNA Center API to report issues related to network devices managed by Cisco DNA Center. The application can be configured to run on a regular basis using crontab and can send notifications via Webex or SMS using eCall REST API.

## Prerequisites

To use this application, you will need the following:

- Python 3.x
- Cisco DNA Center > 2.3.3.x
- Webex account (optional)
- eCall REST API account (optional)

## Installation

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/pamosima/dnac_issue_report.git
   ```

2. Navigate to the repository directory:

   ```
   cd dnac_issue_report
   ```

3. Create a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

5. Create an environment file:

   ```
   cp .env.sample .env
   ```

5. Open `.env` and update the following parameters:

   ```
    # Cisco DNA Center
    dnacIP = "Cisco DNA Center URL" #example: dnacIP = "https://<fqdn or ip>:443"
    dnacUsername = "Cisco DNA Center username"
    dnacPassword = "Cisco DNA Center password"

    # Optional: Webex Notifications
    webexToken = "Webex Teams access token"
    webexRoomId = "Webex Teams roomId" 

    # Optional: eCall Notifications
    ecallUsername = "eCall username"
    ecallPassword = "eCall password"
   ```

   Note: If using Notification, please provide corresponding optional information.

## Usage

To run the application, simply execute the following command:

### Print to console

```
python dnac_issue_report_print.py
```

The application will retrieve a list of open issues and print the information to the console.

### Send notifcations via Webex

```
python dnac_issue_report_webex.py
```
The application will retrieve a list of open issues and send notifications via Webex.

### Send notifcations via eCall (SMS)

```
python dnac_issue_report_webex.py
```
The application will retrieve a list of open issues and send notifications via SMS.

### Send notifcations on regular basis
By default, the application will run once and exit. To run the application on a regular basis, you can use crontab. For example, to run the application every hour, you can add the following line to your crontab:

```
0 * * * * ~/code/dnac_issue_report/venv/bin/python ~/code/dnac_issue_report/dnac_issue_report_webex.py
```
## Examples

### Print to Console
```
Cisco DNA Center Issue Report
Occurrence: 25.04.2023 15:52:50
---
No of Issues: P1=0 P2=6 P3=1 P4=0
---
List of P1 & P2 Issues:
P2: The RADIUS server '192.168.99.14:1812,1813' is not responding to requests being made from the network device 'C9200-24P-1'
P2: The RADIUS server '192.168.99.13:1812,1813' is not responding to requests being made from the network device 'C9200-24P-2'
P2: The RADIUS server '192.168.99.14:1812,1813' is not responding to requests being made from the network device 'wlsn-border-1'
P2: The RADIUS server '192.168.99.13:1812,1813' is not responding to requests being made from the network device 'C9300-24T-1'
---
```

### Webex Notification
![image](https://user-images.githubusercontent.com/16715420/234295585-59d45ec5-ad01-4a18-b45f-ce00ca82546f.png)

### SMS Notification
![image](https://user-images.githubusercontent.com/16715420/234299137-10b0e7a4-ac36-4336-aee1-c62bf8aeaab4.png)


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Authors & Maintainers

People responsible for the creation and maintenance of this project:

- Patrick Mosimann <pamosima@cisco.com>

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).

## Issues/Comments

Please post any issues or comments directly on GitHub.
