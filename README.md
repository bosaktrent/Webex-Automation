# Cisco Webex Teams Automation
This repository contains some simple scripts to automate tasks in Cisco Webex Teams.

To get started you'll need to `install` the required modules and update the token as shown below.

Replace `{}` with your personal token. Do NOT delete the `Bearer` keyword.

```py
if __name__ == '__main__':
    token = "Bearer {}"	# Personal access token
    main()
```
For information regarding your access token, click [here][webex_link] and sign into your Cisco Webex Teams account.

[webex_link]: https://developer.webex.com/

## webex-create-and-add.py
This script creates a new Cisco Webex Teams room, adds a user, and sends a message to the new room.

### Requirements
* Python 2.7
* [Requests][requests_link]
* Cisco Webex Teams account

*The details shown below are the default values. Editing them is completely optional.* 

```py
room_name = "My New Room"               # New room name
user_name = "gifbot@webex.bot"          # User to add to new room
message = "Hello World!"                # Message to send to new room
```

[requests_link]: https://2.python-requests.org/en/master/

To run this script, run the command: `python webex-create-and-add.py`.

## excel-to-new-room.py
This script creates a new room, and adds users from an Excel spreadsheet containing email adresses.
### Requirements
* Python 2.7
* [Requests][requests_link]
* [Pandas][pandas_link]
* Cisco Webex account
 
*This script uses `email_addresses.xlsx` (included in this repo) as the file containing email addresses. You MUST have this file in the same directory as `excel-to-new-room.py`.*
 
```py
filename = 'email_addresses.xlsx'       # File containing email_addresses
room_name = "My New Room"               # New room name
message = "Welcome!"                    # Message to send to new room
```

[requests_link]: https://2.python-requests.org/en/master/
[pandas_link]: https://pandas.pydata.org/

To run this script, run the command: `python excel-to-new-room.py`.

## Questions/Discussion
If you find an issue, please raise an issue within the issues section.

Also, if you would like to extend one of these scripts for a more specific use case, please feel free to contact me with any questions/concerns you may have. 

---
<p>Trent Bosak<br>
Cisco Technical Sales Engineer Intern</p>