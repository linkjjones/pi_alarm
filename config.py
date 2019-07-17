import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
PIN = 26                       # Pin to which the PowerSwitch Tail is connected
ALARM_DURATION = 15            # Light duration in minutes

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = False
BASIC_AUTH_USERNAME = 'alarm'
BASIC_AUTH_PASSWORD = 'password'

# -- Custom Happy Messages
MESSAGES = [
    "Love you!",
    "You're smart AND pretty!",
    "You have a winning smile!",
    "You're home now; kick back and relax!",
    "Your children arise and call you blessed.",
    "What's for breakfast?",
    "Grab a stuffed animal or husband, because it's time to cuddle!",
    "Honey, did you just fart?",
    "Did you lock the front door?",
    "I'm glad we got married!",
    "Thanks for putting up with me <3",
    "Violets are blue, roses are red. Turn off that light because it's time for bed!",
    "If you're happy and you know it go to sleep!",
    "A hug! A hug! My kingdom for a hug!",
    "Did you get your bedtime kiss yet?",
    "You have a lovely voice! But be quiet now because it's time for bed.",
    "My amazing Ozi...",
    "Jeffrey loves you!",
    "Jesus loves you!"
]
