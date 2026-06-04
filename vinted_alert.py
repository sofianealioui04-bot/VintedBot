import requests, schedule, time

# ─── MODIFIE CES 3 VALEURS ───────────────────────────
BOT_TOKEN  = "8981011090:AAEzR1kuIMYRQsZI9fQq4j5oN4SCg6QWxJ0"
CHAT_ID    = "5322714033"
COOKIE_STR = "datadome=CbbT~4Jn2akfe03JTdAVEh~~4_~XESS0DXCeTq~XnLpypONFTHBnxs~TEUHgBrGnnykieTZLH80NmN2PyZB1ylyyJTt7Q25TVL00TtXOT34WEI1R8JuOMFKjRnEXYlyD; _lm_id=9FPOMD8NDJ8F3R3B; cto_bidid=lA2rbF92ZDRCSzVoQ2dqQUVKZkQ0cXV2dEFobVM3Yk1EOSUyQklDVUFPM2RGUXk0aWElMkZWRG05TEFTblFoYWdoU2k0QzdCZm9CSzRrMCUyQk13SEY3cyUyRnc5azlidU5nJTNEJTNE; cto_bundle=RczZxF92TFlBek8lMkJMeU9WSEREdjNWNGhRTDRKaEolMkZMcGh1ZUJMVjBxTk5IRWxHRDJYc2tTTFhKJTJGTVFtUjZNZldCWUhISFJMYldqVnJXTUVmNFhsR29zNlpDQzlVTGtoWUNIRmswVDhNYW1yNnZvSHlpYkxWayUyRmIyMnBRbk4xcEpwRzVk; _vinted_fr_session=MWtjOVRqYkI4a3g2aDhpZitnWklRbkMxZ0FpSGo5cVRyUVpMYVZMeUUyanFDRlMvNzF1TTRDaTF2Qmd6bGFTVVgrM3pVK0Q4b2ZSQUdPOHlIRXRSczRWcjRWSWt2OTkrRkh6U2ZvMzRRa3NWcnQycEkyL0NFTXF1bUd0NEZqSXpMS0lNcXB4RW5TeExycEJJQi9pc0JiTWFBc0VWRTBtdVdRVC8wajFpbDRyMzdTUk10Zjd0dndJSFpYTEd5U0NyN0NoYm9PUlZtdURlZGdsUXNjc2s2ZG9qK1QzdmhLcklkbTZWWjRFMUE0L1ZGRXhjalhHaDJydzlwWXFiWHNmY1AzZTVuR3RRajVNSWxYVXlWUjFVYXdSVDN3MjRFZGZxS1FHV3g3YnpQc29qR1dyWUd0QWlZYTQzTlF6blVZVHotLXJBTEtyU09mc0txRm8vQjhQNzJydFE9PQ%3D%3D--c116f67c09387589c49db497637fe2325bb52864; anon_id=907edafe-f1bb-4623-8a9c-92e4baee0af6; viewport_size=1304; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+04+2026+23%3A38%3A39+GMT%2B0200+(Central+European+Summer+Time)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=65749365&isAnonUser=1&hosts=&interactionCount=1&prevHadToken=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1%2CV2STACK42%3A1%2CC0035%3A1%2CC0038%3A1&genVendors=V5%3A1%2CV2%3A1%2CV1%3A1%2C&intType=1&crTime=1780334976147&geolocation=FR%3BIDF&AwaitingReconsent=false; user-iso-locale=fr-FR; user-locale=fr; ad_blocker_detected=true; cf_clearance=eH7h_hK37oDHoVTHAE_2lLvQ0syToT_snMbtyhffsqo-1780609069-1.2.1.1-6ktc_.Vns87iep1Ojx.F2UHHOnZ46_ZgxxhaWOWI6fYOLDOTTsXONze67y7wNJywQYuMHZNWnNvtgdG6MOF.HkP14xt3pRadf4saVees4na41W905qxCGNVDCThQP9cj5GlSLbeKtImdtweS9bT4g5buEk1BW2OfpjqUJvlwu6_fDqAkUI_.Z_cUOMW_OR6GTJr24QBBQvRDrcetqLUw36nBhybGrHdJmAUXIQjMfcVwSJTx2jCdPISFWQDnMneUMC59_M4DhkMjoAc3OAp6Di0b3k7Pa.K2cwXNd.XXG9fFiTwIs4ZtJyYRV2u_x2cG.kM2AdLCWfn3dtWDf5GZ7A; access_token_web=eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MDYxNjI2OSwiaWF0IjoxNzgwNjA5MDY5LCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoiYWNjZXNzIiwic2NvcGUiOiJ1c2VyIiwic2lkIjoiMTY1NGViZDMtMTc4MDMzNTE3NyIsInN1YiI6IjY1NzQ5MzY1IiwiY2MiOiJGUiIsImFuaWQiOiI5MDdlZGFmZS1mMWJiLTQ2MjMtOGE5Yy05MmU0YmFlZTBhZjYiLCJhY3QiOnsic3ViIjoiNjU3NDkzNjUifX0.KK4B4jcvse1xR6_CppGIBj6_RqXA-m6Z1rTwzZPqDjKrhpn0OhVBKkXmWvGLSAZSDQMuNCSFhC8oW7HIqQaqe_RrugS0b1z8j2P1H6igC2B4GsdX-29gEUt4Az5k6fyFaR-IMeAsuVhLGx7hntkYL0xCVCEXBO7A4cadprSP1aapwfuXclIZmCKcIj-2dQUAast9QHmxbMEfAZRlAzB8ep-qN2A98W8BALB64_eeEtUFQ6HYDTeujghEK6YicZ9LkcOU-YRzEH1x2BkZajhvzCgnkF_gVzWe9LrqQAr3157_xBsIKUnAweik2oWtIgjRlAuqN4KB6a8VsZdgVQfkDQ; refresh_token_web=eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MTIxMzg2OSwiaWF0IjoxNzgwNjA5MDY5LCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoicmVmcmVzaCIsInNjb3BlIjoidXNlciIsInNpZCI6IjE2NTRlYmQzLTE3ODAzMzUxNzciLCJzdWIiOiI2NTc0OTM2NSIsImNjIjoiRlIiLCJhbmlkIjoiOTA3ZWRhZmUtZjFiYi00NjIzLThhOWMtOTJlNGJhZWUwYWY2IiwiYWN0Ijp7InN1YiI6IjY1NzQ5MzY1In19.HVp92lCqziZyoYJDNvITm4xI6t5ak89hr1EuOn7Uk0aXtgpYyeqZnV2AFT9JVXmlAiKvpJiHv4Bvae5_IvhS0iC42ecsWLUCIFM9aBzFAv4Ws4Ekahp0rHSc4OkRhX4TPhHZxRjZ_9o_XkhnokjT_X2elJLUaGDUMEhb92Chc56Olj9t4scH6ul898EnswOZN2P4Lx6PiFuNY5UmObnt2ujQSTYB_PPtEAPvqnOsn0yn27tgyahVkVe7mFaWCoUaNDz8gYbREn54LpgRTmIfnlrP2Cg8u0DZgBv18QZi8DAhJpqKBVO78n-GyKR_VLHdIX0UT22d_C7fs24LKx1-TA; _ga_8H12QY46R8=GS2.1.s1780335090$o1$g1$t1780335697$j60$l0$h0; _ga_ZJHK1N3D75=GS2.1.s1780335090$o1$g1$t1780335697$j60$l0$h0; _fbp=fb.1.1780335090511.691068736998621802; _ga=GA1.1.1443941993.1780335090; _cc_id=fa3af4e532c54b52921491fce3598395; _pubcid=f2407386-9c7d-4a4a-8e2a-5615636cc451; panoramaId=84cc8bdfb0512a17eb79d9bbbb2c185ca02c65fd145582c6a4219acd0824098b; panoramaIdType=panoDevice; panoramaId_expiry=1780940040392; v_sid=1654ebd3-1780335177; v_uid=65749365; fbm_502159173164171=base_domain=.www.vinted.fr; fbsr_502159173164171=ZLxfx3fd6Mpf8LbMc7Cg6euT32H9vcaMZQbVJigvQdU.eyJ1c2VyX2lkIjoiMTc1NjcyMTg2NDUxNTExMSIsImNvZGUiOiJBUUk2S3hFRndELURPQ1BfaXpnalloQVU0dER2V2pBcnpwbTd5cmRCc09LT1dQbGpiLThmUW1wUUVUTlNyU2hXSjZncmVzYWM2T3Q2SFozZllrRFlFd2xxSEVhZ0picWZ5eUpsVVEyZWtVaWx3bkZhM18tTGpKa2Nja3ZGa0p5c01HRWRyZi1pRWxpNnV4TWUyY3lma3Y4R1pQSXZmcloxakp6LTg1UXdpU2hTVnpsYTR5RGNQOHY0SjBwSjB6TmtmaEJqVVJaU1NxWVVjV09CXzItYk9XVEl3bmVfWGJQN2x5bGlmZVl3TWVOR1hMX3NGQW1RaXhkQVlZLXJSWFI5VlZLVnVSQ1pINllIVngzczR3aW1Obl9PM3N6TUtlZHBZSk5LTURNdktvVjJMR1diX0VySTVkNnlfOHZfbzE0WDBDZHNLZklLdkd2WXE4SUc1WlRDWGxDRFpsN1d2RW5lcXVDMGVqbFFZaUN3ell6Ry1Vdk5rNzVpSm40b05ORlNPc1YtWmlUR2FuZ1NTVEpfRDFUS0pKSFkiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTc4MDMzNTE3NX0; __ps_did=pscrb_fd12c3e2-64dc-4378-adba-d4519b48d44c; __ps_fva=1780335090493; __ps_lu=https://www.vinted.fr/; __ps_r=_; _gcl_au=1.1.143950659.1780335090; domain_selected=true; anonymous-iso-locale=fr-FR; anonymous-locale=fr; OTAdditionalConsentString=2~20.43.55.57.61.70.83.89.93.108.117.122.124.135.143.144.147.149.159.161.184.192.196.211.228.230.236.239.255.259.266.272.286.291.311.313.314.320.322.323.327.358.367.370.371.385.407.415.424.429.430.436.445.469.486.491.494.495.522.523.540.550.560.568.574.576.584.587.591.621.723.737.797.798.803.820.827.839.864.899.904.922.938.955.959.979.981.985.986.1003.1027.1031.1033.1046.1047.1048.1051.1053.1067.1092.1095.1097.1099.1107.1109.1126.1135.1143.1149.1152.1162.1166.1186.1188.1192.1205.1215.1220.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1329.1342.1345.1356.1365.1403.1415.1416.1419.1421.1423.1440.1449.1455.1495.1512.1514.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1598.1603.1616.1638.1651.1653.1659.1660.1667.1677.1678.1682.1697.1699.1703.1712.1716.1720.1721.1725.1732.1735.1745.1750.1753.1765.1782.1786.1800.1808.1810.1825.1827.1832.1838.1840.1843.1845.1859.1870.1878.1880.1882.1889.1898.1911.1917.1928.1929.1942.1944.1958.1962.1963.1964.1967.1968.1969.1978.1985.1987.2003.2027.2035.2038.2039.2044.2047.2052.2056.2064.2068.2069.2072.2074.2084.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2141.2147.2156.2166.2177.2186.2205.2213.2216.2219.2220.2222.2223.2224.2225.2227.2234.2251.2253.2271.2275.2279.2282.2295.2299.2309.2312.2316.2322.2325.2328.2331.2335.2336.2343.2354.2358.2359.2370.2373.2376.2377.2400.2403.2405.2406.2410.2411.2414.2415.2416.2418.2425.2427.2440.2447.2453.2461.2465.2468.2472.2477.2484.2486.2488.2498.2506.2510.2517.2526.2527.2531.2532.2534.2535.2542.2552.2559.2564.2567.2568.2569.2571.2572.2575.2577.2579.2583.2584.2589.2595.2596.2604.2605.2608.2609.2610.2612.2614.2621.2624.2627.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2686.2687.2689.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2778.2784.2787.2791.2792.2798.2801.2805.2812.2813.2814.2816.2817.2821.2822.2824.2827.2830.2831.2832.2833.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2872.2874.2875.2878.2880.2881.2882.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2916.2917.2918.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2970.2972.2973.2974.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3001.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3023.3028.3031.3034.3038.3043.3051.3052.3053.3055.3058.3059.3063.3066.3070.3073.3074.3075.3076.3077.3089.3090.3093.3094.3095.3097.3099.3100.3106.3107.3109.3112.3117.3119.3126.3127.3128.3130.3133.3135.3136.3137.3145.3149.3150.3151.3153.3155.3163.3165.3167.3169.3172.3173.3177.3182.3183.3184.3185.3186.3187.3188.3189.3190.3194.3196.3200.3201.3209.3210.3211.3213.3214.3215.3217.3218.3222.3223.3225.3226.3227.3228.3230.3231.3233.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3254.3257.3260.3266.3270.3272.3281.3286.3288.3289.3290.3292.3293.3296.3299.3300.3306.3307.3309.3314.3315.3316.3318.3323.3324.3328.3330.3331.3531.3631.3731.3831.4131.4331.4531.4631.4731.4831.5231.6931.7131.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.11631.13431.13632.14034.14133.14237.14332.15731.16831.16931.21233.21731.23031.25131.25931.26031.26631.26831.27731.27831.28031.28332.28731.28831.29631.30331.30532.30732.32531.33931.34231.34631.34731.36831.39131.39531.40632.41131.41531.43631.43731.43831.45931.47232.47531.48131.49231.49332.49431.50831.52831.54231.56831.56931.57131.57231.57531~dv; OptanonAlertBoxClosed=2026-06-01T17:29:35.837Z; eupubconsent-v2=CQlHtnAQlHtnAAcABBFRChFsAP_gAEPgAAwILNtR_G__bWlr-Tb3abpkeYxP99hr7sQxBgbIkm4FzLvW7JwCx2EZNAzatiIKmRIAu3TBIQNlHIDURUCgKIgFryDMaEyUoTNKJ6BkiBMRI2JQCFhum4pjWQCY4ur_5kc0mB-N7dr82dzyy4hHn3a5fmS1UJCcIYetDfn8ZBKS-9IEd-x8v4v4_EbpEm8eS1n_pGtp4jc6YlM6dBmxt-TyffzPn_f7kfe7X_vc_n3zv8oXH7rr_4LMgAmGh0QRlkQCBAoCAECABQVhABQIAgAASAogIATBgQ5AwAXWESAEAKAAYIAQAAgwABAAAJAAhEAEABAIAQIBAoAAwAIAgIAGBgADABQiAQAAgOgYpgQQCBYAJEYUBggQgAJBAS2VCCQBAgrhCkWOAQQIiYKAAAEAAoAAAA8LAQklBKxIIAuILoAEAAAAKIEGBFIWYAgoDIFoKwJOAyNMASPMEiSHQRAEwQkZBkQmqCQeKYogAAAA.f_wACHwAAAAA.ILNtR_G__bXlv-Tb36bpkeYxf99hr7sQxBgbIsm4FzLvW7JwC32EbNEzatiYKmRIAu3TBIQNtHIjURUChKIgVrzDsaEyUoTtKJ-BkiDMRY2JQCFhum4pjWQCZ4ur_50d0mR-N7dr-2dzyy5hnv3a9fuS1UJicKYetHfn8ZBKS-_IU9_x-_4v4_MbpEm8eS1v_tGtt43c64tP6dpuxt-Tyffzfv_f72fe7X__c__33_-qXX_r7_4A; consent_version=eu; is_shipping_fees_applied_info_banner_dismissed=false; non_dot_com_www_domain_cookie_buster=1; v_udt=VEtlQ1I2eFJnYW8rcmNXb1p2NVJKZ0JxR1FYMy0tMDRMcE92aDU1VjM0ZHBjTy0tUVMrMlpDVmpyNWMwTUxlODRXYzNMQT09"
# ─────────────────────────────────────────────────────

RECHERCHES = [
    {"mot_cle": "young gto",                    "prix_min": 50,  "mots_requis": ["gto"]},
    {"mot_cle": "coq de combat manga",           "prix_max": 40,  "mots_requis": ["coq", "combat"]},
    {"mot_cle": "bakuon retto",                                   "mots_requis": ["bakuon"]},
    {"mot_cle": "homonculus",                                     "mots_requis": ["homonculus"]},
    {"mot_cle": "ascension manga",               "prix_max": 45,  "mots_requis": ["ascension"]},
    {"mot_cle": "rokudenashi blues",             "prix_max": 15,  "mots_requis": ["rokudenashi"]},
    {"mot_cle": "rainbow abe",                                    "mots_requis": ["rainbow", "abe"]},
    {"mot_cle": "billy bat",                     "prix_max": 80,  "mots_requis": ["billy", "bat"]},
    {"mot_cle": "dragon ball perfect edition",   "prix_max": 100, "mots_requis": ["dragon", "ball", "perfect"]},
    {"mot_cle": "fullmetal alchemiste perfect",  "prix_max": 100, "mots_requis": ["fullmetal"]},
    {"mot_cle": "integrale manga",               "prix_max": 80,  "mots_requis": ["integrale", "manga"]},
    {"mot_cle": "vagabond inoue",                                 "mots_requis": ["vagabond", "inoue"]},
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
