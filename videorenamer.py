import ffmpeg
import os
from datetime import datetime, timedelta


print('Video Renamer for (MOV, MP4)')
folderpath = "./" + 'Google'
vid_all = 0
vid_mod = 0
for p in os.listdir(folderpath):
    filepath = folderpath + f"/{p}"
    if os.path.isfile(filepath):
        if p[p.index('.')+1:].upper() in ['MOV', 'MP4']:
            n_filepath = None
            vid_all += 1
            try:
                rawdate = ffmpeg.probe(filepath)['streams'][0]['tags']['creation_time']
                rawdate_dt = datetime.strptime(rawdate, "%Y-%m-%dT%H:%M:%S.%fZ")
                moddate_dt = rawdate_dt + timedelta(hours=9)
                moddate = str(moddate_dt).replace('-', '').replace(' ', '_').replace(':', '')
                vid_mod += 1
                n_filepath = folderpath + f"/{moddate}_" + str(vid_mod).zfill(4) + p[p.index('.'):]
                os.rename(filepath, n_filepath)
            except Exception as e:
                print(f"{p} 파일에서 문제 발생: {e}")
print(f'{vid_all}개의 비디오 중 {vid_mod}개를 수정했습니다.')