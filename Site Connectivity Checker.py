import urllib.request as urllib


def main(url):
    print('Checking connectivity...')

    response = urllib.urlopen(url)
    print(f'Connected to {url} succesfully.')
    print(f'The response code was: {response.getcode()}.')


input_url = input('\nEnter the site url or Exit (x): ')
if input_url.lower() == 'X'.lower():
    print('Program Closed.\n')
    exit()
else:
    main(input_url)