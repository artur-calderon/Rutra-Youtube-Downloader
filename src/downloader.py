import flet as ft
import threading


from youtube import get_video_info
from videosList import VideosList

class Downloader(ft.Column):
    def __init__(self):
        super().__init__()
        self.welcomeText = ft.Text(value='Bem vindo ao Rutra Youtube Downloader')
        self.search_bar = ft.TextField(label="Enter YouTube video URL", expand=True, color="white", icon=ft.Icons.SEARCH_ROUNDED)
        self.list = ft.Column()
        self.loading = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                alignment=ft.CrossAxisAlignment.CENTER,
                height=100,
                controls=[
                    ft.Text(value='Verificando link...'),
                    ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
                ]
            )
            
            
            
        )
        
        def click(e):
            if not self.search_bar.value:
                self.search_bar.error_text = "Insira uma URL"
                self.update()
                return        
            self.list.controls.clear()
            self.url = self.search_bar.value
            self.loading.open = True
            self.update()
            
            threading.Thread(target=fetch_video_info).start()
            
        def fetch_video_info():    
            try:
                self.info = get_video_info(self.url)
                list = VideosList(self.info, self.url)
                self.list.controls.append(list)
            except Exception as e:
                self.search_bar.error_text = f"Erro: {str(e)}"    
            finally:
                self.loading.open = False
                self.update()
        
        
        self.controls = [
            ft.Column(
                width = 500,
                controls=[
                    self.welcomeText,
                    ft.Row(
                        controls=[
                            self.search_bar,
                            ft.ElevatedButton(text="Pesquisar", on_click=click),
                        ]
                    ),
                    self.loading,
                    self.list,
                    
                ]
            )
        ]