# importing the module
from pytube import YouTube, Playlist


def downloadVideo(_link, _path):
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(_link)
    except Exception as e:
        print("Connection Error", e)  # to handle exception
        exit(1)

    # audioStream = yt.streams.filter(only_audio=True)
    audioStream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

    print(audioStream)
    audioStream.download()

    # YT.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download(AUDIO_FILE_PATH)


def downloadPlaylist(_link, _path):
    print(f'Link: {_link}')
    try:
        p = Playlist(_link)
        print("Total Videos: ", len(p.video_urls))
    except Exception as e:
        print("Connection Error", e)  # to handle exception
        exit(1)

    for video in p.videos:
        print(f'Downloading {video}')
        try:
            video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download()
        except Exception as e:
            video.streams.filter(only_audio=True).order_by('abr').desc().first().download()


if __name__ == '__main__':
    # where to save
    SAVE_PATH = 'C:\\Users\Deepak\Downloads'

    # link of the video to be downloaded
    links = 'https://www.youtube.com/playlist?list=PLAP3oyPRrIVeLif_-fYgQjPB_iATd_pvt'
    downloadPlaylist(links, SAVE_PATH)
