import webbrowser, requests, bs4, sys

res = requests.get('http://park11.wakwak.com/~hkn/result2020.htm')

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

print(rps)