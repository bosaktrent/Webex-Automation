# Cisco Webex Teams Automation
This repository contains some simple scripts to automate tasks in Cisco Webex Teams.

To get started you'll need to `install` the required modules and update required tokens.

## webex-create-and-add.py
This script creates a new Cisco Webex Teams room, adds a user, and sends a message to the new room.

### Requirements
* Python 3
* [Requests][requests_link]
* Cisco Webex Teams account

*The details shown below are the default values. Editing them is completely optional.* 

```py
room_name = "My New Room"               # New room name
user_name = "gifbot@webex.bot"          # User to add to new room
message = "Hello World!"                # Message to send to new room
```

*You MUST add your persoanl access token prior to running this script.*

Replace `{}` with your personal token. Do NOT delete the `Bearer` keyword.

```py
if __name__ == '__main__':
    token = "Bearer {}"	# Personal access token
    main()
```

[requests_link]: https://2.python-requests.org/en/master/
[webex_link]: https://developer.webex.com/

For information regarding your access token, click [here][webex_link] and sign into your Cisco Webex Teams account.

To run this script, run the command: `python3 webex-create-and-add.py`

## Questions/Discussion
If you find an issue, please raise an issue within the issues section.

Also, if you would like to extend one of these scripts for a more specific use case, please feel free to contact me with any questions/concerns you may have. 

---
<p>Trent Bosak<br>
Cisco Technical Sales Engineer Intern</p>