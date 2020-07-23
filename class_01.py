import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


class Music:
    __SEARCH_URL = "https://imusic.я.wiki/search/"
    __DOWNLOAD_URL = 'https://imusic.я.wiki'
    __NAME = 'Music-Downloader'
    __STATUS_CODE = 200

    def __init__(self, song_name, save_name):
        self.song_name = song_name
        self.save_name = save_name

    def get_html(self):
        request = requests.get(self.__SEARCH_URL + self.song_name)
        return request

    def get_current_url(self):
        return self.__SEARCH_URL + self.song_name

    def get_parse_name(self):
        return self.__NAME

    def music_parse(self):
        try:
            html = self.get_html()
            print(f'html {html}\n')

            soup = BeautifulSoup(html.text, 'lxml')
            total_res = soup.find('h1', class_='title').text
            print(total_res.replace(' ', ' - '), '\t\n')

            group_names = soup.find_all('h2', class_='playlist-name')

            for i, element in enumerate(group_names):   # working with index i, # do something with (element)
                groups = element.find('b').text
                song_names = element.find('em').text
                print(f" \t{i} Group_Name: {groups} - {song_names} ")

            download_urls = []
            tmp_urls = soup.find_all('a', class_='playlist-btn-down no-ajaxy')

            # Getting href
            for href in tmp_urls:
                href = href['href']
                download_urls.append(href)
            print()

            # Building final Download url
            choice = int(input("Enter song-number: "))
            result_url = self.__DOWNLOAD_URL + download_urls[choice]                     # Download url

            # Downloading
            res = requests.get(result_url, stream=True)
            if res.status_code == self.__STATUS_CODE:
                with open(self.save_name + '.mp3', 'wb') as file:
                    file.write(res.content)

        except ConnectionError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    music = Music('', '')    # Song name, song name to download file
    print(music.get_current_url())
    music.music_parse()
