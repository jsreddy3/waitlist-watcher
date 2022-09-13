# waitlist-watcher
This script watches the waitlist of a given Stanford course and sends an email when a spot opens.

## How to Setup
1. Find the path to your chrome driver. If you're not sure how, [this guide](https://www.youtube.com/watch?v=KrHHnbfbEtE&themeRefresh=1) should help.
2. Add your source email address, source email API password, and destination email address. The source email password is not your actual email password. If you're not sure where to find this password, [look here](https://www.youtube.com/watch?v=JRCJ6RtE3xU).

Note: I didn't request the HTML of the explorecoureses page using simpler means, such as the python requests library, because Stanford wouldn't let me.
