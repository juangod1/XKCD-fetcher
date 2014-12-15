import urllib.request
import time, re, os


def xkcd_fetcher():
    print("\nFetching XKCD...\n")
    webpage = urllib.request.urlopen("http://c.xkcd.com/random/comic/")
    webpage_text = str(webpage.read())
    expression = "for hotlinking/embedding\): http://imgs.xkcd.com/comics/.+\.png"
    output = re.search(expression, webpage_text)
    image_dirty_link = output.group(0)
    image_link = image_dirty_link[27:]
    image_name = image_link[28:]
    urllib.request.urlretrieve(image_link, "comics/" + image_name)
    return image_name

while True:
    try:
        image_name = xkcd_fetcher()
        os.startfile("comics\\" + image_name)
        break
    except FileNotFoundError:
        os.system("mkdir comics")
        image_name = xkcd_fetcher()
        os.startfile("comics\\" + image_name)
        break
    except urllib.error.URLError:
        time.sleep(3)
        print("\nIt seems like your connection to the internet is not working, trying again in 5 seconds.\n")
        for i in range(1,6):
            time.sleep(1)
            print(i)
