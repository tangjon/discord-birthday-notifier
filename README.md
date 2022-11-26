# Setup

## config.ini
Create `config.ini` in the root directory (samve directory of this README.md).
Inside specify your discord webhook.
```
[discord]
birthday-web-hook = https://discord.com/api/webhooks/.../..
```

## contacts.csv
Download this file from [Google Contacts](https://contacts.google.com/). 
Export your contacts as csv and place it into the root directory.

# Save docker images

```commandline
docker save -o birthdaynotifier.tar birthdaynotifier
```