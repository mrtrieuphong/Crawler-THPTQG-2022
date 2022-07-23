import requests
import numpy as np
from bs4 import BeautifulSoup, Tag
with open('data.csv', 'w+', encoding='utf-8') as w:
    w.write('TO,NV,SU,DI,VL,HH,SH,NN,GD\n')
    for idx in range(10000001, 99999999):
        page = requests.get("https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/{}.html".format(idx))
        print("[GET] {}/99999999".format(idx))
        soup = BeautifulSoup(page.text, "html.parser")
        parent = soup.find_all("div", {"class": "resultSearch__right"})
        elements = soup.find_all("td")
        n = 2
        elements = [elements[i:i+n] for i in range(0, len(elements), n)]
        to, nv, su, di, vl, hh, sh, ta, gd = '', '', '', '', '', '', '', '', ''
        for element in elements:
            if element[0].text == 'Toán':
                to = element[1].text
            elif element[0].text == 'Văn':
                nv = element[1].text
            elif element[0].text == 'Sử':
                su = element[1].text
            elif element[0].text == 'Địa':
                di = element[1].text
            elif element[0].text == 'Lí':
                vl = element[1].text
            elif element[0].text == 'Hoá':
                hh = element[1].text
            elif element[0].text == 'Sinh':
                si = element[1].text
            elif element[0].text == 'Ngoại ngữ':
                nn = element[1].text
            elif element[0].text == 'GDCD':
                gd = element[1].text
        line = ','.join([to, nv, su, di, vl, hh, sh, ta, gd])
        w.write(line + '\n')
