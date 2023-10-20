from pytube import YouTube , Playlist
from os import system as cmd
from time import sleep as wait

yt = None
resolucao = []
#trabalhar na escolha de resolução

def VideoDownloader():
    try:
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        cmd('cls'),print('Url inválida'), wait(3), cmd('cls')

    
    if yt:
        cmd('cls'), print(yt.title)
        opcao = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if opcao == '1':
            print('Baixando . . .')

            yt = yt.streams.get_highest_resolution()
            yt.download('./midias')
            wait(2), cmd('cls')

def AudioDownloader():
    '''
    Baixa em arquvio de áudio
    '''
    try:
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        cmd('cls'),print('Url inválida'), wait(3), cmd('cls')
    
    if yt:
        cmd('cls'), print(yt.title)
        opcao = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if opcao == '1':
            print('Baixando . . .')
            yt = yt.streams.get_audio_only()
            yt.download('./midias')
            wait(2), cmd('cls')

def PlaylistDownloader():
    '''
    Baixa as playlists
    '''
    playlist = None
    try:
        playlist = Playlist(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url da playlist : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        cmd('cls'),print('Url inválida'), wait(3), cmd('cls')
    
    if p:
        cmd('cls'), print(p.title)
        opcao = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if opcao == '1':
            print('Baixando . . .')
            for video in playlist.videos:
                video.streams.first().download('./midias')
                
            wait(2), cmd('cls')

def menu() -> None:
    '''
    Exibe o menu de inicio
    '''
    print('PyTube Downloader\n1 - Baixar video\n2 - Baixar áudio\n3 - Baixar playlist\n4 - Encerrar')
    opcao = input('Insira a opção que correponde a que você deseja : ')

    return opcao

def main() -> None:
    cmd('cls')
    op = menu()
    match op:
        case '1':
            VideoDownloader()
            main()
        case '2':
            AudioDownloader()
            main()
        case '3':
            PlaylistDownloader()
            main()
        case '4':
            print('Encerrando . . .')
        case _:
            print('Opção inválida'),wait(3),cmd('cls')
            main()

if __name__ == '__main__':
    main()