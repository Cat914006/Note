#追加用經緯度找"里"的工能
from geopy.geocoders import Nominatim


def get_nativeland(id, addr, ll):
    try:
        geolocation = Nominatim(user_agent="geotest")
        location = geolocation.reverse(ll)
        arr = str(location).split(',')
        nativeland = ''
        for ar in arr:
            if ar.find('里') != -1:
                nativeland = ar
        print(id, addr, ll, nativeland)
        # 寫一下log
        path = 'C:\python\AddrPX.txt'
        with open(path, 'a') as f:
            f.write(f'{id},{addr},{ll},{nativeland}'+'\n')
            f.close()
    except:
        print(addr, '發生錯誤')
        err = '無法逆地理編碼'
        path = 'C:\python\AddrPX.txt'
        with open(path, 'a') as f:
            f.write(f'{id},{addr},{ll},{err}' + '\n')
            f.close()
        pass
    # return lat, lon


df = pd.read_excel('pxaddr.xlsx')
df = df.reset_index()
for index, row in df.iterrows():
    get_nativeland(row["客編"], row["地址"], row["經緯"])
