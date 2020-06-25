from urllib.request import Request, urlopen
import urllib.request
import json
import os
import sys
import subprocess
exclude = ["default","nsfw","spoiler"] #previews to exclude. If the script fails and it gives you the preview, append it to the array.
sys.argv.pop(0)
for url in sys.argv:
    req = Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)') #Random user agent to avoid getting 429 errors.
    content = urlopen(req).read()
    data = json.loads(content)
    for item in data["data"]["children"]:
        if item["data"]["url"].find("comments") == -1:
            print(item["data"]["thumbnail"]+item["data"]["url"]) #print the current image downloading
            if not item["data"]["thumbnail"] in exclude:
                urllib.request.urlretrieve(item["data"]["thumbnail"],"thumb."+item["data"]["url"].replace("/","_"))
                urllib.request.urlretrieve(item["data"]["url"],item["data"]["url"].replace("/","_"))

subprocess.Popen("notify-send 'Done downloading wallpapers' ", shell=True, stdout=subprocess.PIPE).stdout.read()


