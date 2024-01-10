import os
import humanfriendly

def search_folder(location, min_filesize):
    for folder, subfolders, filenames in os.walk(location):
        for filename in filenames:
            try:
                size_bytes = os.path.getsize(os.path.join(folder, filename))
                if min_filesize * 1024 ** 2 <= size_bytes:
                    yield filename, size_bytes
            except FileNotFoundError:
                print('bummer file not found')
                # maybe log error, maybe `pass`, maybe raise an exception
                # (halting further processing), maybe return an error object

if __name__ == '__main__':
    print('This program searches for ...')

    location='.'
    filesize=50
    print('Files larger than %d MB in location: %s' % (filesize, location))
    for filename, size in search_folder(location, filesize):
        friend_size = humanfriendly.format_size(size)            
        print(filename,friend_size)
