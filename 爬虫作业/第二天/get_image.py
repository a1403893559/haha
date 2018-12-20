from urllib.request import Request,urlopen
import ssl

def writeImage(image_url):
    print("正在保存")
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0"
    }
    requestContent = ssl._create_unverified_context()
    request = Request(image_url, headers=headers)
    response = urlopen(request,context=requestContent)
    image = response.read()
    filename = 'gp=0.jpg'
    # filename = link[-10:]
    with open(filename, "wb") as f:
        f.write(image)
        print("已成功下载"+filename)


def main():
    image_url='https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3008776979,632905106&fm=27&gp=0.jpg'
    writeImage(image_url)

if __name__ == '__main__':
    main()