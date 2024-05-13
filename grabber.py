#! /usr/bin/python3

banner = r''
import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=30).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://windows.os')
                return
            #os.system(f'wget {url} -O win.txt')
            os.system(f'curl "{url}" > win.txt')
            response = ''.join(open('win.txt').readlines())
            if '.m3u8' not in response:
                print('https://ubuntu.os')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://manifest.googlevideo.com')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U')
print('#EXT-X-INDEPENDENT-SEGMENTS')
#s = requests.Session()
with open('youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            print(f'')
        else:
            grab(line)
            
if 'win.txt' in os.listdir():
    os.system('rm win.txt')
    os.system('rm watch*')
