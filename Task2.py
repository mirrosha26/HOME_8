import requests
from pprint import pprint 

class YaUploader:
    def __init__(self, token: str):
        self.headers =  {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def get_upload_link(self, y_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": y_path, "overwrite": "true" }
        response = requests.get(upload_url, headers = self.headers, params = params)
        return response.json()

    def upload(self, file_path: str):
        url_upload = self.get_upload_link(file_path).get("href","")
        response = requests.put(url_upload, data = open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Ваш файл загружен!")

if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)