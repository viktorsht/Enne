from enne import Download
import interface

if __name__ == "__main__":
    #url = "https://www.youtube.com/watch?v=d8ekz_CSBVg"
    url = input("url: ")
    d = Download(url)
    d.go_download()
