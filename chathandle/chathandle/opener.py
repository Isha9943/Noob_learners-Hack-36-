import os
import time


# tic = time.perf_counter()
# toc = time.perf_counter()
# print(f'{toc-tic:0.4f}')

def mod(x,y):
    globals()[x](y)


class opener:

    def __init__(self,appnm):
        self.appnm = appnm[0].lower()
        self.loca = [r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs',r'C:\Users\Dharma\AppData\Roaming\Microsoft\Windows\Start Menu\Programs']
        # os.startfile(r'shell:AppsFolder')
        self.cd = 0
        self.applist = self.loca[self.cd]
        self.apps = {}
        self.uninstallers = {}
        self.open()

    def refetch(self):
        for pathh,sub,files in os.walk(self.applist):
            for i in files:
                if 'ninstall' not in i:
                    self.apps[i] = os.path.join(pathh,i)
                else:
                    self.uninstallers[i] = os.path.join(pathh, i)
    def open(self):
        self.refetch()
        self.appnm.lower()
        temp = {}
        for i in self.apps:
            k = i.lower()
            if self.appnm in k:
                temp[i] = self.apps.get(i)
        l = sorted(temp)
        if len(temp) == 1:
            pass
            os.startfile(self.apps.get(l[0]))
        elif len(temp) == 0:
            try:
                self.cd +=1
                self.applist = self.loca[self.cd]
                self.open()
            except:
                print('Not found')
        else:
            print('Which file do you need to open ?')
            d = 0
            for i in l:
                print(f'{d} . {i}')
                d += 1
            t = int(input('Enter '))
            os.startfile(self.apps.get(l[t]))
    def paral(self):
        l = ['appname']
        return l

