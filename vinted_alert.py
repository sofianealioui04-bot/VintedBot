import requests, schedule, time

# ─── MODIFIE CES 3 VALEURS ───────────────────────────
BOT_TOKEN     = "8981011090:AAEzR1kuIMYRQsZI9fQq4j5oN4SCg6QWxJ0"
CHAT_ID       = "5322714033"
ACCESS_TOKEN  = "eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MDYxNjI2OSwiaWF0IjoxNzgwNjA5MDY5LCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoiYWNjZXNzIiwic2NvcGUiOiJ1c2VyIiwic2lkIjoiMTY1NGViZDMtMTc4MDMzNTE3NyIsInN1YiI6IjY1NzQ5MzY1IiwiY2MiOiJGUiIsImFuaWQiOiI5MDdlZGFmZS1mMWJiLTQ2MjMtOGE5Yy05MmU0YmFlZTBhZjYiLCJhY3QiOnsic3ViIjoiNjU3NDkzNjUifX0.KK4B4jcvse1xR6_CppGIBj6_RqXA-m6Z1rTwzZPqDjKrhpn0OhVBKkXmWvGLSAZSDQMuNCSFhC8oW7HIqQaqe_RrugS0b1z8j2P1H6igC2B4GsdX-29gEUt4Az5k6fyFaR-IMeAsuVhLGx7hntkYL0xCVCEXBO7A4cadprSP1aapwfuXclIZmCKcIj-2dQUAast9QHmxbMEfAZRlAzB8ep-qN2A98W8BALB64_eeEtUFQ6HYDTeujghEK6YicZ9LkcOU-YRzEH1x2BkZajhvzCgnkF_gVzWe9LrqQAr3157_xBsIKUnAweik2oWtIgjRlAuqN4KB6a8VsZdgVQfkDQ; 
"
REFRESH_TOKEN = "eyJraWQiOiJFNTdZZHJ1SHBsQWp1MmNObzFEb3JIM2oyN0J1NS1zX09QNVB3UGlobjVNIiwiYWxnIjoiUFMyNTYifQ.eyJhY2NvdW50X2lkIjo0NTkwMDg1OSwiYXBwX2lkIjo0LCJhdWQiOiJmci5jb3JlLmFwaSIsImNsaWVudF9pZCI6IndlYiIsImV4cCI6MTc4MTIxMzg2OSwiaWF0IjoxNzgwNjA5MDY5LCJpc3MiOiJ2aW50ZWQtaWFtLXNlcnZpY2UiLCJsb2dpbl90eXBlIjoxLCJwdXJwb3NlIjoicmVmcmVzaCIsInNjb3BlIjoidXNlciIsInNpZCI6IjE2NTRlYmQzLTE3ODAzMzUxNzciLCJzdWIiOiI2NTc0OTM2NSIsImNjIjoiRlIiLCJhbmlkIjoiOTA3ZWRhZmUtZjFiYi00NjIzLThhOWMtOTJlNGJhZWUwYWY2IiwiYWN0Ijp7InN1YiI6IjY1NzQ5MzY1In19.HVp92lCqziZyoYJDNvITm4xI6t5ak89hr1EuOn7Uk0aXtgpYyeqZnV2AFT9JVXmlAiKvpJiHv4Bvae5_IvhS0iC42ecsWLUCIFM9aBzFAv4Ws4Ekahp0rHSc4OkRhX4TPhHZxRjZ_9o_XkhnokjT_X2elJLUaGDUMEhb92Chc56Olj9t4scH6ul898EnswOZN2P4Lx6PiFuNY5UmObnt2ujQSTYB_PPtEAPvqnOsn0yn27tgyahVkVe7mFaWCoUaNDz8gYbREn54LpgRTmIfnlrP2Cg8u0DZgBv18QZi8DAhJpqKBVO78n-GyKR_VLHdIX0UT22d_C7fs24LKx1-TA"
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

# Token en mémoire (se renouvelle automatiquement)
current_token = {"access": ACCESS_TOKEN}

def refresh_access_token():
    try:
        res = requests.post(
            "https://www.vinted.fr/api/v2/tokens/refresh",
            json={"refresh_token": REFRESH_TOKEN},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        data = res.json()
        new_token = data.get("access_token")
        if new_token:
            current_token["access"] = new_token
            print("🔄 Token renouvelé automatiquement")
            return True
    except Exception as e:
        print(f"Erreur renouvellement token : {e}")
    return False

def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "application/json",
        "Authorization": f"Bearer {current_token['access']}",
    }

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

seen_ids = set()

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
                params=params, headers=get_headers(), timeout=10
            )

            # Si token expiré, on le renouvelle et on réessaie
            if res.status_code == 401:
                print("⚠️ Token expiré, renouvellement...")
                if refresh_access_token():
                    res = requests.get(
                        "https://www.vinted.fr/api/v2/catalog/items",
                        params=params, headers=get_headers(), timeout=10
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
