import yt_dlp

# from components.progressBar import ProgressBar 

# from components import progressBar


# def getProgress(status):
#     progress = ProgressBar()
#     progress.update_progress(status)

downloader = yt_dlp

optionforGetInfo = {
    
}

def download_video(url,getProgress):
    optionForDownload = {
        'progress_hooks':[getProgress],
        'outtmpl':'Rutra Downloader/%(title)s.%(ext)s',
        'ffmpeg_location':'C:/Program Files/ffmpeg/bin',
        'ffprobe_location':'C:/Program Files/ffmpeg/bin',
    }
    with downloader.YoutubeDL(optionForDownload) as youtube:
        youtube.download([url])
        
def get_video_info(url):
    with downloader.YoutubeDL(optionforGetInfo) as ydl:
        info = ydl.extract_info(url, download=False)
    return info        

def download_playlist(url, getProgress):
    ydl_opts = {
        'progress_hooks':[getProgress],
        'outtmpl': 'Rutra Downloader/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'ffmpeg_location':'C:/Program Files/ffmpeg/bin',
        'ffprobe_location':'C:/Program Files/ffmpeg/bin',
    }
    with downloader.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url, getProgress):
    ydl_opts = {
    'progress_hooks':[getProgress],
    'outtmpl':'Rutra Downloader/%(title)s.%(ext)s',
    'format': 'mp3/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location':'C:/Program Files/ffmpeg/bin',
    'ffprobe_location':'C:/Program Files/ffmpeg/bin',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
