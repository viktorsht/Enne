import requests

class Verificador:

    def check_video_url(self,video_id):
        checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
        video_url = checker_url + video_id

        request = requests.get(video_url)

        return request.status_code == 200
