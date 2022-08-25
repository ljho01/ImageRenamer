import exifread
import os


print('Image Renamer for (JPG, JPEG, PNG, HEIC)')
folderpath = "./" + input("이미지 파일이 있는 폴더명을 입력해주세요: ")
img_all = 0
img_mod = 0
for p in os.listdir(folderpath):
    filepath = folderpath + f"/{p}"
    if os.path.isfile(filepath):
        if p[p.index('.')+1:].upper() in ['JPG', 'JPEG', 'HEIC', 'PNG']:
            mod = True
            img_all += 1
            with open(filepath, 'rb') as f:
                tags = exifread.process_file(f)
                n_filepath = None
                if 'EXIF DateTimeOriginal' in tags:
                    n_filepath = str(tags['EXIF DateTimeOriginal']).replace(':', '').replace(' ', '_')
                elif 'EXIF DateTimeDigitized' in tags:
                    n_filepath = str(tags['EXIF DateTimeDigitized']).replace(':', '').replace(' ', '_')
                elif 'Image DateTime' in tags:
                    n_filepath = str(tags['Image DateTime']).replace(':', '').replace(' ', '_')
                else:
                    mod = False
                    print(f'E{img_all-img_mod}: {filepath} 이미지에 적용할 날짜가 없습니다.')
            if n_filepath is not None:
                os.rename(filepath, folderpath + f"/{n_filepath}_" + str(img_mod).zfill(4) + p[p.index('.'):])
                print(filepath, 'to',folderpath + f"/{n_filepath}_" + str(img_mod).zfill(4) + p[p.index('.'):])
                img_mod += 1
print(f'{img_all}개의 이미지 중 {img_mod}개를 수정했습니다.')
