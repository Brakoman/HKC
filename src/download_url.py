import urllib2

def download_url_files():
    print "\033[1;31mNOTE : \033[1;37mGUNAKAN HTTP!\n"
    file_url=raw_input('\033[1;35m[?] URL tempat files  : \033[1;33m')
    filedata=urllib2.urlopen(file_url)
    datawrite=filedata.read()
    file_save=raw_input('\033[1;35m[?] TEMPAT FILE      : \033[1;33m')
    with open(file_save,'wb') as f:
        f.write(datawrite)
    print "[+] BERHASIL!\n"
