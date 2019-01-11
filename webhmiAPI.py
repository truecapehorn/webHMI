import requests

device_adress = 'http://80.50.4.62:60043'
#wifi_name = "BigBang"
#wifi_pwd = "501195121"


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 140 * '-' + '\n')
    print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url,r.apparent_encoding))
    print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
    print('* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))  # HTTP
    print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
    print('<!---------koniec-----------!>')






def devive_uptime():
    '''
        Popbranie danych połaczenia
    '''
    #action = 'Device - Get device uptime'
    # ADRESS
    api_adress = '/api / connections'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
   #response_status(action, r)

device_adress()


