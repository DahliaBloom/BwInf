import argparse
import requests

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--url', type=str)
    arg_parser.add_argument('--number', type=int)
    arg_parser.add_argument('--out', type=str)
    args = arg_parser.parse_args()

    for i in range(args.number):
        url = f'{args.url}{i}.txt'
        print(f'Fetching from {url}')
        data = requests.get(url)
        print(f'Status {data.status_code}')
        with open(f'{args.out}{i}.txt', 'w') as f:
            f.write(data.text)