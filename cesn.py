import numpy as np
import matplotlib.pyplot as plt
import random, math
import webbrowser, requests, bs4, sys

def get_data(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('ERROR:{}'.format(exc))
    soup = bs4.BeautifulSoup(res.content, "html.parser")
    cnt = 0
    flg = 0
    rps = []
    for elems in soup.find_all("td"):
        if cnt == 4:
            if flg == 1:
                if elems.text == 'グー':
                    rps.append(1)
                elif elems.text == 'チョキ':
                    rps.append(2)
                elif elems.text == 'パー':
                    rps.append(3)
            else:
                flg = 1
        cnt += 1
        if cnt == 6: cnt = 0

    return rps


def f(x):
    ep = 0.3
    return 1/(1+np.exp(-x/ep))

N = 10000
sp, rho = 0.3, 0.999
k, a, th = 0.9, 1, 0.2

#u = np.matrix(np.array([0.49]).reshape((1, 1)))
#for i in range(T):
#    u = np.append(u, 4*u[i]*(1-u[i]), axis=0)
#d = u[1:,0].T

tr = get_data('http://park11.wakwak.com/~hkn/result1996.htm')
u = np.matrix(np.array(tr).reshape((len(tr), 1)))
tr = get_data('http://park11.wakwak.com/~hkn/result1997.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result1998.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result1999.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2000.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2001.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2002.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2003.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2004.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2005.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2006.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2007.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2008.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2009.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2010.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2011.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2012.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2013.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2014.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2015.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2016.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2017.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2018.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
tr = get_data('http://park11.wakwak.com/~hkn/result2019.htm')
u = np.append(u, np.matrix(np.array(tr).reshape((len(tr), 1))), axis=0)
d = (u[1:,0].T)/3
u = u[0:-1,0]/3

T = len(u)

win = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
win[win >= 1-sp] = 1
win[win < sp] = -1
win[(win < 1) & (win > -1)] = 0

x = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
y = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
w = np.matrix(np.array([1+(random.random()-1)/sp for _ in range(N**2)]).reshape(N, N))
w[w < 0] = 0
la, v = np.linalg.eig(w)
w = rho * w / abs(la[np.argmax(la)])
w = w - np.multiply(np.diag(w) + a*np.array([1 for _ in range(N)]), np.eye(N))

yout = np.matrix(np.array([0]).reshape(1, 1))
wout = np.matrix(np.array([random.random() for _ in range(N)]).reshape(1, N))

for i in range(T-1):
    x = np.append(x, k*x[:,i] + np.dot(w, y[:,i]) + th + np.dot(win, u[i]), axis=1)
    y = np.append(y, f(x[:,i+1]), axis=1)

wout = np.dot(np.dot(d, y.T), np.linalg.pinv(np.dot(y, y.T)))

yout = np.dot(wout, y)
plt.plot(d.T)
plt.plot(yout.T)
plt.show()

'''
#u = np.matrix(np.array([random.random()]).reshape((1, 1)))
#for i in range(T):
#    u = np.append(u, 4*u[i]*(1-u[i]), axis=0)
#d = u[1:,0].T

te = get_data('http://park11.wakwak.com/~hkn/result2020.htm')
u = np.matrix(np.array(te).reshape((len(te), 1)))
d = (u[1:,0].T)/3
u = u[:-1,0]/3

x = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
y = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))

T = len(u)

for i in range(T-1):
    x = np.append(x, k*x[:,i] + np.dot(w, y[:,i]) + th + np.dot(win, u[i]), axis=1)
    y = np.append(y, f(x[:,i+1]), axis=1)
    yout = np.append(yout, np.dot(wout, y[:,i+1]), axis=0)

plt.plot(d[:,-12:].T, marker='x')
plt.plot(yout[-12:,:], marker='o')
plt.show()
'''