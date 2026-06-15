import flet as ft
import random

# --- Vocabulary Data ---
vocab_data = {
    'どうぶつえん': ['മൃഗശാല', 'Zoo'],
    'いりぐち': ['പ്രവേശന വഴി (Entrance)', 'Iriguchi'],
    'でぐち': ['പുറത്തുകടക്കുന്ന വഴി (Exit)', 'Deguchi'],
    'みぎ': ['വലത് (Right)', 'Migi'],
    'ひだり': ['ഇടത് (Left)', 'Hidari'],
    'まえ': ['മുൻപിൽ (Front/Before)', 'Mae'],
    'うしろ': ['പുറകിൽ (Back/Behind)', 'Ushiro'],
    'なか': ['ഉള്ളിൽ (Inside)', 'Naka'],
    'そと': ['പുറത്ത് (Outside)', 'Soto'],
    'うえ': ['മുകളിൽ (Up/Above)', 'Ue'],
    'した': ['താഴെ (Down/Below)', 'Shita'],
    'となり': ['അടുത്ത് (Next to)', 'Tonari'],
    'ちかく': ['അടുത്ത്/സമീപം (Near)', 'Chikaku'],
    'とおい': ['ദൂരെ (Far)', 'Tooi'],
    'ちかい': ['അടുത്തുള്ള (Close/Near)', 'Chikai'],
    'おじいさん': ['മുത്തശ്ശൻ (Grandfather)', 'Ojiisan'],
    'おばあさん': ['മുത്തശ്ശി (Grandmother)', 'Obaasan'],
    'おじさん': ['അമ്മാവൻ (Uncle)', 'Ojisan'],
    'おばさん': ['അമ്മായി (Aunt)', 'Obasan'],
    'いとこ': ['കസിൻ (Cousin)', 'Itoko'],
    'きょうだい': ['സഹോദരങ്ങൾ (Siblings)', 'Kyoudai'],
    'さいふ': ['പേഴ്സ് (Wallet)', 'Saifu'],
    'かぎ': ['താക്കോൽ (Key)', 'Kagi'],
    'みやげ': ['സമ്മാനം/ഓർമ്മച്ചിഹ്നം (Souvenir)', 'Miyage'],
    'おもちゃ': ['കളിപ്പാട്ടം (Toy)', 'Omocha'],
    'かんじ': ['കാൻജി (Kanji)', 'Kanji'],
    'ぶんしょう': ['വാചകം (Sentence)', 'Bunshou'],
    'ことば': ['വാക്ക് (Word/Language)', 'Kotoba'],
    'とし': ['വർഷം/പ്രായം (Year/Age)', 'Toshi'],
    'たんじょうび': ['ജന്മദിനം (Birthday)', 'Tanjoubi'],
    'いみ': ['അർത്ഥം (Meaning)', 'Imi'],
    'はじめまして': ['കണ്ടതിൽ സന്തോഷം (Nice to meet you)', 'Hajimemashite'],
    'どうぞよろしく': ['ദയവായി എന്നെ പരിഗണിക്കുക (Pleased to meet you)', 'Douzo yoroshiku'],
    'わたし': ['ഞാൻ (I/Me)', 'Watashi'],
    'あなた': ['നീ/നിങ്ങൾ (You)', 'Anata'],
    'かれ': ['അവൻ (He)', 'Kare'],
    'かのじょ': ['അവൾ (She)', 'Kanojo'],
    'わたしたち': ['ഞങ്ങൾ (We)', 'Watashitachi'],
    'みなさん': ['എല്ലാവരും (Everyone)', 'Minasan'],
    'こんにちは': ['ഹലോ/ശുഭദിനം (Hello/Good afternoon)', 'Konnichiwa'],
    'こんばんは': ['ശുഭസന്ധ്യ (Good evening)', 'Konbanwa'],
    'おやすみなさい': ['ശുഭരാത്രി (Good night)', 'Oyasuminasai'],
    'おやすみ': ['ശുഭരാത്രി - കാഷ്വൽ (Good night - Casual)', 'Oyasumi'],
    'すみません': ['ക്ഷമിക്കണം/എക്സ്ക്യൂസ് മീ (Excuse me/Sorry)', 'Sumimansen'],
    'ごめんなさい': ['എന്നോട് ക്ഷമിക്കൂ (I\'m sorry)', 'Gomennasai'],
    'ください': ['ദയവായി തരൂ (Please give me)', 'Kudasai'],
    'おねがいします': ['ദയവായി (Please/I request)', 'Onegaishimasu'],
    'どうぞ': ['ദാ പിടിച്ചോളൂ/ആവാമല്ലോ (Please/Here you go)', 'Douzo'],
    'どうも': ['നന്ദി - കാഷ്വൽ (Thanks - Casual)', 'Doumo'],
    'だいじょうぶ': ['സാരമില്ല/കുഴപ്പമില്ല (All right/OK)', 'Daijoubu'],
    'しつれいします': ['ഞാൻ ഇറങ്ങുന്നു/ക്ഷമിക്കണം (Excuse me/Goodbye)', 'Shitsureishimasu'],
    'いってきます': ['ഞാൻ പോയിട്ട് വരാം (I\'m leaving now)', 'Ittekimasu'],
    'いってらっしゃい': ['പോയിട്ട് വരൂ (Take care/See you)', 'Itterasshai'],
    'ただいま': ['ഞാൻ തിരിച്ചെത്തി (I\'m home)', 'Tadaima'],
    'おかえりなさい': ['സ്വാഗതം/തിരിച്ചെത്തിയോ (Welcome home)', 'Okaerinasai'],
    'いただきます': ['ഭക്ഷണത്തിന് മുൻപ് പറയുന്ന നന്ദി (Let\'s eat)', 'Itadakimasu'],
    'ごちそうさまでした': ['ഭക്ഷണത്തിന് ശേഷം പറയുന്ന നന്ദി (Thank you for the meal)', 'Gochisousamadeshita'],
    'おめでとう': ['അഭിനന്ദനങ്ങൾ (Congratulations)', 'Omedetou'],
    'もしもし': ['ഹലോ - ഫോണിൽ (Hello on phone)', 'Moshimoshi'],
    'げんき': ['സുഖമാണോ? (Healthy/Well?)', 'Genki'],
    'おげんきですか': ['സുഖമാണോ? - ഫോർമൽ (How are you?)', 'Ogenkideska'],
    'そうですね': ['അതെ അങ്ങനെയൊക്കെ തന്നെ (That\'s right/Let me see)', 'Soudesune'],
    'ほんとう': ['സത്യമാണോ/ശരിക്കും? (Really?)', 'Hontou'],
    'ちょっと': ['കുറച്ച്/ഒരു മിനിറ്റ് (A little/Just a moment)', 'Chotto'],
    'いくら': ['എത്രയാണ് വില? (How much)', 'Ikura'],
    'いくつ': ['എത്ര എണ്ണം/എത്ര വയസ്സ്? (How many/How old)', 'Ikutsu'],
    'どの': ['ഏത് (Which)', 'Dono'],
    'どれ': ['ഏതാണ് (Which one)', 'Dore'],
    'ここ': ['ഇവിടെ (Here)', 'Koko'],
    'そこ': ['അവിടെ (There)', 'Soko'],
    'あそこ': ['അങ്ങ് ദൂരെ (Over there)', 'Asoko'],
    'こちら': ['ഈ വശത്തേക്ക്/ഇദ്ദേഹം (This way/This person)', 'Kochira'],
    'そちら': ['ആ വശത്തേക്ക് (That way)', 'Sochira'],
    'あちら': ['അങ്ങ് ദൂരെ വശത്തേക്ക് (That way over there)', 'Achira'],
    'どちら': ['ഏത് വശത്തേക്ക് (Which way)', 'Dochira'],
    'こんな': ['ഇങ്ങനെയുള്ള (This kind of)', 'Konna'],
    'そんな': ['അങ്ങനെയുള്ള (That kind of)', 'Sonna'],
    'あんな': ['അങ്ങനെയുള്ള - ദൂരെ (That kind of over there)', 'Anna'],
    'どんな': ['എങ്ങനെയുള്ള (What kind of)', 'Donna'],
    'こう': ['ഇതുപോലെ (In this way)', 'Kou'],
    'そう': ['അതുപോലെ (In that way)', 'Sou'],
    'ああ': ['അതുപോലെ - ദൂരെ (In that way over there)', 'Aa'],
    'どう': ['എങ്ങനെ (How)', 'Dou'],
    'たくさん': ['ധാരാളം (A lot)', 'Takusan'],
    'すこし': ['കുറച്ച് (A little)', 'Sukoshi'],
    'ぜんぜん': ['ഒട്ടുമില്ല/തീരെയില്ല (Not at all)', 'Zenzen'],
    'たいへん': ['വളരെ/വലിയ ബുദ്ധിമുട്ട് (Very/Difficult)', 'Taihen'],
    'とても': ['വളരെ (Very)', 'Totemo'],
    'あまり': ['അത്രയ്ക്കില്ല (Not very much)', 'Amari'],
    'いつも': ['എപ്പോഴും (Always)', 'Itsumo'],
    'ときどき': ['ഇടയ്ക്കിടെ (Sometimes)', 'Tokidoki'],
    'よく': ['പലപ്പോഴും/നന്നായി (Often/Well)', 'Yoku'],
    'ゆっくり': ['പതുക്കെ (Slowly)', 'Yukkuri'],
    'すぐ': ['ഉടൻ തന്നെ (Immediately)', 'Sugu'],
    'もういちど': ['ഒന്നുകൂടി (One more time)', 'Mouichido'],
    'いっしょに': ['ഒരുമിച്ച് (Together)', 'Isshoni'],
    'おなじ': ['ഒരേപോലെ (Same)', 'Onaji'],
    'ほか': ['മറ്റുള്ളവ (Other)', 'Hoka'],
    'じぶん': ['സ്വയം (Oneself)', 'Jibun'],
    'しんせつ': ['ദയയുള്ള (Kind)', 'Shinsetsu'],
    'べんり': ['സൗകര്യപ്രദമായ (Convenient)', 'Benri'],
    'ふべん': ['അസൗകര്യമുള്ള (Inconvenient)', 'Fuben'],
    'ゆうめい': ['പ്രശസ്തമായ (Famous)', 'Yuumei'],
    'きれい': ['ഭംഗിയുള്ള/വൃത്തിയുള്ള (Beautiful/Clean)', 'Kirei'],
    'にぎやか': ['ആളുകൾ നിറഞ്ഞ/ബഹളമുള്ള (Lively)', 'Nigiyaka'],
    'しずか': ['ശബ്ദമില്ലാത്ത/ശാന്തമായ (Quiet)', 'Shizuka'],
    'ひま': ['വെറുതെയിരിക്കുന്ന സമയം (Free time)', 'Hima'],
    'いそがしい': ['തിരക്കുള്ള (Busy)', 'Isogashii'],
    'すき': ['ഇഷ്ടം (Like)', 'Suki'],
    'きらい': ['വെറുപ്പ്/ഇഷ്ടമില്ലാത്ത (Dislike)', 'Kirai'],
    'じょうず': ['സാമർത്ഥ്യമുള്ള (Skillful)', 'Jouzu'],
    'へた': ['സാമർത്ഥ്യം കുറഞ്ഞ (Unskillful)', 'Heta'],
    'ほしい': ['വേണം/ആഗ്രഹമുണ്ട് (Want)', 'Hoshii'],
    'いたい': ['വേദനയുള്ള (Painful)', 'Itai'],
    'あぶない': ['അപകടകരമായ (Dangerous)', 'Abunai'],
    'おもしろい': ['രസകരമായ (Interesting)', 'Omoshiroi'],
    'つまらない': ['ബോറടിപ്പിക്കുന്ന (Boring)', 'Tsumaranai'],
    'わかい': ['പ്രായം കുറഞ്ഞ (Young)', 'Wakai'],
    'かっこいい': ['കാണാൻ കൊള്ളാവുന്ന/സുന്ദരനായ (Cool/Handsome)', 'Kakkoii'],
    'かわいい': ['ക്യൂട്ട് ആയ/സുന്ദരിയായ (Cute)', 'Kawaii'],
    'にほん': ['ജാപ്പനീസ് രാജ്യം (Japan)', 'Nihon'],
    'しゅみ': ['വിനോദം (Hobby)', 'Shumi'],
    'うた': ['പാട്ട് (Song)', 'Uta'],
    'え': ['ചിത്രം (Picture/Drawing)', 'E'],
    'すぽーつ': ['കായികം (Sports)', 'Supootsu'],
    'だんす': ['നൃത്തം (Dance)', 'Dansu'],
    'かめら': ['ക്യാമറ (Camera)', 'Kamera'],
    'ぱそこん': ['കമ്പ്യൂട്ടർ (PC)', 'Pasokon'],
    'あにめ': ['ആനിമേഷൻ/ആниമേ (Anime)', 'Anime'],
    'げーむ': ['ഗെയിം (Game)', 'Geemu'],
    'てにす': ['ടെന്നീസ് (Tennis)', 'Tenisu']
    # ... ബാക്കി വാക്കുകൾ ഇതിൽ തന്നെ ഉണ്ടാകും ...
}

# --- Hiragana Letters ---
hiragana_groups = {
    "Basic": {
        'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
        'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
        'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so'
    },
    "Tenten": {
        'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
        'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo'
    },
    "Maru": {
        'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po'
    }
}

def main(page: ft.Page):
    page.title = "Mazin's Learning Quest"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # BGM Setup (Persistent in overlay)
    bgm = ft.Audio(src="bgm.mp3", autoplay=True, loop=True)
    page.overlay.append(bgm)

    # Routing
    def route_change(route):
        page.views.clear()
        
        # --- HOME ---
        if page.route == "/":
            page.views.append(ft.View("/", [
                ft.AppBar(title=ft.Text("Mazin's Quest"), bgcolor=ft.colors.RED_700, color="white"),
                ft.ElevatedButton("📚 Vocabulary", on_click=lambda _: page.go("/vocab")),
                ft.ElevatedButton("📝 Hiragana Letters", on_click=lambda _: page.go("/letters"))
            ]))
            
        # --- VOCABULARY PAGE ---
        elif page.route == "/vocab":
            word_display = ft.Text("Press Next", size=40, weight="bold")
            meaning_display = ft.Text("", size=20)
            
            def next_word(e):
                word = random.choice(list(vocab_data.keys()))
                word_display.value = word
                meaning_display.value = f"{vocab_data[word][0]} | {vocab_data[word][1]}"
                page.update()

            page.views.append(ft.View("/vocab", [
                ft.AppBar(title=ft.Text("Vocabulary Study"), leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")), bgcolor=ft.colors.RED_700, color="white"),
                ft.Container(content=ft.Column([word_display, meaning_display]), padding=30),
                ft.ElevatedButton("Next Word", on_click=next_word)
            ]))

        # --- HIRAGANA PAGE ---
        elif page.route == "/letters":
            letter_display = ft.Text("あ", size=60)
            roman_display = ft.Text("a", size=20)
            
            def next_letter(e):
                group_name = random.choice(list(hiragana_groups.keys()))
                char = random.choice(list(hiragana_groups[group_name].keys()))
                letter_display.value = char
                roman_display.value = hiragana_groups[group_name][char]
                page.update()

            page.views.append(ft.View("/letters", [
                ft.AppBar(title=ft.Text("Hiragana Letters"), leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")), bgcolor=ft.colors.RED_700, color="white"),
                ft.Container(content=ft.Column([letter_display, roman_display]), padding=30),
                ft.ElevatedButton("Next Letter", on_click=next_letter)
            ]))
        
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
