import webview

video = {
    'url': 'https://youtu.be/3Wo4L2dPS58',
    'title': '',
    'thumbnail': '',
}


def main():
    webview.create_window('Youtube Downloader', './index.html')
    webview.start()

if __name__ == '__main__':
    main()