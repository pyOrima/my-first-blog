import numpy as np
import random, math
import webbrowser, requests, bs4, sys

def predict():

    def f(x):
        ep = 0.5
        return 1/(1+np.exp(-x/ep))

    def get_data(url):
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('ERROR:{}'.format(exc))
        soup = bs4.BeautifulSoup(res.content, "html.parser")
        cnt = 0
        flg = 0
        rps = [[], [], []]
        for elems in soup.find_all("td"):
            if cnt == 4:
                if flg == 1:
                    if elems.text == 'グー':
                        rps[0].append(1)
                        rps[1].append(0)
                        rps[2].append(0)
                    elif elems.text == 'チョキ':
                        rps[0].append(0)
                        rps[1].append(1)
                        rps[2].append(0)
                    elif elems.text == 'パー':
                        rps[0].append(0)
                        rps[1].append(0)
                        rps[2].append(1)
                else:
                    flg = 1
            cnt += 1
            if cnt == 6: cnt = 0

        return rps

    tr = get_data('http://park11.wakwak.com/~hkn/result1996.htm')
    u_tr = np.matrix(np.array(tr))
    tr = get_data('http://park11.wakwak.com/~hkn/result1997.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result1998.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result1999.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2000.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2001.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2002.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2003.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2004.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2005.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2006.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2007.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2008.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2009.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2010.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2011.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2012.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2013.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2014.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2015.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2016.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2017.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2018.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)
    tr = get_data('http://park11.wakwak.com/~hkn/result2019.htm')
    u_tr = np.append(u_tr, np.matrix(np.array(tr)), axis=1)

    te = get_data('http://park11.wakwak.com/~hkn/result2020.htm')
    u_te = np.matrix(np.array(te))

    N = 30
    sp, rho = 0.2, 0.9
    best = 0
    for t in range(1000):
        d = u_tr[:,1:]
        u = u_tr[:,:-1]
        T = len(u.T)

        win = np.matrix(np.array([random.random() for _ in range(N*3)]).reshape(N, 3))
        win[win >= 1-sp] = 1
        win[win < sp] = -1
        win[(win < 1) & (win > -1)] = 0

        x = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
        w = np.matrix(np.array([1+(random.random()-1)/sp for _ in range(N**2)]).reshape(N, N))
        w[w < 0] = 0
        la, v = np.linalg.eig(w)
        w = rho * w / abs(la[np.argmax(la)])

        y = np.matrix(np.array([random.random() for _ in range(3)]).reshape(3, 1))
        wout = np.matrix(np.array([random.random() for _ in range(N*3)]).reshape(3, N))


        for i in range(T-1):
            x = np.append(x, f(np.dot(w, x[:,i]) + np.dot(win, u[:,i])), axis=1)

        wout = np.dot(np.dot(d, x.T), np.linalg.pinv(np.dot(x, x.T)))

        d = u_te[:,1:]
        u = u_te
        T = len(u.T)

        x = np.matrix(np.array([random.random() for _ in range(N)]).reshape(N, 1))
        pre = []

        for i in range(T):
            x = np.append(x, f(np.dot(w, x[:,i]) + np.dot(win, u[:,i])), axis=1)
            y = np.append(y, np.dot(wout, x[:,i+1]), axis=1)
            if y[0,i+1] > y[1,i+1] and y[0,i+1] > y[2,i+1]:
                pre.append(1)
            elif y[1,i+1] > y[0,i+1] and y[1,i+1] > y[2,i+1]:
                pre.append(2)
            elif y[2,i+1] > y[0,i+1] and y[2,i+1] > y[1,i+1]:
                pre.append(3)
            else:
                pre.append(0)

        ans = 1*d[0,:] + 2*d[1,:] + 3*d[2,:]

        cnt = 0
        for i in range(T-1):
            if ans[0,i] == pre[i]:
                cnt += 1
        if cnt > best:
            pre_best = pre
            best = cnt
    rslt = document["result"]
    rslt.text = pre
    #print(best/T*100, '%')