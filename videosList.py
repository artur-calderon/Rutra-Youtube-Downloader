import flet as ft


from youtube import download_video, download_playlist, download_audio
from components.progressBar import ProgressBar

class VideosList(ft.Column):
    def __init__(self, videos_list, urlToDownload):
        super().__init__()
        self.progressBar = ProgressBar()
        
        self.downloadButton = ft.ElevatedButton(text="Baixar")
        self.listVideos = ft.ListView(spacing=10, padding=20, height=500)
        self.downloadPlaylistButtonVideo = ft.ElevatedButton(text="Baixar Playlist Inteira (Vídeo)", visible=False, on_click=  lambda e: download_playlist(urlToDownload,self.progressBar.update_progress))
        self.downloadPlaylistButtonAudio = ft.ElevatedButton(text="Baixar Playlist Inteira (Áudio)", visible=False, on_click=  lambda e: download_audio(urlToDownload,self.progressBar.update_progress))
        
        if videos_list.get("_type") == "playlist":
            # Caso seja uma playlist
            self.downloadPlaylistButtonVideo.visible = True
            self.downloadPlaylistButtonAudio.visible = True
            self.videos_list = []
            
            for video in videos_list["entries"]:
                self.videos_list.append({
                    "id":video.get("id", "ID não disponível"),
                    "title": video.get("title", "Título não disponível"),
                    "thumbnail": video.get("thumbnail", None),
                    "duration": video.get("duration", None),
                    "uploader": video.get("uploader", "Uploader não disponível"),
                })
                        
            for video in self.videos_list: 
                video_id = video["id"]
                self.listVideos.controls.append(ft.Text(value=video["title"]))
                self.listVideos.controls.append(ft.Image(src=video["thumbnail"], width=200, height=200, fit=ft.ImageFit.CONTAIN))
                self.listVideos.controls.append(ft.ElevatedButton(text="Baixar Vídeo", on_click= lambda event , v_id = video_id : download_video(f"https://www.youtube.com/watch?v={v_id}",self.progressBar.update_progress)))
                self.listVideos.controls.append(ft.ElevatedButton(text="Baixar Áudio", on_click= lambda event , v_id = video_id : download_audio(f"https://www.youtube.com/watch?v={v_id}",self.progressBar.update_progress)))
                self.listVideos.controls.append(ft.Divider(height=1, color="white"))
        else:
            # Caso seja um único vídeo
            self.video_info = {
                "title": videos_list["title"],
                "thumbnail":videos_list["thumbnail"],
                "duration": videos_list["duration"],
                "uploader": videos_list["uploader"]
            }
            
            self.listVideos.controls.append(ft.Text(value=self.video_info["title"]))
            self.listVideos.controls.append(ft.Image(src=self.video_info["thumbnail"], width=200, height=200, fit=ft.ImageFit.CONTAIN))
            self.listVideos.controls.append(ft.ElevatedButton(text="Baixar Vídeo", on_click= lambda event : download_video(urlToDownload,self.progressBar.update_progress)))
            self.listVideos.controls.append(ft.ElevatedButton(text="Baixar Áudio", on_click= lambda event : download_audio(urlToDownload,self.progressBar.update_progress)))
            self.listVideos.controls.append(ft.Divider(height=1, color="white"))
            
        self.controls =  [
            ft.Column(
            width=500,
            controls=[
                ft.Row(
                  controls=[
                       self.downloadPlaylistButtonVideo,
                       self.downloadPlaylistButtonAudio
                  ]  
                ),
               self.progressBar,
                self.listVideos
            ]
        )
        ]