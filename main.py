import flet as ft

from youtube import download_video, get_video_info
from downloader import Downloader
from components.progressBar import ProgressBar

def main(page: ft.Page):
   #TODO: Adicionar Progress Bar
   # Adicionar opção de download de audio
   # Adicionar configuração de qual pasta salvar
   
   page.title = "Rutra Youtube Downloader"
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.window.width = 500
   page.window.resizable = False
   page.update()

   downloaderApp = Downloader()
   
   page.add(downloaderApp)
       
   
ft.app(main)


# https://www.youtube.com/watch?v=NdBEQbDmjus&list=PLQjdqucc2geA4XHbSHJgj8jPGYuYu594X
# https://www.youtube.com/watch?v=zrH6Y6JYS4k