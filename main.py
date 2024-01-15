import os, sys, platform
os.system('rm -rf LogoSak.cpython.so')

try:
    os.system ('rm -rf LogoSak.cpython.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile ('LogoSak.cpython.so'):
        os.system('curl -L https://github.com/OliverKH12/today/blob/main/LogoSak.cpython.so?raw=true -o LogoSak.cpython.so ')
        import LogoSak
    else:
        import LogoSak
        