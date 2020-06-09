import os
import asyncio
from .DBFunctions import *

class OsuAPI:

    def __init__(self,user = "",discid = None):
        self.db = Database()
        username = " ".join(user)
        if username == "":
            self.user = self.db.fetch_osuid(discid)
        else:
            self.user = username
        self.url = "https://osu.ppy.sh/api"
        self.key = os.environ['OSUAPI']

    async def getUser(self):
        res = await fetch_json(self,"get_user",f"u={self.user}")
        if len(res) == 0:
            return None
        return res

    async def fetch_json(self,type,params = ""):
        async with aiohttp.ClientSession(headers=self.header) as session:
            try:
                async with session.get("{}/{}?k={}&{}".format(self.url,type,self.key,params)) as channel:
                    res = await channel.json()
                    return res
            except Exception as e:
                return e