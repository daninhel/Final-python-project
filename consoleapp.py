from pytube import YouTube , Playlist
from os import system as cmd
from time import sleep as wait

yt = None

def VideoDownloader():
    try:
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        print('Url inválida'), wait(3), cmd('cls')
    
    if yt:
        print(yt.title)
        op = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if op == '1':
            print('Baixando . . .')
            yt = yt.streams.get_highest_resolution()
            yt.download('./midias')
            wait(2), cmd('cls')

def AudioDownloader():
    try:
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        print('Url inválida'), wait(3), cmd('cls')
    
    if yt:
        print(yt.title)
        op = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if op == '1':
            print('Baixando . . .')
            yt = yt.streams.get_audio_only()
            yt.download('./midias')
            wait(2), cmd('cls')

def PlaylistDownloader():
    try:
        yt = YouTube(input('Aviso: para colar só basta clicar com o botão direito do mouse.\nInsira a url do video : '))
        print(yt.title), wait(3), cmd('cls')
    except:
        print('Url inválida'), wait(3), cmd('cls')
    
    if yt:
        print(yt.title)
        op = input('Se deseja baixar esse video digite 1, caso contrario qualquer outra tecla.')
        if op == '1':
            print('Baixando . . .')
            yt = yt.streams.get_highest_resolution()
            yt.download('./midias')
            wait(2), cmd('cls')

def menu():
    print('1 - Baixar video\n2 - Baixar áudio\n3 - Baixar playlist\n4 - Encerrar')
    opcao = input('Insira a opção que correponde a que você deseja : ')

    return opcao

def main():
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