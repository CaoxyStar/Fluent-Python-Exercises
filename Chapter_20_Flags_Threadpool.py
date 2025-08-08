from concurrent import futures
from Chapter_20_Flags import save_flag, get_flag, main

def download_one(cc):
    image = get_flag(cc)
    save_flag(image, cc.lower() + '.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list):
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))

if __name__ == '__main__':
    main(download_many)
