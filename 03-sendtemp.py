from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def Temperature(pid):
    
    url = 'https://www.tmd.go.th/province.php?id={}'.format(pid)
    webopen = req(url) #เปิดเว็บโดยไม่เปิด web browser
    page_html = webopen.read() #code html ไปใช้งานต่อ
    webopen.close()
    data = soup(page_html,'html.parser') #แปลงเป็น soup
    #print(type(data))
    '''
    <TD width='100%' align='left' style='FONT-SIZE:40px;
    color: #F6E207; padding-left:25px;'
    class='strokeme'>28.2 &deg;C</TD>
    '''
    # <span class="title" >&nbsp;กรุงเทพมหานคร</span>
    province = data.find_all('span',{'class':'title'})
    province = province[0].text
    province = province.strip()

    temp = data.find_all('td',{'class':'strokeme'})
    temp = temp[0].text # .text เป็นคำสั่งที่ใช้ในการตัด tag ออก

    #print(province, temp)
    return 'จังหวัด: {} อุณหภูมิ: {}'.format(province,temp)


alltext = '' #เอาไว้สะสมข้อความ
for i in range(20,40):
    #สั่งรันตัวเลช 1-10 ออกมาเพื่อเป็น ID ของจังหวัด
    try:
        text = Temperature(i) #เช็คอุณหภูมิ
        alltext = alltext + text + '\n' #เอาผลลัพท์ที่เช็คได้ไปบวกกับค่าเก่า
    except:
        print('Not found')

print(alltext)
# ได้ข้อความทั้งหมดแล้วก็ทำการส่ง Line
from songline import Sendline
token = 'xm4K7kqtfU1yfybWQUm2GDLhxZYOeVAQCoUeYMpK7HP'
messenger = Sendline(token)
messenger.sendtext(alltext)












