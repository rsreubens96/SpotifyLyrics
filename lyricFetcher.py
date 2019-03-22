import spotipy
import spotipy.util as util
import random
import requests
import time
from bs4 import BeautifulSoup
import time
import wx
from GUI_Main import guiMain
from threading import Thread
from gui import SpotifyLyrics


def progressBar(progress, duration):
    progressSeconds = int((progress / 1000)%60)
    progressMinutes = int((progress / (1000*60))%60)
    durationSeconds = int((duration / 1000)%60)
    durationMinutes = int((duration / (1000*60))%60)
    percentage = int((progress / duration) * 100)
    r = [progressSeconds, progressMinutes, durationSeconds, durationMinutes, percentage]
    return r

def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + 'H1yVKgAtF3p6BczQ_idi34ePGCu9lPPs7Bc7CwFgT8_W6ugkAObB_WpCxzQu2iEd'}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics

def run(self):
    update = False
    currentTrack = None
    duration = 0
    progress = 0
    while(True):
        scope = 'user-read-playback-state'
        token = util.prompt_for_user_token('thornbird116', scope, client_id='7ef6e7b8699046f3a23bf7be5ac8ec86', client_secret='126128f52f1c44fb8900fba37fcb5f08', redirect_uri='http://localhost:8080')
        spotify = spotipy.Spotify(auth=token)
        currentlyPlaying = spotify.currently_playing()


        track = currentlyPlaying['item']
        progress = currentlyPlaying['progress_ms']
        duration = track['duration_ms']
        name = track['name']
        artists = track['artists']
        names = []
        for a in artists:
            names.append(a['name'])
        mainArtist = names[0]
        if currentTrack is None:
            currentTrack = name
            update = True
        elif currentTrack != name:
            currentTrack = name
            update = True
        else:
            update = False

        if(update == True):
            response = request_song_info(name, mainArtist)
            json = response.json()
            remote_song_info = None

            for hit in json['response']['hits']:
                if mainArtist.lower() in hit['result']['primary_artist']['name'].lower():
                    remote_song_info = hit
                    break
            if remote_song_info:
                song_url = remote_song_info['result']['url']
                finalPrint = "Currently Playing: " + currentTrack + " by " + names[0] + "\n" + scrap_song_url(song_url)
                self.updateText(finalPrint)
            else:
               self.updateText("Stop listening to weeb shit")

        r = progressBar(progress, duration)
        print(r[0], r[1], r[2], r[3], r[4])
        self.updateTime(r[0], r[1], r[2], r[3], r[4])
        time.sleep(1)
def main():

    app = wx.App()
    frm = SpotifyLyrics(None)
    thread = Thread(target = run, args = (frm, ))
    thread.start()
    mainFrm = guiMain(frm)
    frm.Show()
    app.MainLoop()
#
#     update = False
#     currentTrack = None
#     duration = 0
#     progress = 0
#     while(True):
#         scope = 'user-read-playback-state'
#         token = util.prompt_for_user_token('thornbird116', scope, client_id='7ef6e7b8699046f3a23bf7be5ac8ec86', client_secret='126128f52f1c44fb8900fba37fcb5f08', redirect_uri='http://localhost:8080')
#         spotify = spotipy.Spotify(auth=token)
#
#         currentlyPlaying = spotify.currently_playing()
#         track = currentlyPlaying['item']
#         progress = currentlyPlaying['progress_ms']
#         duration = track['duration_ms']
#         name = track['name']
#         artists = track['artists']
#         names = []
#         for a in artists:
#             names.append(a['name'])
#         mainArtist = names[0]
#
#         if currentTrack is None:
#             currentTrack = name
#             update = True
#         elif currentTrack != name:
#             currentTrack = name
#             update = True
#         else:
#             update = False
#
#         if(update == True):
#             response = request_song_info(name, mainArtist)
#             json = response.json()
#             remote_song_info = None
#
#             for hit in json['response']['hits']:
#                 if mainArtist.lower() in hit['result']['primary_artist']['name'].lower():
#                     remote_song_info = hit
#                     break
#
#             if remote_song_info:
#                 song_url = remote_song_info['result']['url']
#                 print("-------------------------------------------------------------------------------------------")
#                 finalPrint = "Currently Playing: " + currentTrack + " by " + names[0] + "\n" + scrap_song_url(song_url)
#                 print(finalPrint)
#                 print("-------------------------------------------------------------------------------------------")
#
#             else:
#                 print("-------------------------------------------------------------------------------------------")
#                 print("Stop listening to weeb shit")
#                 print("-------------------------------------------------------------------------------------------")
#         progressBar(progress, duration)
#         time.sleep(1)
#
#
if __name__ == "__main__": main()
