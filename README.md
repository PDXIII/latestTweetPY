LatestTweetByHashTag
====================

There was a time, when Twitter changed its API and a lot of plug ins stopped working. At this time I just wanted to display my latest tweet on my own website, but without all that Twitter branded clutter. So, I decided to write my own server sided plug in.

If you want to display your latest tweet with a specified #hashtag on a website, then this could maybe interesting for you!

### Installation

1. Head over to [Twitter Developers](https://dev.twitter.com).
2. Register yourself as developer and register a new app.
3. Look for a safe directory on your server (e.g. `/bin`).
4. Clone this repository into that directory.
5. Make sure you have [Twython](https://twython.readthedocs.org/en/latest/usage/install.html) installed
6. Open `config.json` set the parameters and save as `.config.json`.
7. Setup a cronjob, which continously runs the script e.g. `*/10 * * * * PATH_TO_YOUR_SCRIPT/latestTweet.py`.

### Dependencies

+ [Twython](https://twython.readthedocs.org/en/latest/usage/install.html) - Actively maintained, pure Python wrapper for the Twitter API.
