import subprocess

while True:
    site = input('Введите адрес сайта:\n')
    if site == 'end':
        break

    if 'http://' in site:
        subprocess.Popen(['open', site])
    elif 'www.' in site:
        site = 'http://' + site
        subprocess.Popen(['open', site])
    else:
        site = 'http://www.' + site
        subprocess.Popen(['open', site])
