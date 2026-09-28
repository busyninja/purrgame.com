#!/usr/bin/env python3
"""Builds the static site from content/<lang>/<page>.html fragments.

English lives at the root (/), every other language in /<code>/. The English
pages carry a tiny script that sends first-time visitors to their browser's
language when we have it; choosing a language in the switcher is remembered
(localStorage "purr_lang") and always wins. Run after editing any fragment:

    python3 build.py

Output files are committed (GitHub Pages serves the repo as is).
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://purrgame.com"
PAGES = ["index", "privacy", "support", "delete", "terms"]

LANGS = {
    "en": {"dir": "", "html": "en", "name": "English"},
    "es": {"dir": "es/", "html": "es", "name": "Español"},
    "de": {"dir": "de/", "html": "de", "name": "Deutsch"},
    "fr": {"dir": "fr/", "html": "fr", "name": "Français"},
    "ja": {"dir": "ja/", "html": "ja", "name": "日本語"},
    "ko": {"dir": "ko/", "html": "ko", "name": "한국어"},
    "zh-hant": {"dir": "zh-hant/", "html": "zh-Hant", "name": "繁體中文"},
}

UI = {
    "en": {"support": "Support", "privacy": "Privacy", "terms": "Terms", "delete": "Delete account", "language": "Language",
           "titles": {"index": "Purr: Cozy Cat Home", "privacy": "Privacy Policy · Purr", "support": "Support · Purr", "delete": "Delete your account · Purr", "terms": "Terms of Use · Purr"},
           "desc": "Adopt, cuddle and collect cats in Purr, a cozy cat home for phones and tablets. Free, kind and made for families."},
    "es": {"support": "Ayuda", "privacy": "Privacidad", "terms": "Condiciones", "delete": "Borrar cuenta", "language": "Idioma",
           "titles": {"index": "Purr: Cozy Cat Home", "privacy": "Política de privacidad · Purr", "support": "Ayuda · Purr", "delete": "Borrar tu cuenta · Purr", "terms": "Condiciones de uso · Purr"},
           "desc": "Adopta, mima y colecciona gatos en Purr, un hogar acogedor para gatos en tu móvil o tablet. Gratis, amable y pensado para familias."},
    "de": {"support": "Hilfe", "privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "delete": "Konto löschen", "language": "Sprache",
           "titles": {"index": "Purr: Gemütliches Katzenheim", "privacy": "Datenschutzerklärung · Purr", "support": "Hilfe · Purr", "delete": "Konto löschen · Purr", "terms": "Nutzungsbedingungen · Purr"},
           "desc": "Adoptiere, knuddle und sammle Katzen in Purr, einem gemütlichen Katzenheim für Handy und Tablet. Kostenlos, liebevoll und für Familien gemacht."},
    "fr": {"support": "Aide", "privacy": "Confidentialité", "terms": "Conditions", "delete": "Supprimer le compte", "language": "Langue",
           "titles": {"index": "Purr : Maison de chats", "privacy": "Politique de confidentialité · Purr", "support": "Aide · Purr", "delete": "Supprimer ton compte · Purr", "terms": "Conditions d'utilisation · Purr"},
           "desc": "Adopte, câline et collectionne des chats dans Purr, une maison douillette pour chats sur mobile et tablette. Gratuit, doux et pensé pour les familles."},
    "ja": {"support": "サポート", "privacy": "プライバシー", "terms": "利用規約", "delete": "アカウント削除", "language": "言語",
           "titles": {"index": "Purr：ねこのおうち", "privacy": "プライバシーポリシー · Purr", "support": "サポート · Purr", "delete": "アカウントの削除 · Purr", "terms": "利用規約 · Purr"},
           "desc": "Purrは、ネコを迎えて、なでて、集めるあたたかいおうちゲーム。基本無料で、家族みんなで安心して遊べます。"},
    "ko": {"support": "고객 지원", "privacy": "개인정보", "terms": "이용 약관", "delete": "계정 삭제", "language": "언어",
           "titles": {"index": "Purr: 포근한 고양이 집", "privacy": "개인정보 처리방침 · Purr", "support": "고객 지원 · Purr", "delete": "계정 삭제 · Purr", "terms": "이용 약관 · Purr"},
           "desc": "Purr에서 고양이를 입양하고, 쓰다듬고, 모아요. 휴대폰과 태블릿을 위한 포근한 고양이 집. 무료이며 가족 모두를 위해 만들었어요."},
    "zh-hant": {"support": "客服", "privacy": "隱私權", "terms": "使用條款", "delete": "刪除帳號", "language": "語言",
           "titles": {"index": "Purr：溫馨貓咪之家", "privacy": "隱私權政策 · Purr", "support": "客服 · Purr", "delete": "刪除你的帳號 · Purr", "terms": "使用條款 · Purr"},
           "desc": "在 Purr 領養、寵愛、收集貓咪，一個適合手機與平板的溫馨貓咪之家。免費遊玩，溫柔又適合全家。"},
}

# First visit to an English page: go to the visitor's language if we have it.
REDIRECT = """<script>
(function(){try{
var have={"es":"es","de":"de","fr":"fr","ja":"ja","ko":"ko"};
var pick=localStorage.getItem("purr_lang");
if(!pick){var ls=navigator.languages||[navigator.language||""];
for(var i=0;i<ls.length;i++){var l=(ls[i]||"").toLowerCase();
if(l.indexOf("zh")===0){if(/hant|tw|hk|mo/.test(l)){pick="zh-hant";break;}continue;}
var b=l.split("-")[0];if(b==="en"){pick="en";break;}if(have[b]){pick=have[b];break;}}}
if(pick&&pick!=="en"){var p=location.pathname.replace(/^\\//,"");if(p==="index.html")p="";
location.replace("/"+pick+"/"+p+location.search+location.hash);}
}catch(e){}})();
</script>"""

SWITCH_JS = """<script>
document.querySelectorAll("[data-lang]").forEach(function(a){a.addEventListener("click",function(){try{localStorage.setItem("purr_lang",a.getAttribute("data-lang"));}catch(e){}});});
</script>"""


def page_url(lang: str, page: str) -> str:
    return "/" + LANGS[lang]["dir"] + ("" if page == "index" else page + ".html")


def build_page(lang: str, page: str, fragment: str) -> str:
    ui = UI[lang]
    meta = LANGS[lang]
    alternates = "\n".join(f'<link rel="alternate" hreflang="{LANGS[l]["html"]}" href="{SITE}{page_url(l, page)}">' for l in LANGS)
    alternates += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{page_url("en", page)}">'
    switch = " · ".join(
        (f'<strong>{html.escape(LANGS[l]["name"])}</strong>' if l == lang else
         f'<a href="{page_url(l, page)}" lang="{LANGS[l]["html"]}" data-lang="{l}">{html.escape(LANGS[l]["name"])}</a>')
        for l in LANGS)
    home = page_url(lang, "index")
    doc = page != "index"
    body = f'<article class="doc">\n{fragment}</article>' if doc else fragment
    return f"""<!doctype html>
<html lang="{meta['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(ui['titles'][page])}</title>
<meta name="description" content="{html.escape(ui['desc'])}">
<link rel="icon" href="/assets/icon-512.png">
<link rel="apple-touch-icon" href="/assets/icon-512.png">
<link rel="canonical" href="{SITE}{page_url(lang, page)}">
{alternates}
<meta property="og:title" content="{html.escape(ui['titles']['index'])}">
<meta property="og:description" content="{html.escape(ui['desc'])}">
<meta property="og:image" content="{SITE}/assets/feature.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{REDIRECT if lang == 'en' else ''}
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="{home}"><img src="/assets/icon-512.png" alt="">Purr</a>
    <nav class="links">
      <a href="support.html">{html.escape(ui['support'])}</a>
      <a href="privacy.html">{html.escape(ui['privacy'])}</a>
    </nav>
  </header>

{body}

  <footer>
    <span>© 2026 Busy Ninja · Purr: Cozy Cat Home</span>
    <span><a href="terms.html">{html.escape(ui['terms'])}</a> · <a href="privacy.html">{html.escape(ui['privacy'])}</a> · <a href="support.html">{html.escape(ui['support'])}</a> · <a href="delete.html">{html.escape(ui['delete'])}</a></span>
  </footer>
  <nav class="langs" aria-label="{html.escape(ui['language'])}">🌐 {switch}</nav>
</div>
{SWITCH_JS}
</body>
</html>
"""


def main() -> None:
    written = 0
    missing = []
    for lang, meta in LANGS.items():
        for page in PAGES:
            src = ROOT / "content" / lang / f"{page}.html"
            if not src.exists():
                missing.append(f"{lang}/{page}")
                continue
            out = ROOT / meta["dir"] / f"{page}.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(build_page(lang, page, src.read_text(encoding="utf-8")), encoding="utf-8")
            written += 1
    print(f"wrote {written} pages" + (f"; missing: {', '.join(missing)}" if missing else ""))


if __name__ == "__main__":
    main()
