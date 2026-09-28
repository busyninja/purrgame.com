#!/usr/bin/env python3
"""One-off generator for the index, support and delete fragments of the five
added languages (de, fr, ja, ko, zh-hant). Kept for reference: edit the
fragments in content/<lang>/ directly from now on, then run build.py."""
from pathlib import Path

HERE = Path(__file__).resolve().parent

INDEX = """  <section class="hero">
    <div>
      <h1>{h1a} <span>{h1b}</span></h1>
      <p class="lead">{lead}</p>
      <div class="badges">
        <span class="badge">🍎 <span>App Store<small>{soon}</small></span></span>
        <span class="badge">▶ <span>Google Play<small>{soon}</small></span></span>
      </div>
    </div>
    <div class="art"><img src="/assets/splash.png" alt="{art}"></div>
  </section>

  <section class="shots" aria-label="{shots}">
    <img src="/assets/shot-01.png" alt="{s1}">
    <img src="/assets/shot-02.png" alt="{s2}">
    <img src="/assets/shot-03.png" alt="{s3}">
    <img src="/assets/shot-04.png" alt="{s4}">
    <img src="/assets/shot-05.png" alt="{s5}">
    <img src="/assets/shot-06.png" alt="{s6}">
  </section>

  <section class="features">
    <div class="feature"><div class="emoji">🐾</div><h3>{f1h}</h3><p>{f1}</p></div>
    <div class="feature"><div class="emoji">🐱</div><h3>{f2h}</h3><p>{f2}</p></div>
    <div class="feature"><div class="emoji">🛋️</div><h3>{f3h}</h3><p>{f3}</p></div>
    <div class="feature"><div class="emoji">🏡</div><h3>{f4h}</h3><p>{f4}</p></div>
    <div class="feature"><div class="emoji">💌</div><h3>{f5h}</h3><p>{f5}</p></div>
    <div class="feature"><div class="emoji">🧸</div><h3>{f6h}</h3><p>{f6}</p></div>
  </section>

  <section class="families">
    <h2>{fam}</h2>
    <ul>
      <li>{g1}</li>
      <li>{g2}</li>
      <li>{g3}</li>
      <li>{g4}</li>
    </ul>
  </section>
"""

SUPPORT = """    <h1>{h1}</h1>
    <p>{intro}</p>

    <h2>{faq}</h2>
    <h3>{q1}</h3>
    <p>{a1}</p>
    <h3>{q2}</h3>
    <p>{a2}</p>
    <h3>{q3}</h3>
    <p>{a3}</p>
    <h3>{q4}</h3>
    <p>{a4}</p>
    <h3>{q5}</h3>
    <p>{a5}</p>
"""

DELETE = """    <h1>{h1}</h1>
    <p class="meta">Purr: Cozy Cat Home · Busy Ninja</p>
    <h2>{h_game}</h2>
    <ol>
      <li>{l1}</li>
      <li>{l2}</li>
      <li>{l3}</li>
    </ol>
    <h2>{h_mail}</h2>
    <p>{mail}</p>
    <h2>{h_what}</h2>
    <p>{what}</p>
    <h2>{h_kept}</h2>
    <p>{kept}</p>
"""

MAIL = '<a href="mailto:hello@purrgame.com">hello@purrgame.com</a>'

T = {}

T["de"] = dict(
    index=dict(
        h1a="Katzen adoptieren, knuddeln und", h1b="sammeln",
        lead="Purr ist ein warmes kleines Zuhause für sehr süße Katzen. Füttere sie, spiele mit der Feder, zieh sie an und sieh zu, wie deine Familie wächst. Hier passiert nie etwas Schlimmes.",
        soon="bald verfügbar", art="Ein cremefarbenes Kätzchen sitzt auf einer Wolke, daneben der Name Purr", shots="Bildschirmfotos",
        s1="Das Wohnzimmer mit zwei Katzen auf einem Teppich", s2="Eine Katze wird im Kleiderschrank angezogen", s3="Das Katzenalbum mit vielen Rassen",
        s4="Die Kätzchenstube mit einem Zauber-Ei", s5="Villa Miau, das Katzendorf", s6="Ein Minispiel mit einem Wollknäuel",
        f1h="Kümmern, das guttut", f1="Füttern, streicheln und spielen. Katzen schnurren, wenn du die richtige Stelle kraulst, dösen in der Sonne und freuen sich immer, dich zu sehen.",
        f2h="Über 60 Rassen zum Sammeln", f2="Adoptiere gewöhnliche Katzen mit Kibble, brüte neue aus Zauber-Eiern aus und öffne den Wunderkorb mit Tickets, die du beim Spielen gewinnst.",
        f3h="Richte dein Zuhause ein", f3="Sieben Deko-Plätze, Möbel, Tapeten und 120 Accessoires, von Baskenmützen bis zu Drachenflügeln. Mach Fotos zum Teilen.",
        f4h="Villa Miau", f4="Wenn das Haus voll ist, ziehen Katzen in ein sonniges Dorf auf dem Hügel. Sie schicken Postkarten und jede Katze kann wieder nach Hause kommen.",
        f5h="Gemeinsam spielen", f5="Füge Freunde per Code hinzu, besuche ihr Zuhause und findet bei einem Spieltreffen ein Ei, aus dem ihr beide ein Kätzchen bekommt. Kein Chat, keine Fremden.",
        f6h="Für Familien gemacht", f6="Ein neutraler Altersbildschirm, ein Kindermodus ohne Werbung und ohne Käufe, eine Sperre für Erwachsene und ein monatliches Ausgabenlimit.",
        fam="Für Erwachsene",
        g1="Kostenlos spielbar. Optionale Käufe haben feste Preise, werden vollständig angezeigt und sind nie zufällig. Ein Erwachsener legt das Monatslimit fest.",
        g2="Kinder spielen ohne Werbung, ohne persönliche Daten und ohne freien Text. Freunde kommen per Code dazu, Namen stammen aus einer ausgewählten Liste.",
        g3="Erinnerungen sind sanft, höchstens einmal am Tag, nie nachts, und sagen nie, dass eine Katze traurig oder hungrig ist.",
        g4='Alles steht in unserer <a href="privacy.html">Datenschutzerklärung</a>. Fragen: <a href="support.html">Hilfe</a>.',
    ),
    support=dict(
        h1="Hilfe", intro=f"Schreib an {MAIL}. Wir antworten innerhalb weniger Tage. Geht es um einen Kauf, nenne das Produkt und das Datum; Kartendaten brauchst du nie zu schicken.",
        faq="Häufige Fragen",
        q1="Wie lösche ich mein Konto und meine Daten?", a1='Im Spiel: Einstellungen → Kindersicherung → Daten → „Alle Daten löschen“. Dein Konto wird von unseren Servern entfernt und der Spielstand von deinem Gerät. Das lässt sich nicht rückgängig machen. Mehr: <a href="delete.html">Konto löschen</a>.',
        q2="Ich habe ein neues Handy. Wo ist mein Spiel?", a2="Dein Spiel gehört zu dem Gerät, auf dem es erstellt wurde. Die Verknüpfung mit deinem Apple- oder Google-Konto kommt bald; bis dahin schreib uns mit deinem Freundescode vom alten und vom neuen Handy, und wir übertragen es.",
        q3="Ein Kauf ist nicht angekommen.", a3="Öffne den Shop und tippe auf „Käufe wiederherstellen“. Fehlt er nach ein paar Minuten immer noch, schick uns den Produktnamen und das Bestelldatum.",
        q4="Werden die Katzen je traurig oder krank?", a4="Nein. Die Katzen in Purr werden nie krank, hungern nie wirklich und gehen nie für immer fort. Wenn du nach einer Weile zurückkommst, freuen sie sich einfach, dich zu sehen.",
        q5="Wie funktioniert die Kindersicherung?", a5="Einstellungen → Kindersicherung, hinter einer kurzen Rechenaufgabe, die nur ein Erwachsener beantworten sollte: Käufe aus, jeden Kauf bestätigen, Monatslimit, Benachrichtigungen und Ruhezeiten, Pausenerinnerungen.",
    ),
    delete=dict(
        h1="Konto löschen", h_game="Im Spiel (sofort)",
        l1="Öffne Purr und tippe auf das Zahnrad, um die <strong>Einstellungen</strong> zu öffnen.",
        l2="Beantworte die kurze Rechenaufgabe für Erwachsene, um die <strong>Kindersicherung</strong> zu öffnen.",
        l3="Tippe unter <strong>Daten</strong> auf <strong>Alle Daten löschen</strong> und bestätige mit einem zweiten Tippen. Du brauchst eine Internetverbindung.",
        h_mail="Per E-Mail",
        mail='Wenn das Spiel nicht mehr installiert ist, schreib an <a href="mailto:hello@purrgame.com?subject=Delete%20my%20Purr%20account">hello@purrgame.com</a> mit dem Betreff „Mein Purr-Konto löschen“ und, falls vorhanden, deinem Freundescode (Bildschirm Freunde, „Mein Code“). Wir löschen das Konto innerhalb von 30 Tagen und bestätigen es per E-Mail.',
        h_what="Was gelöscht wird", what="Dein Konto und alles darin: Katzen, Gegenstände, Kibble und Funkeln, Zuhause, Einstellungen, Altersgruppe, Freundescode, Freunde und Nachrichten. Käufe werden durch das Löschen nicht erstattet; Erstattungen richten sich nach den Regeln von Apple oder Google.",
        h_kept="Was aufbewahrt wird", kept='Kaufbelege, die Steuer- und Buchhaltungsrecht verlangen (Produkt, Datum, Bestellnummer des Stores), so lange das Gesetz es verlangt, sowie Meldungen, die du über andere Spieler gemacht hast, die wir aus Sicherheitsgründen behalten. Absturzberichte und anonyme Statistiken sind nicht mit deinem Konto verbunden und verfallen von selbst (90 Tage und 12 Monate). Siehe die <a href="privacy.html">Datenschutzerklärung</a>.',
    ),
)

T["fr"] = dict(
    index=dict(
        h1a="Adopte, câline et", h1b="collectionne des chats",
        lead="Purr est une petite maison chaleureuse pour des chats trop mignons. Nourris-les, joue avec la plume, habille-les et regarde ta famille grandir. Ici, rien de mal n'arrive jamais.",
        soon="bientôt", art="Un chaton crème assis sur un nuage, avec le nom Purr", shots="Captures d'écran",
        s1="Le salon avec deux chats sur un tapis", s2="Un chat habillé dans la garde-robe", s3="L'album des chats avec de nombreuses races",
        s4="La nurserie des chatons avec un œuf magique", s5="Villa Miau, le village des chats", s6="Un mini-jeu avec une pelote de laine",
        f1h="Des soins qui font du bien", f1="Nourris, caresse et joue. Les chats ronronnent quand tu trouves le bon endroit, font la sieste au soleil et sont toujours heureux de te voir.",
        f2h="Plus de 60 races à collectionner", f2="Adopte des chats communs avec des croquettes, fais éclore des œufs magiques et ouvre le Panier mystère avec les tickets gagnés en jouant.",
        f3h="Crée ton chez-toi", f3="Sept emplacements de décoration, des meubles, des papiers peints et 120 accessoires, du béret aux ailes de dragon. Prends des photos à partager.",
        f4h="Villa Miau", f4="Quand la maison est pleine, les chats s'installent dans un village ensoleillé sur la colline. Ils envoient des cartes postales et chacun peut revenir à la maison.",
        f5h="Jouez ensemble", f5="Ajoute des amis avec un code, visite leur maison et trouvez un œuf de Rencontre de jeu : chacun de vous reçoit un chaton. Pas de messagerie, pas d'inconnus.",
        f6h="Pensé pour les familles", f6="Un écran d'âge neutre, un mode enfant sans publicité ni achats, un contrôle réservé aux adultes et une limite de dépenses mensuelle.",
        fam="Pour les adultes",
        g1="Gratuit. Les achats facultatifs ont un prix fixe, affiché en entier, et ne sont jamais aléatoires. Un adulte fixe la limite mensuelle.",
        g2="Les enfants jouent sans publicité, sans données personnelles et sans texte libre. Les amis s'ajoutent avec un code et les noms viennent d'une liste choisie.",
        g3="Les rappels sont doux, au plus un par jour, jamais la nuit, et ne disent jamais qu'un chat est triste ou affamé.",
        g4='Tout est expliqué dans notre <a href="privacy.html">politique de confidentialité</a>. Des questions : <a href="support.html">aide</a>.',
    ),
    support=dict(
        h1="Aide", intro=f"Écris à {MAIL}. Nous répondons en quelques jours. S'il s'agit d'un achat, indique le produit et la date ; tu n'as jamais besoin d'envoyer tes données de carte.",
        faq="Questions fréquentes",
        q1="Comment supprimer mon compte et mes données ?", a1='Dans le jeu : Réglages → Contrôle parental → Données → « Supprimer toutes les données ». Ton compte est effacé de nos serveurs et la partie de ton appareil. C\'est définitif. Plus d\'infos : <a href="delete.html">supprimer ton compte</a>.',
        q2="J'ai changé de téléphone. Où est ma partie ?", a2="Ta partie est liée à l'appareil où elle a été créée. La liaison avec ton compte Apple ou Google arrive bientôt ; en attendant, écris-nous avec ton code ami de l'ancien et du nouveau téléphone et nous la transférerons.",
        q3="Un achat n'est pas arrivé.", a3="Ouvre la Boutique et utilise « Restaurer les achats ». S'il manque toujours après quelques minutes, envoie-nous le nom du produit et la date de la commande.",
        q4="Les chats peuvent-ils être tristes ou malades ?", a4="Non. Dans Purr, les chats ne tombent jamais malades, n'ont jamais vraiment faim et ne partent jamais pour de bon. Quand tu reviens après un moment, ils sont simplement heureux de te voir.",
        q5="Comment fonctionne le contrôle parental ?", a5="Réglages → Contrôle parental, derrière un petit calcul qu'un adulte doit résoudre : achats désactivés, approbation de chaque achat, limite mensuelle, notifications et heures calmes, rappels de pause.",
    ),
    delete=dict(
        h1="Supprimer ton compte", h_game="Depuis le jeu (immédiat)",
        l1="Ouvre Purr et touche la roue dentée pour ouvrir les <strong>Réglages</strong>.",
        l2="Réponds au petit calcul pour adultes pour ouvrir le <strong>Contrôle parental</strong>.",
        l3="Sous <strong>Données</strong>, touche <strong>Supprimer toutes les données</strong>, puis touche encore pour confirmer. Il faut une connexion internet.",
        h_mail="Par e-mail",
        mail='Si le jeu n\'est plus installé, écris à <a href="mailto:hello@purrgame.com?subject=Delete%20my%20Purr%20account">hello@purrgame.com</a> avec l\'objet « Supprimer mon compte Purr » et, si tu l\'as, ton code ami (écran Amis, « Mon code »). Nous supprimons le compte sous 30 jours et te le confirmons par e-mail.',
        h_what="Ce qui est supprimé", what="Ton compte et tout ce qu'il contient : chats, objets, croquettes et Étincelles, maison, réglages, tranche d'âge, code ami, amis et messages. Supprimer le compte ne rembourse pas les achats ; les remboursements suivent les règles d'Apple ou de Google.",
        h_kept="Ce qui est conservé", kept='Les justificatifs d\'achat exigés par la loi fiscale et comptable (produit, date, référence de commande de la boutique), aussi longtemps que la loi l\'exige, et les signalements que tu as faits sur d\'autres joueurs, que nous gardons pour la sécurité. Les rapports de plantage et les statistiques anonymes ne sont pas liés à ton compte et expirent d\'eux-mêmes (90 jours et 12 mois). Voir la <a href="privacy.html">politique de confidentialité</a>.',
    ),
)

T["ja"] = dict(
    index=dict(
        h1a="ネコを迎えて、なでて、", h1b="集めよう",
        lead="Purrは、とってもかわいいネコたちのための、あたたかい小さなおうち。ごはんをあげて、羽根で遊んで、着せかえて、家族がふえていくのを見守ろう。悪いことは何も起きません。",
        soon="近日公開", art="雲の上にすわるクリーム色の子ネコと、Purrの文字", shots="スクリーンショット",
        s1="ラグの上に2匹のネコがいるリビング", s2="クローゼットでネコを着せかえ", s3="たくさんの種類が並ぶネコ図鑑",
        s4="まほうのたまごがある子ネコの部屋", s5="ネコの村、ビラ・ミャウ", s6="毛糸玉で遊ぶミニゲーム",
        f1h="お世話で心がほっこり", f1="ごはん、なでなで、あそび。ちょうどいい場所をなでるとゴロゴロ、日なたでお昼寝、いつでもうれしそうに迎えてくれます。",
        f2h="60種類以上のネコを集めよう", f2="カリカリで普通のネコを迎え、まほうのたまごから新しいネコをかえし、遊んで手に入れたチケットでミステリーバスケットを開けよう。",
        f3h="おうちをかざろう", f3="7つのかざり枠、家具、壁紙、ベレー帽からドラゴンの羽まで120のアクセサリー。写真を撮ってシェアしよう。",
        f4h="ビラ・ミャウ", f4="おうちがいっぱいになると、ネコたちは丘の上の日あたりのいい村へ。絵はがきを送ってくれて、どのネコもおうちに帰ってこられます。",
        f5h="いっしょに遊ぼう", f5="コードでフレンドを追加して、おうちを訪ね、プレイデートのたまごを見つけよう。ふたりとも子ネコがもらえます。チャットなし、知らない人とのやりとりもなし。",
        f6h="家族みんなで安心", f6="年齢をたずねる中立的な画面、広告も購入もない子どもモード、おとな用の確認、毎月の使用上限。",
        fam="保護者の方へ",
        g1="基本プレイ無料。任意の購入は固定価格ですべて表示され、ランダムになることはありません。毎月の上限はおとなが決めます。",
        g2="子どもは広告なし、個人データなし、自由入力なしで遊べます。フレンドはコードで追加し、名前は用意されたリストから選びます。",
        g3="お知らせはやさしく、1日1回まで、夜には届かず、ネコが悲しい・おなかがすいたとは決して言いません。",
        g4='くわしくは<a href="privacy.html">プライバシーポリシー</a>をご覧ください。お問い合わせは<a href="support.html">サポート</a>へ。',
    ),
    support=dict(
        h1="サポート", intro=f"{MAIL} までご連絡ください。数日以内にお返事します。購入に関するお問い合わせは、商品名と日付をお知らせください。カード情報を送っていただく必要はありません。",
        faq="よくある質問",
        q1="アカウントとデータを削除するには？", a1='ゲーム内の「設定」→「保護者設定」→「データ」→「すべてのデータを削除」。アカウントはサーバーから、セーブデータは端末から削除されます。元に戻すことはできません。くわしくは<a href="delete.html">アカウントの削除</a>へ。',
        q2="スマホを変えました。ゲームはどこ？", a2="ゲームは作成した端末にひもづいています。Apple・Googleアカウントとの連携は準備中です。それまでは、古いスマホと新しいスマホのフレンドコードを添えてご連絡いただければ、データを移します。",
        q3="購入したものが届きません。", a3="ストアを開いて「購入を復元」をタップしてください。数分たっても届かない場合は、商品名と注文日をお送りください。",
        q4="ネコが悲しんだり病気になったりしますか？", a4="いいえ。Purrのネコは病気にならず、本当におなかをすかせることもなく、ずっといなくなることもありません。しばらくぶりに戻っても、うれしそうに迎えてくれます。",
        q5="保護者設定はどうなっていますか？", a5="「設定」→「保護者設定」。おとなだけが答えられる簡単な計算のあとで、購入オフ、購入ごとの承認、毎月の上限、通知とおやすみ時間、休憩のお知らせを設定できます。",
    ),
    delete=dict(
        h1="アカウントの削除", h_game="ゲームから（すぐに）",
        l1="Purrを開き、歯車ボタンをタップして<strong>設定</strong>を開きます。",
        l2="おとな用の簡単な計算に答えて<strong>保護者設定</strong>を開きます。",
        l3="<strong>データ</strong>の<strong>すべてのデータを削除</strong>をタップし、もう一度タップして確定します。インターネット接続が必要です。",
        h_mail="メールで",
        mail='ゲームをもうインストールしていない場合は、件名「Purrのアカウントを削除」で <a href="mailto:hello@purrgame.com?subject=Delete%20my%20Purr%20account">hello@purrgame.com</a> までご連絡ください。フレンドコード（フレンド画面の「わたしのコード」）があれば添えてください。30日以内に削除し、メールでお知らせします。',
        h_what="削除されるもの", what="アカウントとその中身すべて：ネコ、アイテム、カリカリとキラキラ、おうち、設定、年齢層、フレンドコード、フレンド、メッセージ。アカウントを削除しても購入代金は返金されません。返金はAppleまたはGoogleの規定に従います。",
        h_kept="保存されるもの", kept='税務・会計上の法律で必要な購入記録（商品、日付、ストアの注文番号）を法律が定める期間、また、ほかのプレイヤーについてあなたが行った通報を安全のために保存します。クラッシュレポートと匿名の統計はアカウントにひもづいておらず、自動的に消えます（90日と12か月）。<a href="privacy.html">プライバシーポリシー</a>もご覧ください。',
    ),
)

T["ko"] = dict(
    index=dict(
        h1a="고양이를 입양하고, 쓰다듬고,", h1b="모아요",
        lead="Purr는 아주 귀여운 고양이들을 위한 따뜻하고 작은 집이에요. 밥을 주고, 깃털로 놀아 주고, 옷을 입히며 가족이 늘어 가는 걸 지켜보세요. 여기서는 나쁜 일이 절대 없어요.",
        soon="곧 출시", art="구름 위에 앉은 크림색 아기 고양이와 Purr 이름", shots="스크린샷",
        s1="러그 위에 고양이 두 마리가 있는 거실", s2="옷장에서 고양이 꾸미기", s3="많은 품종이 있는 고양이 도감",
        s4="마법의 알이 있는 아기 고양이 방", s5="고양이 마을 빌라 미아우", s6="털실 뭉치 미니게임",
        f1h="기분 좋아지는 돌봄", f1="밥 주기, 쓰다듬기, 놀아 주기. 딱 좋은 곳을 쓰다듬으면 골골거리고, 햇볕에서 낮잠을 자고, 언제나 반갑게 맞아 줘요.",
        f2h="60가지가 넘는 품종 수집", f2="사료로 일반 고양이를 입양하고, 마법의 알에서 새 고양이를 부화시키고, 놀이로 얻은 티켓으로 미스터리 바구니를 열어요.",
        f3h="나만의 집 꾸미기", f3="7개의 꾸미기 자리, 가구, 벽지, 베레모부터 드래곤 날개까지 120가지 액세서리. 사진을 찍어 공유해요.",
        f4h="빌라 미아우", f4="집이 가득 차면 고양이들은 언덕 위 햇살 가득한 마을로 이사해요. 엽서를 보내 주고, 어떤 고양이든 다시 집으로 돌아올 수 있어요.",
        f5h="함께 놀아요", f5="코드로 친구를 추가하고, 집에 놀러 가고, 놀이 약속 알을 찾아요. 두 사람 모두 아기 고양이를 받아요. 채팅도, 낯선 사람도 없어요.",
        f6h="가족을 위해 만들었어요", f6="중립적인 나이 확인 화면, 광고와 구매가 없는 어린이 모드, 어른 확인 절차와 월별 지출 한도.",
        fam="보호자분들께",
        g1="무료로 즐길 수 있어요. 선택 구매는 가격이 고정되어 모두 표시되며, 절대 무작위가 아니에요. 월 한도는 어른이 정해요.",
        g2="아이들은 광고, 개인 정보, 자유 입력 없이 놀아요. 친구는 코드로 추가하고 이름은 정해진 목록에서 골라요.",
        g3="알림은 부드럽게, 하루 최대 한 번, 밤에는 오지 않으며, 고양이가 슬프거나 배고프다고 절대 말하지 않아요.",
        g4='자세한 내용은 <a href="privacy.html">개인정보 처리방침</a>을 참고하세요. 문의: <a href="support.html">고객 지원</a>.',
    ),
    support=dict(
        h1="고객 지원", intro=f"{MAIL}로 연락해 주세요. 며칠 안에 답변드려요. 구매 관련 문의는 상품과 날짜를 알려 주세요. 카드 정보는 절대 보내실 필요가 없어요.",
        faq="자주 묻는 질문",
        q1="계정과 데이터는 어떻게 삭제하나요?", a1='게임에서: 설정 → 보호자 설정 → 데이터 → "모든 데이터 삭제". 계정은 서버에서, 저장 데이터는 기기에서 삭제돼요. 되돌릴 수 없어요. 자세히: <a href="delete.html">계정 삭제</a>.',
        q2="휴대폰을 바꿨어요. 게임은 어디 있나요?", a2="게임은 처음 만든 기기에 연결되어 있어요. Apple·Google 계정 연동은 준비 중이에요. 그전까지는 이전 휴대폰과 새 휴대폰의 친구 코드를 적어 연락 주시면 옮겨 드려요.",
        q3="구매한 상품이 도착하지 않았어요.", a3='스토어를 열고 "구매 복원"을 눌러 주세요. 몇 분 뒤에도 없으면 상품 이름과 주문 날짜를 보내 주세요.',
        q4="고양이가 슬퍼하거나 아플 수 있나요?", a4="아니요. Purr의 고양이는 아프지 않고, 정말로 배고프지도 않으며, 영영 떠나지도 않아요. 한동안 지나 돌아와도 그저 반갑게 맞아 줘요.",
        q5="보호자 설정은 어떻게 작동하나요?", a5="설정 → 보호자 설정. 어른만 답할 수 있는 간단한 계산 뒤에서 구매 끄기, 구매마다 승인, 월 한도, 알림과 방해 금지 시간, 휴식 알림을 설정할 수 있어요.",
    ),
    delete=dict(
        h1="계정 삭제", h_game="게임에서 (즉시)",
        l1="Purr를 열고 톱니바퀴 버튼을 눌러 <strong>설정</strong>을 열어요.",
        l2="어른용 간단한 계산에 답해 <strong>보호자 설정</strong>을 열어요.",
        l3="<strong>데이터</strong>에서 <strong>모든 데이터 삭제</strong>를 누르고, 한 번 더 눌러 확인해요. 인터넷 연결이 필요해요.",
        h_mail="이메일로",
        mail='게임이 더 이상 설치되어 있지 않다면 제목을 "Purr 계정 삭제"로 하여 <a href="mailto:hello@purrgame.com?subject=Delete%20my%20Purr%20account">hello@purrgame.com</a>으로 연락해 주세요. 친구 코드(친구 화면의 "내 코드")가 있으면 함께 적어 주세요. 30일 안에 삭제하고 이메일로 알려 드려요.',
        h_what="삭제되는 것", what="계정과 그 안의 모든 것: 고양이, 아이템, 사료와 반짝이, 집, 설정, 연령대, 친구 코드, 친구, 메시지. 계정을 삭제해도 구매 금액은 환불되지 않아요. 환불은 Apple 또는 Google의 정책을 따라요.",
        h_kept="보관되는 것", kept='세법과 회계법이 요구하는 구매 기록(상품, 날짜, 스토어 주문 번호)은 법이 정한 기간 동안, 다른 플레이어에 대해 신고한 내용은 안전을 위해 보관해요. 오류 보고서와 익명 통계는 계정과 연결되지 않으며 자동으로 사라져요(90일, 12개월). <a href="privacy.html">개인정보 처리방침</a>을 참고하세요.',
    ),
)

T["zh-hant"] = dict(
    index=dict(
        h1a="領養、寵愛、", h1b="收集貓咪",
        lead="Purr 是一個溫暖的小家，住著超可愛的貓咪。餵牠們吃飯、用羽毛陪牠們玩、替牠們打扮，看著你的貓咪家族慢慢長大。這裡永遠不會發生壞事。",
        soon="即將推出", art="坐在雲朵上的奶油色小貓與 Purr 字樣", shots="螢幕截圖",
        s1="地毯上有兩隻貓咪的客廳", s2="在衣櫃裡替貓咪換裝", s3="收錄許多品種的貓咪圖鑑",
        s4="有魔法蛋的小貓育嬰室", s5="貓咪村子喵喵村", s6="毛線球小遊戲",
        f1h="讓人暖心的照顧", f1="餵食、撫摸、陪玩。摸對地方貓咪就會呼嚕呼嚕，在陽光下打盹，永遠開心地迎接你。",
        f2h="收集超過 60 種貓咪", f2="用飼料領養一般貓咪、從魔法蛋孵出新貓咪，再用玩遊戲贏來的票券打開神秘籃子。",
        f3h="佈置你的家", f3="7 個裝飾位置、家具、壁紙，以及從貝雷帽到龍翅膀的 120 種配件。拍照分享吧。",
        f4h="喵喵村", f4="家裡住滿時，貓咪會搬到山丘上陽光充足的小村子。牠們會寄明信片，每隻貓咪都能再回家。",
        f5h="一起玩", f5="用代碼加好友、拜訪他們的家，一起找到「一起玩」的蛋，兩個人都能得到一隻小貓。沒有聊天，也沒有陌生人。",
        f6h="為家庭打造", f6="中立的年齡畫面、沒有廣告和購買的兒童模式、大人驗證，以及每月消費上限。",
        fam="給大人的說明",
        g1="免費遊玩。選購項目價格固定且完整顯示，絕不隨機。每月上限由大人設定。",
        g2="孩子遊玩時沒有廣告、沒有個人資料、也不能自由輸入文字。好友用代碼加入，名字從精選清單中挑選。",
        g3="提醒很溫柔，一天最多一次，夜間不打擾，也絕不會說貓咪難過或餓了。",
        g4='詳情請見<a href="privacy.html">隱私權政策</a>。有問題請聯絡<a href="support.html">客服</a>。',
    ),
    support=dict(
        h1="客服", intro=f"請寫信至 {MAIL}，我們會在幾天內回覆。若與購買有關，請附上商品與日期；你永遠不需要提供信用卡資料。",
        faq="常見問題",
        q1="如何刪除我的帳號和資料？", a1='在遊戲中：設定 → 家長控制 → 資料 →「刪除所有資料」。帳號會從我們的伺服器刪除，存檔也會從裝置刪除，而且無法復原。詳情：<a href="delete.html">刪除你的帳號</a>。',
        q2="我換了手機，遊戲在哪裡？", a2="遊戲綁定在建立它的裝置上。與 Apple 或 Google 帳號連結的功能即將推出；在那之前，請附上舊手機與新手機的好友代碼寫信給我們，我們會幫你搬移。",
        q3="購買的東西沒有收到。", a3="打開商店並點選「恢復購買」。幾分鐘後仍沒有出現的話，請把商品名稱與訂單日期寄給我們。",
        q4="貓咪會難過或生病嗎？", a4="不會。Purr 的貓咪從不生病，也不會真的挨餓，更不會永遠離開。隔一段時間再回來，牠們依然開心地迎接你。",
        q5="家長控制怎麼運作？", a5="設定 → 家長控制，需要先答對一題只有大人該回答的簡單算術：關閉購買、每次購買需核准、每月上限、通知與安靜時段、休息提醒。",
    ),
    delete=dict(
        h1="刪除你的帳號", h_game="在遊戲中（立即生效）",
        l1="打開 Purr，點選齒輪按鈕開啟<strong>設定</strong>。",
        l2="回答大人用的簡單算術，開啟<strong>家長控制</strong>。",
        l3="在<strong>資料</strong>中點選<strong>刪除所有資料</strong>，再點一次確認。需要網路連線。",
        h_mail="透過電子郵件",
        mail='若已經沒有安裝遊戲，請以主旨「刪除我的 Purr 帳號」寫信至 <a href="mailto:hello@purrgame.com?subject=Delete%20my%20Purr%20account">hello@purrgame.com</a>，如有好友代碼（好友畫面的「我的代碼」）也請附上。我們會在 30 天內刪除帳號並以電子郵件通知你。',
        h_what="會刪除的資料", what="你的帳號及其中所有內容：貓咪、物品、飼料與星光、家、設定、年齡組、好友代碼、好友與訊息。刪除帳號不會退還購買款項；退款依 Apple 或 Google 的規定辦理。",
        h_kept="會保留的資料", kept='稅務與會計法規要求的購買紀錄（商品、日期、商店訂單編號）依法定期間保存，以及你檢舉其他玩家的紀錄，我們基於安全考量會保留。當機報告與匿名統計不會連結到你的帳號，並會自動失效（90 天與 12 個月）。請參閱<a href="privacy.html">隱私權政策</a>。',
    ),
)

for lang, parts in T.items():
    d = HERE / lang
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(INDEX.format(**parts["index"]), encoding="utf-8")
    (d / "support.html").write_text(SUPPORT.format(**parts["support"]), encoding="utf-8")
    (d / "delete.html").write_text(DELETE.format(**parts["delete"]), encoding="utf-8")
print("short pages written for", ", ".join(T))
