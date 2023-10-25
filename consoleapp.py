from pytube import YouTube , Playlist
from os import system as cmd
from time import sleep as wait

resolucoes = []
#trabalhar na escolha de resolução

def VideoDownloader() ->None:
    '''
    Baixa em arquvi de vídeo
    '''
    opcao = None
    try:
        cmd('cls')
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a URL do vídeo: '))
        
        print(yt.title)
        wait(3), cmd('cls')
        
        resolucoes = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
        
        while True:
            print("Resoluções disponíveis para download:")
            for i, res in enumerate(resolucoes, start=1):
                print(f"{i} - {res.resolution}")
            try:
                escolha = int(input('Escolha a resolução desejada pelo número correspondente: '))
                if 1 <= escolha <= len(resolucoes):
                    yt = resolucoes[escolha - 1]
                    break
                else:
                    cmd('cls')
                    print("Escolha inválida. Digite o número correspondente à resolução desejada.")
                    wait(3), cmd('cls')
            except:
                cmd('cls'),print("Escolha inválida. Digite o número correspondente à resolução desejada."),wait(3),cmd('cls')
                
        cmd('cls'),print(yt.title)
        try:
            opcao = input('Se deseja baixar esse vídeo, digite 1; caso contrário, pressione qualquer outra tecla: ')
        except KeyboardInterrupt:
            ...
        
        if opcao == '1':
            cmd('cls'), print('Baixando . . .')
            yt.download('./midias')
            print('Baixado!'),wait(2), cmd('cls')
        else:
            print('Vídeo não baixado,voltando para o menu principal. . .'),wait(3),cmd('cls')
        
    except:
        cmd('cls'), print('Url inválida'),wait(3), cmd('cls')

def AudioDownloader() -> None:
    '''
    Baixa em arquvio de áudio
    '''
    opcao = None
    try:
        cmd('cls')
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
        
        cmd('cls'), print(yt.title)
        
        try:
            opcao = input('Se deseja baixar o áudio desse vídeo digite 1, caso contrario qualquer outra tecla.')
        except:
            ...
            
        if opcao == '1':
            cmd('cls'), print('Baixando . . .')
            yt = yt.streams.get_audio_only()
            yt.download('./midias')
            print('Baixado!'),wait(2), cmd('cls')

        else:
            print('Vídeo não baixado,voltando para o menu principal. . .'),wait(3),cmd('cls')
    except:
        cmd('cls'),print('Url inválida'), wait(3), cmd('cls')

def PlaylistDownloader() -> None:
    '''
    Baixa as playlists
    '''
    playlist = None
    opcao = None
    try:
        cmd('cls')
        playlist = Playlist(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url da playlist : '))
        
        cmd('cls'), print(playlist.title)
        try:
            opcao = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        except KeyboardInterrupt:
            ...
        
        if opcao == '1':
            cmd('cls'), print('Baixando . . .')
            for video in playlist.videos:
                video.streams.first().download(f'./midias/{playlist.title}')
                
            print('Baixado!'),wait(2), cmd('cls')
        else:
            print('Vídeo não baixado,voltando para o menu principal. . .'),wait(3),cmd('cls')
    except:
        cmd('cls'),print('Url inválida'), wait(3), cmd('cls')

def menu() -> str:
    '''
    Exibe o menu de inicio e retorna a opção escolhida pelo usuário
    '''
    opcao = None
    print('PyTube Downloader\n1 - Baixar vídeo\n2 - Baixar áudio\n3 - Baixar playlist\n4 - Encerrar')
    try:
        opcao = input('Insira a opção que correponde a que você deseja : ')
    except KeyboardInterrupt:
        ...
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