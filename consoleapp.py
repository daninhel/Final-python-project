from pytube import YouTube
from os import system as cmd
from time import sleep as wait

video = {
    'url': 'https://youtu.be/3Wo4L2dPS58',
    'title': '',
    'thumbnail': '',
}

def VideoDownload():
                try :
                    video['url'] = input('Insira a url do video : \nOu Ctrl + C para voltar.')
                except KeyboardInterrupt:
                    ...
            
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
                        
                else:
                    print("Por favor, insira uma URL válida."), wait(3), cmd('cls')
                    

def opcao():
    a = None
    try :
        a  = input('Insira o numero que correponde a opção que deseja : ')
    except:
        ...
        
    return a

def AudioDownload():
    ...
    
def main():
    print('1 - Baixar video\n2 - Baixar audio\n3 - Encerrar')

if __name__ == '__main__':
    main()
    op = opcao()
    
    match op:
        case '1':
            VideoDownload()
            main()
        case '2':
            AudioDownload
            main()
        case '3':
            print('Encerrando . . .')
        case _:
            print('Opção inválida.')
            ...