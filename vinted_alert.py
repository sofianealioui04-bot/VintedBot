import requests, schedule, time
 
# ─── MODIFIE CES 3 VALEURS ───────────────────────────
BOT_TOKEN  = "8981011090:AAEzR1kuIMYRQsZI9fQq4j5oN4SCg6QWxJ0"
CHAT_ID    = "5322714033"
COOKIE_STR = "v_udt=UlRVTDVKL1JtL0xBeWxyaUpOUWcycTBIN3BRVi0tMFdqV2dmeUZLVlYrUjU3RC0tUkJ4WWFCL01ZUElWVVMwY0ZhNmIzdz09; anonymous-locale=fr; anonymous-iso-locale=fr-FR; non_dot_com_www_domain_cookie_buster=1; is_shipping_fees_applied_info_banner_dismissed=false; OptanonAlertBoxClosed=2026-05-21T08:55:32.267Z; eupubconsent-v2=CQkjdTAQkjdTAAcABBFRCfFgAAAAAEPgAAwIAAAWZABMNDogjLIgECBQEAIEACgrCACgQBAAAkBRAQAmDAhyBgAusIkAIAUAAwQAgABBgACAAASABCIAIACAQAgQCBQABgAQBAQAMDAAGAChEAgABAdAxTAggECwASIyoDTAhAASCAlsqEEgCBBXCFIscAggREwUAAAIABQAAAD4WAhJKCViQQBcQXQAIAAAAUQIMCKQswBBQGaLQVgScBkaYAkeYJElOgiAJghIyDIhNUEg8UxRAAAA.YAAACHwAAAAA.ILNtR_G__bXlv-Tb36bpkeYxf99hr7sQxBgbIsm4FzLvW7JwC32EbNEzatiYKmRIAu3TBIQNtHIjURUChKIgVrzDsaEyUoTtKJ-BkiDMRY2JQCFxvm4pjWQCZ4ur_50d9mR-N7dr-2dzyy5hnv3a9fuS1UJicKYetHfn8ZBKT-_IU9_x-_4v4_MbpEm8eS1v_tGtt43c64tP_dpuxt-Tyffzfv_f72_e7X__c__33_-qXX_r7_4A; OTAdditionalConsentString=2~~dv.20.43.55.57.61.70.83.89.93.108.117.122.124.135.143.144.147.149.159.161.184.192.196.211.228.230.236.239.255.259.266.272.286.291.311.313.314.320.322.323.327.358.367.370.371.385.407.415.424.429.430.436.445.469.486.491.494.495.522.523.540.550.560.568.574.576.584.587.591.621.723.737.797.798.803.820.827.839.864.899.904.922.938.955.959.979.981.985.986.1003.1027.1031.1033.1046.1047.1048.1051.1053.1067.1092.1095.1097.1099.1107.1109.1126.1135.1143.1149.1152.1162.1166.1186.1188.1192.1205.1215.1220.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1329.1342.1345.1356.1365.1403.1415.1416.1419.1421.1423.1440.1449.1455.1495.1512.1514.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1598.1603.1616.1638.1651.1653.1659.1660.1667.1677.1678.1682.1697.1699.1703.1712.1716.1720.1721.1725.1732.1735.1745.1750.1753.1765.1782.1786.1800.1808.1810.1825.1827.1832.1838.1840.1843.1845.1859.1870.1878.1880.1882.1889.1898.1911.1917.1928.1929.1942.1944.1958.1962.1963.1964.1967.1968.1969.1978.1985.1987.2003.2027.2035.2038.2039.2044.2047.2052.2056.2064.2068.2069.2072.2074.2084.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2141.2147.2156.2166.2177.2186.2205.2213.2216.2219.2220.2222.2223.2224.2225.2227.2234.2251.2253.2271.2275.2279.2282.2295.2299.2309.2312.2316.2322.2325.2328.2331.2335.2336.2343.2354.2358.2359.2370.2373.2376.2377.2400.2403.2405.2406.2410.2411.2414.2415.2416.2418.2425.2427.2440.2447.2453.2461.2465.2468.2472.2477.2484.2486.2488.2498.2506.2510.2517.2526.2527.2531.2532.2534.2535.2542.2552.2559.2564.2567.2568.2569.2571.2572.2575.2577.2579.2583.2584.2589.2595.2596.2604.2605.2608.2609.2610.2612.2614.2621.2624.2627.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2686.2687.2689.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2778.2784.2787.2791.2792.2798.2801.2805.2812.2813.2814.2816.2817.2821.2822.2824.2827.2830.2831.2832.2833.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2872.2874.2875.2878.2880.2881.2882.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2916.2917.2918.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2970.2972.2973.2974.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3001.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3023.3028.3031.3034.3038.3043.3051.3052.3053.3055.3058.3059.3063.3066.3070.3073.3074.3075.3076.3077.3089.3090.3093.3094.3095.3097.3099.3100.3106.3107.3109.3112.3117.3119.3126.3127.3128.3130.3133.3135.3136.3137.3145.3149.3150.3151.3153.3155.3163.3165.3167.3169.3172.3173.3177.3182.3183.3184.3185.3186.3187.3188.3189.3190.3194.3196.3200.3201.3209.3210.3211.3213.3214.3215.3217.3218.3222.3223.3225.3226.3227.3228.3230.3231.3233.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3254.3257.3260.3266.3270.3272.3281.3286.3288.3289.3290.3292.3293.3296.3299.3300.3306.3307.3309.3314.3315.3316.3318.3323.3324.3328.3330.3331.3531.3631.3731.3831.4131.4331.4531.4631.4731.4831.5231.6931.7131.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.11631.13431.13632.14034.14133.14237.14332.15731.16831.16931.21233.21731.23031.25131.25931.26031.26631.26831.27731.27831.28031.28332.28731.28831.29631.30331.30532.30732.32531.33931.34231.34631.34731.36831.39131.39531.40632.41131.41531.43631.43731.43831.45931.47232.47531.48131.49231.49332.49431.50831.52831.54231.56831.56931.57131.57231.57531; cf_clearance=FD5pEv9gT3GZ61LwLRoaR.PqGYcDuNLliq6T7ZAl7fI-1780645583-1.2.1.1-MctlCMJoWvZB9vGKb8t9qJ9lHI_k6SnMH3RVlpM_QEBZgukskqWZDpXdq_EkXKIL_PJ282XJQL7ku8qBN6zy8TOv8n3_V9u4QLzR7fkYFw6QZRwW6vg0taQWACQaQe8bWx.ogkcdN99OiJSi0n5l1Wpdk.KwGC2EA5jJip0wiSIRhprns9zby_TWVbkryG1.yseCgd9GGXS4k98.y2i1TlOw6ybPPQUGUZof259bQLMiRfVImS84OJVn4rjx.zHjCNfODo.UjOtz8jK4Di74xWv6a3sT9P9RLqZTMgprOupRl.2FqAg3enj9TgOC84tZfLFwjnHQBbIyN0AGnMwIvA; __cf_bm=pvdybwzX60Pdo4mW9LuTvZYqLDc7sujIZ4E46CflsQo-1780645583.558194-1.0.1.1-TFZVvA_LxHTSuT_YGeomCpA6Gl0PHLI32iSwgDkDC.Sf68F1VRjN_P2KAwvcjM3M8xCx0lIZkB.vPT.enskBaSBc61Me_ksxOokHW40v0.tkcOqZUCJ5ohU.xNUa9UixUpkfIa9KO1ZdndB_DMGzZw; consent_version=eu; domain_selected=true; viewport_size=1912; fbm_502159173164171=base_domain=.www.vinted.fr; fbsr_502159173164171=_SfixAaw2HU_FpqcQjuvuINBXMNeLbEScY8ndS1pzGo.eyJ1c2VyX2lkIjoiMTc1NjcyMTg2NDUxNTExMSIsImNvZGUiOiJBUUxfd2YtXzNlcUVjbDZGcjNlbmQ2TGdLUWlrUVRUa25iZGJHM2ZpclVuV245YngxQmd0d3F3V0RMOGFKaWdlQkpHMkdNX21BRmxSWnhPRFFMOGxSbFFLSkhNMXpRRlBnQVZ1bWVIbEdwdEdXMlN1NzZmQ0xITF9UZ0xxckdQOVpfV3BodTM4T19wdktRWktPWV94LVMtejVPdnF4bHp2TUlXcHhDZVQ1b0RoT05zZTU4X3p2aEVnZDhIbEt5THZud01VLVdscGJ2WmY3MEZ6SjJXbFE2MDhjQ0hlT0tBUUh3M0dRQXZ5RE53d3BSRG9sY3B6a09NeVMydzd3VXJRZk5lcGNFcXlGb1p4VkNUUndOeHVoYkJJejZFUGhjMGtSNnNZeDA5anVvQ3FBcjg3ay0zZEh2aUlCUExYVnE0TlFDSmx2ZEZKbVZMZlNIemtXMTBha1RsMTJ3YzZNMVE5NDE4dlEzaVlSNm5Na3ciLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTc4MDY0NTc1OX0; refresh_token_web=eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MTI1MDU2MSwiaWF0IjoxNzgwNjQ1NzYxLCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoicmVmcmVzaCIsInNjb3BlIjoidXNlciIsInNpZCI6Ijk2M2M0NGU4LTE3ODA2NDU3NjEiLCJzdWIiOiI2NTc0OTM2NSIsImNjIjoiRlIiLCJhbmlkIjoiOTA3ZWRhZmUtZjFiYi00NjIzLThhOWMtOTJlNGJhZWUwYWY2IiwiYWN0Ijp7InN1YiI6IjY1NzQ5MzY1In19.si_d8V4TkEG8zqFBfmJ6XPnPf4cZxwa01sNUv9ovgvVDVQ7kVtS8WaVLRnaLVKrnNrhUgpcleoBBvdKgnVj5Xkd77YHLNFJBh4BFIjqUlBN2utl1hb87lXuVGEtHffyok2mklUP0gD3aVNaj53GSWDgbRZQm7zrTgNkUNvKVEo9-5xBQN_ReNUyZLda2rZAtQmNqlZ6B-3JOhu0AArtglDV-gdcxapCNMK73qktMHYF8kM5mwVTI1Rrcd09K5Gtz7j6YRB0BOcjPHhapLfXnPr0GQI_nbG_cXIRmar1ABN7i-qUQhXfWGght7w_81ebQ0HqgZKT_GPm7nj9x8qbYWA; access_token_web=eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MDY1Mjk2MSwiaWF0IjoxNzgwNjQ1NzYxLCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoiYWNjZXNzIiwic2NvcGUiOiJ1c2VyIiwic2lkIjoiOTYzYzQ0ZTgtMTc4MDY0NTc2MSIsInN1YiI6IjY1NzQ5MzY1IiwiY2MiOiJGUiIsImFuaWQiOiI5MDdlZGFmZS1mMWJiLTQ2MjMtOGE5Yy05MmU0YmFlZTBhZjYiLCJhY3QiOnsic3ViIjoiNjU3NDkzNjUifX19.RRYGS2WnhAxSN2GjQCXfCyHwSlDTmiWEPpqoilIIGYhu-ayBx89lRDjKjPm3R0cZKhx_dAE6IaKEt-UPZMOBJIgNKbRV2osUypr7hZ--PsZgwo9nceMaDz1fBqci1A8EvqwpYAuPYuA4MPQzEhx-hZZyjLl_hMKqa8pAJ_KTPZrRQ1beLhyt0UqZu3OW4wOVmlnBcHTGOENzsnmEzw37VDCqB-HGywbVhXngUFkmdUj0hgbyN3fMKs4h3L5JGsQee4MgY2Gw0k4IR6nttyIW-oFovOJ65AhNDmI5T3Spw55U88ufhO-ZHnWX_RZqMyVSA72K9j1W2faEWHv8WN21wg; anon_id=907edafe-f1bb-4623-8a9c-92e4baee0af6; v_uid=65749365; v_sid=963c44e8-1780645761; user-locale=fr; user-iso-locale=fr-FR; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+05+2026+09%3A49%3A23+GMT%2B0200+(heure+d%E2%80%99%C3%A9t%C3%A9+d%E2%80%99Europe+centrale)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=65749365&isAnonUser=0&hosts=&interactionCount=2&prevHadToken=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0%2CV2STACK42%3A0%2CC0035%3A0%2CC0038%3A0&genVendors=V5%3A0%2CV2%3A0%2CV1%3A0%2C&crTime=1779353732584&intType=2&geolocation=FR%3BIDF&AwaitingReconsent=false; banners_ui_state=SUCCESS; _vinted_fr_session=TmdVTmFKdDdOMzdTaXFUOStXSndPRkw0Uy9UbDBNREFxblMvSWZqRGphN3RyeVYvb09USUdyblg3djlqUy9jRjNUakJobjJ0VWswS1k1eW9zUFZSMnNpSExaaDZpb0luNi9uYVFtUjczSkxZeGNYUlpwV2t2K0pVOVRUTzRnYy9RYWlSNWZGYk1WYWJ0ZFVmVjRoWERpdlU2RmVCV1lHTnFHVXRrNjZGN1NvN2I5dVFkR05ERTMzKzdrMUJ5VDd0bkhVVUZtY1M3Z0hQQTJIMm1wcERYZGpNOExQSldreU8yakRiNWNtRTFFekQycFhycUpoSjB5eG53R3VYa2VwYnk5aXN2VjZPTGNVOVhaNGVPOEl5a29pemhDbGpQUVloSXExdXRSMFREMHRSZXIvNlp5TVZldUtUU0pVODJMTnItLWFmbUozbFJlTURnYWM1R1lEbzNoT3c9PQ%3D%3D--304962fd0e50eabbc2732bb0f816cf5a8cc39562; datadome=kzLBei8l_tJydslLV9~2hVmtRJg09j1Zj5dezTBAfD7H4MXsIKv9siyzfEjO0TtP7S8_Fdh7D4Yr1YIL7bMFOg1tYGn1XCDcc2rGmujjGvT5tsewEQxlBmgxdV2Z9pj~"
# ─────────────────────────────────────────────────────
 
RECHERCHES = [
    {"mot_cle": "young gto",                    "prix_min": 50,  "mots_requis": ["gto"]},
    {"mot_cle": "coq de combat manga",           "prix_max": 40,  "mots_requis": ["coq"]},
    {"mot_cle": "bakuon retto",                                   "mots_requis": ["bakuon"]},
    {"mot_cle": "homonculus",                                     "mots_requis": ["homonculus"]},
    {"mot_cle": "ascension manga",               "prix_max": 45,  "mots_requis": ["ascension"]},
    {"mot_cle": "rokudenashi blues",             "prix_max": 15,  "mots_requis": ["rokudenashi"]},
    {"mot_cle": "rainbow abe",                                    "mots_requis": ["rainbow"]},
    {"mot_cle": "billy bat",                     "prix_max": 80,  "mots_requis": ["billy"]},
    {"mot_cle": "dragon ball perfect edition",   "prix_max": 100, "mots_requis": ["dragon", "ball"]},
    {"mot_cle": "fullmetal alchemiste perfect",  "prix_max": 100, "mots_requis": ["fullmetal"]},
    {"mot_cle": "integrale manga",               "prix_max": 80,  "mots_requis": ["integrale"]},
    {"mot_cle": "vagabond inoue",                                 "mots_requis": ["vagabond"]},
]
 
MOTS_EXCLUS = [
    "t-shirt", "tshirt", "tee shirt", "teeshirt", "sweat", "hoodie", "veste", "pull",
    "casquette", "chapeau", "chaussette", "pantalon", "short", "pyjama", "costume",
    "figurine", "figure", "statuette", "statue", "funko", "pop", "nendoroid",
    "poster", "affiche", "print", "tableau", "cadre",
    "goodies", "goodie", "gadget", "accessoire",
    "mug", "tasse", "verre", "assiette",
    "jeu video", "jeu vidéo", "game", "ps4", "ps5", "nintendo", "switch", "xbox",
    "soundtrack", "musique", "cd", "vinyle", "vinyl",
    "cartes", "carte", "trading card", "card game",
    "cosplay", "déguisement", "deguisement",
    "sac", "sacoche", "tote bag", "trousse",
    "sticker", "autocollant", "pin", "badge",
    "lampe", "veilleuse", "coussin", "plaid",
    "peluche", "doudou",
]
 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json",
    "Cookie": COOKIE_STR,
}
 
seen_ids = set()
 
def est_valide(titre, description, mots_requis):
    texte = (titre + " " + description).lower()
    for mot in mots_requis:
        if mot not in texte:
            return False
    for mot in MOTS_EXCLUS:
        if mot in texte:
            return False
    return True
 
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"})
 
def check_vinted():
    for r in RECHERCHES:
        params = {
            "search_text": r["mot_cle"],
            "order": "newest_first",
            "per_page": 20,
            "catalog_ids[]": 1231,
        }
        if "prix_min" in r:
            params["price_from"] = r["prix_min"]
        if "prix_max" in r:
            params["price_to"] = r["prix_max"]
 
        try:
            res = requests.get(
                "https://www.vinted.fr/api/v2/catalog/items",
                params=params, headers=HEADERS, timeout=10
            )
            items = res.json().get("items", [])
            for item in items:
                iid = item["id"]
                if iid not in seen_ids:
                    seen_ids.add(iid)
                    titre = item.get("title", "Sans titre")
                    desc  = item.get("description", "")
                    prix  = item.get("price", {}).get("amount", "?")
                    url   = f"https://www.vinted.fr/items/{iid}"
 
                    if not est_valide(titre, desc, r.get("mots_requis", [])):
                        print(f"⏭️ Ignoré : {titre}")
                        continue
 
                    msg = (
                        f"🔴 <b>[{r['mot_cle'].upper()}]</b> Nouvelle annonce !\n\n"
                        f"📦 {titre}\n"
                        f"💶 {prix}€\n"
                        f"🔗 {url}"
                    )
                    send_telegram(msg)
                    print(f"✅ Envoyé : {titre} — {prix}€")
        except Exception as e:
            print(f"Erreur : {e}")
 
print("🚀 VintedAlert démarré — vérification toutes les 3 minutes")
send_telegram("✅ VintedAlert est actif ! Tu recevras les annonces ici.")
check_vinted()
schedule.every(3).minutes.do(check_vinted)
 
while True:
    schedule.run_pending()
    time.sleep(30)
 
