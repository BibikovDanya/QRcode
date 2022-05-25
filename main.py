import qrcode


def get_qrcode(url='https://typerun.top/#rus_begin', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created. Open the {name}.png'


def main():
    get_qrcode(url=input("URL:"), name =input('name:'))

if __name__ == '__main__':
    main()
