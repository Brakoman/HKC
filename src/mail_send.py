from colorama import init,AnsiToWin32
init()

import smtplib
from email.mime.text import MIMEText
import sys

def send_mail2(smtp_ssl_host,port_ssl):
    print "\033[1;32m[*] \033[1;37mSistem berhasil menuju Host!"
    print "\n\033[1;35mANDA HARUS LOGIN DULU EMAIL NYA!!! :D"
    username=raw_input('\033[1;34m      EMAIL adr : \033[1;37m')
    password=raw_input('\033[1;34m      PASSOWRD  : \033[1;31m')
    from time import sleep as s
    s(2)
    victims=raw_input('\033[1;35m      SUBJEK EMAIL: \033[1;34m')
    target=[
        username,
        victims
        ]
    print "\n\033[1;36m[INFO] Masukan pesan anda "
    msgs=raw_input('\033[1;32m')
    msg_subject=raw_input('\033[1;32m     SUBJECT   : \033[1;31m')

    msg=MIMEText(msgs)
    msg['Subject']  = msg_subject
    msg['From']     = username
    msg['To']       = ', '.join(target)
    print "\033[1;33m[+] MENGIRIM..."
    try:
        server=smtplib.SMTP_SSL(smtp_ssl_host,port_ssl)
        server.login(username,password)
        server.sendmail(victims,target,msg.as_string())
        server.quit()
        print "\033[1;34m[*] \033[1;37mBERHASIL TERKIRIM!"
    except:
        print "\033[1;31m[!] \033[1;37mKESALAHAN TERDETEKSI"

def send_mailfail():
    smtp_ssl_host='smtp.gmail.com'
    smtp_ssl_port=465
    username=raw_input('\033[1;34m      EMAIL adr : \033[1;37m')
    password=raw_input('\033[1;34m      PASSOWRD  : \033[1;31m')
    sender=username
    target=raw_input('\033[1;34m       TARGET email : \033[1;37m')
    targets=[
        sender,target
        ]
    print "\n\033[1;36m[INFO] Masukan pesan anda "
    msgs=raw_input('\033[1;32m')
    msg_subject=raw_input('\033[1;32m     SUBJECT   : \033[1;31m')
    msg=MIMEText(msgs)
    msg['Subject']  = msg_subject
    msg['From']     = sender
    msg['To']       = ', '.join(targets)
    print "\033[1;33m[+] MENGIRIM..."
    try:
        server=smtplib.SMTP_SSL(smtp_ssl_host,port_ssl)
        server.login(username,password)
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
        print "\033[1;34m[*] \033[1;37mBERHASIL TERKIRIM!"
    except:
        print "\033[1;31m[!] \033[1;37mKESALAHAN TERDETEKSI"

def Send_Email():
    pilihan=raw_input('\033[1;34m[?] \033[1;37m Host yang anda pakai : ')
    port_mu=raw_input('\033[;34m[?] \033[1;37m Port mu              : ')
    print "\033[1;33m[+] \033[1;37mMenghubungkan...."
    try:
        smtp_ssl_host=pilihan
        port_ssl=port_mu
        send_mail2(smtp_ssl_host,port_ssl)
    except:
        print "\033[1;31m[!] \033[1;37mSepertinya host dan port anda salah"
        yorno=raw_input('\033[1;34m[?] \033[1;37Apakah anda mau mencoba sistem dari saya [y/n] ')
        if yorno=='y' or yorno=='Y':
            send_mailfail
        else:
            sys.exit()
