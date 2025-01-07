import flet as ft
import yt_dlp


class ProgressBar(ft.Row):
    def __init__(self):
        super().__init__()
        self.progressBar  = ft.ProgressBar(width=400, value=0.0)
        self.fileName = ft.Text(value="")
        self.status = ft.Text(value="")
        self.percent = ft.Text(value="")
        self.tempoRestante = ft.Text(value="")
        self.stopDownload = False
        
        self.fecharModalButton = ft.Button(text="Fechar", on_click=lambda e: close(), visible=False)
        self.stopDownloadButton = ft.Button(text="Parar Download", on_click=lambda e: stop_download(), visible=False)
        
        self.modalProgress = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                height=200,
                controls=[
                    self.fileName,
                    self.progressBar,
                    ft.Column(
                        controls=[
                            self.percent,
                            self.status,
                            self.tempoRestante
                        ]
                    )
                ]
            ),
            actions=[
               self.fecharModalButton,
               self.stopDownloadButton
            ]
        )
        def close():
            self.modalProgress.open = False
            self.update()
        
        def stop_download():
            self.stopDownload = True
            self.update()    
        
        self.controls = [
            ft.Column(
                controls= [
                    self.modalProgress
                ]
            )
        ]
      
    def update_progress(self, status):
        self.status.value = f"Status: {status['status']}"
        if status['status'] == 'downloading':
            percent = float(status['_percent_str'].strip('%')) / 100
            self.stopDownloadButton.visible = True
            self.progressBar.value = percent
            self.fileName.value = status['filename']
            self.percent.value = f"Progresso: {status['_percent_str']}"
            self.tempoRestante.value = f"Tempo restante: {status['_eta_str']}"
            self.fecharModalButton.visible = True
            self.modalProgress.open = True
        elif self.stopDownload:
            self.status.value = "Download Cancelado"
            raise yt_dlp.DownloadError("Download Cancelado")
        elif status['status'] == 'post_process':
        # Pós-processamento (extração/conversão de áudio)
            self.status.value = "Processando o áudio..."
            self.percent.value = "Progresso: Pós-processamento"
            self.tempoRestante.value = "Tempo restante: N/A"
        self.update()
        
    
        
       
        
    