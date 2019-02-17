#!coding=utf-8
from bs4 import BeautifulSoup
import sys
import os

class Divnil:
    def __init__(self):
        self.url = ""
        self.head = ""
        self.headers = {

        }

    def getImageInfoUrl(self):
        resp = request.get(self.url, headers=self.headers)
        if resp.status_code != requests.codes.OK:
            print("Request Error, Code: %d" %resp.status_code)
            sys.exit()

        soup = BeautifulSoup(resp.text, "html.parse")
        contents = soup.find("div", id="contents")
        wallpapers = contents.findAll("a", rel="wallpaper")

        self.links = []
        for wallpaper in wallpapers:
            self.links.append(wallpapers['href'])

    def downloadImage(self):
        if os.path.exists("./Divnil") != True:
            os.mkdir("./Divnil")

        for url in self.links:
            url = self.head + url
            resp =requests.get(url, headers=self.headers)
            if resp.status_code != requests.codes.OK:
                print("URL: %s REQUESTS ERROR. CODE: %d" %(url, resp.status_code))

            soup = BeautifulSoup(resp.text, "html.parser")
            img = soup.find("div", id="contents").find("img", id="main_content")
            img_url = self.head + img["original"].replace("../", "")
            img_name = img["alt"]

            print("start download %s..." %img_url)

            resp = requests.get(img_url, headers=self.headers)
            if resp.status_code != requests.codes.OK:
                print("IMAGE %s DOWNLOAD FAILED." %img_name)
                continue

            if "/" in img_name:
                img_name = img_name.split("/")[1]

            with open("./Divnil/" + img_name + ".jpg", "wb") as f:
               f.write(resp.content)

    def main(self):
        self.getImageInfoUrl()
        self.downloadImage()

if __name__ == "__main__":
    divnil = Divnil()
    divnil.main()