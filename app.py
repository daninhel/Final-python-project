import webview
from pytube import YouTube
from os import system as cmd
from time import sleep as wait

video = {
    'url': 'https://youtu.be/3Wo4L2dPS58',
    'title': '',
    'thumbnail': '',
}

def YtDownload():
    # Obtém o valor do campo de entrada no HTML
    #video['url'] = webview.evaluate_js('document.getElementById("floatingInput").value')
    while True:
        print('1 - Baixar video\n2 - Baixar audio\n3 - Encerrar')
        op = None
        try :
            op  = input('Insira o numero que correponde a opção que deseja : ')
        except:
            ...
            
        if op == '1':
            cmd('cls')
            while True:
                try :
                    video['url'] = input('Insira a url do video : \nOu Ctrl + C para voltar.')
                except KeyboardInterrupt:
                    break
            
                if video['url']:
                    try:
                        youtube = YouTube(video['url'])
                        video['title'] = youtube.title
                        print(f'Título do vídeo: {video["title"]}')
                        op = input('Deseja')
                        if op == '':
                            youtube.streams.get_highest_resolution().download()
                        else:
                            ...
                    except Exception as e:
                        print(f"Erro ao obter informações do vídeo: {str(e)}"),wait(3),cmd('cls')
                        continue
                else:
                    print("Por favor, insira uma URL válida."), wait(3), cmd('cls')
                    continue
        elif op == '2':
            ...
        elif op == '3':
            break
        else:
            print('Opção inválida.')
            ...

def main():
    webview.create_window('Youtube Downloader', './index.html')
    webview.start()

if __name__ == '__main__':
    #main()
    YtDownload()
    ...