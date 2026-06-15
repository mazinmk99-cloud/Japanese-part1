import flet as ft
import random

# --- നിങ്ങളുടെ മുഴുവൻ വാക്കുകളും (N5 Vocabulary) ---
n5_vocab = {
    'どうぶつえん': ['മൃഗശാല (Zoo)', 'Doubutsuen'],
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
    'こんにちは': ['ഹലോ/ശുഭദിനം (Hello)', 'Konnichiwa'],
    'こんばんは': ['ശുഭസന്ധ്യ (Good evening)', 'Konbanwa'],
    'おやすみなさい': ['ശുഭരാത്രി (Good night)', 'Oyasuminasai'],
    'すみません': ['ക്ഷമിക്കണം (Excuse me/Sorry)', 'Sumimansen'],
    'ごめんなさい': ['എന്നോട് ക്ഷമിക്കൂ (I\'m sorry)', 'Gomennasai'],
    'ください': ['ദയവായി തരൂ (Please give me)', 'Kudasai'],
    'おねがいします': ['ദയവായി (Please/I request)', 'Onegaishimasu'],
    'どうぞ': ['ദാ പിടിച്ചോളൂ (Please/Here you go)', 'Douzo'],
    'どうも': ['നന്ദി - കാഷ്വൽ (Thanks - Casual)', 'Doumo'],
    'だいじょうぶ': ['സാരമില്ല/കുഴപ്പമില്ല (All right/OK)', 'Daijoubu'],
    'しつれいします': ['ഞാൻ ഇറങ്ങുന്നു/ക്ഷമിക്കണം (Excuse me/Goodbye)', 'Shitsureishimasu'],
    'いってきます': ['ഞാൻ പോയിട്ട് വരാം (I\'m leaving now)', 'Ittekimasu'],
    'いってらっしゃい': ['പോയിട്ട് വരൂ (Take care/See you)', 'Itterasshai'],
    'ただいま': ['ഞാൻ തിരിച്ചെത്തി (I\'m home)', 'Tadaima'],
    'おかえりなさい': ['സ്വാഗതം/തിരിച്ചെത്തിയോ (Welcome home)', 'Okaerinasai'],
    'いただきます': ['ഭക്ഷണത്തിന് മുൻപ് പറയുന്ന നന്ദി (Let\'s eat)', 'Itadakimasu'],
    'ごちそうさまでした': ['ഭക്ഷണത്തിന് ശേഷം പറയുന്ന നന്ദി (Thank you for meal)', 'Gochisousamadeshita'],
    'おめでとう': ['അഭിനന്ദനങ്ങൾ (Congratulations)', 'Omedetou'],
    'もしもし': ['ഹലോ - ഫോണിൽ (Hello on phone)', 'Moshimoshi'],
    'げんき': ['സുഖമാണോ? (Healthy/Well?)', 'Genki'],
    'いくら': ['എത്രയാണ് വില? (How much)', 'Ikura'],
    'いくつ': ['എത്ര എണ്ണം/എത്ര വയസ്സ്? (How many/How old)', 'Ikutsu'],
    'ここ': ['ഇവിടെ (Here)', 'Koko'],
    'そこ': ['അവിടെ (There)', 'Soko'],
    'あそこ': ['അങ്ങ് ദൂരെ (Over there)', 'Asoko'],
    'たくさん': ['ധാരാളം (A lot)', 'Takusan'],
    'すこし': ['കുറച്ച് (A little)', 'Sukoshi'],
    'ぜんぜん': ['ഒട്ടുമില്ല/തീരെയില്ല (Not at all)', 'Zenzen'],
    'たいへん': ['വളരെ/വലിയ ബുദ്ധിമുട്ട് (Very/Difficult)', 'Taihen'],
    'とても': ['വളരെ (Very)', 'Totemo'],
    'いつも': ['എപ്പോഴും (Always)', 'Itsumo'],
    'ときどき': ['ഇടയ്ക്കിടെ (Sometimes)', 'Tokidoki'],
    'よく': ['പലപ്പോഴും/നന്നായി (Often/Well)', 'Yoku'],
    'ゆっくり': ['പതുക്കെ (Slowly)', 'Yukkuri'],
    'すぐ': ['ഉടൻ തന്നെ (Immediately)', 'Sugu'],
    'もういちど': ['ഒന്നുകൂടി (One more time)', 'Mouichido'],
    'いっしょに': ['ഒരുമിച്ച് (Together)', 'Isshoni'],
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
    'きらい': ['വെറുപ്പ്/ഇಷ್ಟമില്ലാത്ത (Dislike)', 'Kirai'],
    'じょうず': ['സാമർത്ഥ്യമുള്ള (Skillful)', 'Jouzu'],
    'へた': ['സാമർത്ഥ്യം കുറഞ്ഞ (Unskillful)', 'Heta'],
    'ほしい': ['വേണം/ആഗ്രഹമുണ്ട് (Want)', 'Hoshii'],
    'いたい': ['വേദനയുള്ള (Painful)', 'Itai'],
    'あぶない': ['അപകടകരമായ (Dangerous)', 'Abunai'],
    'おもしろい': ['രസകരമായ (Interesting)', 'Omoshiroi'],
    'つまらない': ['ബോറടിപ്പിക്കുന്ന (Boring)', 'Tsumaranai'],
    'わかい': ['പ്രായം കുറഞ്ഞ (Young)', 'Wakai'],
    'かっこいい': ['കാണാൻ കൊള്ളാവുന്ന (Cool/Handsome)', 'Kakkoii'],
    'かわいい': ['ക്യൂട്ട് ആയ (Cute)', 'Kawaii'],
    'にほん': ['ജാപ്പനീസ് രാജ്യം (Japan)', 'Nihon'],
    'うた': ['പാട്ട് (Song)', 'Uta'],
    'え': ['ചിത്രം (Picture/Drawing)', 'E'],
    'あける': ['തുറക്കുക (To open)', 'Akeru'],
    'しめる': ['അടയ്ക്കുക (To close)', 'Shimeru'],
    'いれる': ['അകത്തേക്ക് ഇടുക/ചേർക്കുക (To insert/put in)', 'Ireru'],
    'だす': ['പുറത്തെടുക്കുക (To take out)', 'Dasu'],
    'つける': ['ഓൺ ചെയ്യുക (To turn on)', 'Tsukeru'],
    'けす': ['ഓഫ് ചെയ്യുക/മായ്ക്കുക (To turn off/erase)', 'Kesu'],
    'すわる': ['ഇരിക്കുക (To sit)', 'Suwaru'],
    'たつ': ['എഴുന്നേറ്റു നിൽക്കുക (To stand)', 'Tatsu'],
    'いう': ['പറയുക (To say)', 'Iu'],
    'おしえる': ['പഠിപ്പിച്ചു കൊടുക്കുക (To teach)', 'Oshieru'],
    'みせる': ['കാണിച്ചു കൊടുക്കുക (To show)', 'Miseru'],
    'おぼえる': ['പഠിക്കുക (To remember)', 'Oboeru'],
    'わすれる': ['മറന്നുപോവുക (To forget)', 'Wasureru'],
    'はじめる': ['തുടങ്ങുക (To start)', 'Hajimeru'],
    'まつ': ['കാത്തുനിൽക്കുക (To wait)', 'Matsu'],
    'よぶ': ['വിളിക്കുക (To call)', 'Yobu'],
    'あう': ['കണ്ടുമുട്ടുക (To meet)', 'Au'],
    'あげる': ['കൊടുക്കുക (To give)', 'Ageru'],
    'もらう': ['വാങ്ങുക (To receive)', 'Morau'],
    'てつだう': ['സഹായിക്കുക (To help)', 'Tetsudau'],
    'いち': ['ഒന്ന് (One)', 'Ichi'],
    'に': ['രണ്ട് (Two)', 'Ni'],
    'さん': ['മൂന്ന് (Three)', 'San'],
    'よん': ['നാല് (Four)', 'Yon'],
    'ご': ['അഞ്ച് (Five)', 'Go'],
    'ろく': ['ആറ് (Six)', 'Roku'],
    'なな': ['ഏഴ് (Seven)', 'Nana'],
    'ハち': ['എട്ട് (Hachi)', 'Hachi'],
    'きゅう': ['ഒൻപത് (Kyuu)', 'Kyuu'],
    'じゅう': ['പത്ത് (Juu)', 'Juu'],
    'ひゃく': ['നൂറ് (Hundred)', 'Hyaku'],
    'せん': ['ആയിരം (Thousand)', 'Sen'],
    'まん': ['പതിനായിരം (Ten thousand)', 'Man'],
    'げつようび': ['തിങ്കളാഴ്ച (Monday)', 'Getsuyoubi'],
    'かようび': ['ചൊവ്വാഴ്ച (Tuesday)', 'Kayoubi'],
    'すいようび': ['ബുധനാഴ്ച (Wednesday)', 'Suiyoubi'],
    'もくようび': ['വ്യാഴാഴ്ച (Thursday)', 'Mokuyoubi'],
    'きんようび': ['വെള്ളിയാഴ്ച (Friday)', 'Kinyoubi'],
    'どようび': ['ശനിയാഴ്ച (Saturday)', 'Doyoubi'],
    'にちようび': ['ഞായറാഴ്ച (Sunday)', 'Nichiyoubi'],
    'ことし': ['ഈ വർഷം (This year)', 'Kotoshi'],
    'きょねん': ['കഴിഞ്ഞ വർഷം (Last year)', 'Kyonen'],
    'らいねん': ['അടുത്ത വർഷം (Next year)', 'Rainen'],
    'はる': ['വസന്തകാലം (Spring)', 'Haru'],
    'なつ': ['വേനൽക്കാലം (Summer)', 'Natsu'],
    'あき': ['ശരത്കാലം (Autumn)', 'Aki'],
    'ふゆ': ['ശീതകാലം (Winter)', 'Fuyu'],
    'てんきよほう': ['കാലാവസ്ഥ പ്രവചനം (Weather forecast)', 'Tenkiyohou'],
    'みず': ['വെള്ളം (Water)', 'Mizu'],
    'おちゃ': ['പച്ചച്ചായ (Green tea)', 'Ocha'],
    'こーひー': ['കോഫി (Coffee)', 'Koohii'],
    'びーる': ['ബിയർ (Beer)', 'Biiru'],
    'ぱん': ['റൊട്ടി/ബ്രെഡ് (Bread)', 'Pan'],
    'たまご': ['മുട്ട (Egg)', 'Tamago'],
    'ちきゅう': ['ഭൂമി (Earth)', 'Chikyuu'],
    'せかい': ['ലോകം (World)', 'Sekai'],
    'しぜん': ['പ്രകൃതി (Nature)', 'Shizen'],
    'じてんしゃ': ['സൈക്കിൾ (Bicycle)', 'Jitensha'],
    'じどうしゃ': ['കാർ (Car)', 'Jidousha'],
    'ひこうき': ['വിമാനം (Airplane)', 'Hikouki'],
    'えき': ['റെയിൽവേ സ്റ്റേഷൻ (Station)', 'Eki'],
    'てがみ': ['കത്ത് (Letter)', 'Tegami'],
    'ほん': ['പുസ്തകം (Book)', 'Hon'],
    'じしょ': ['നിഘണ്ടു (Dictionary)', 'Jisho'],
    'かさ': ['കുട (Umbrella)', 'Kasa'],
    'くつ': ['ഷൂസ് (Shoes)', 'Kutsu'],
    'まど': ['ജാലകം (Window)', 'Mado'],
    'どあ': ['വാതിൽ (Door)', 'Doa'],
    'がっこう': ['സ്കൂൾ (School)', 'Gakkou'],
    'びょういん': ['ആശുപത്രി (Hospital)', 'Byouin'],
    'みせ': ['കട (Shop)', 'Mise'],
    'かいしゃ': ['കമ്പനി (Company)', 'Kaisha'],
    'しごと': ['ജോലി (Job)', 'Shigoto'],
    'うみ': ['കടൽ (Sea)', 'Umi'],
    'やま': ['മല (Mountain)', 'Yama'],
    'かわ': ['പുഴ (River)', 'Kawa'],
    'まち': ['നഗരം/ടൗൺ (Town)', 'Machi'],
    'みち': ['വഴി (Road)', 'Michi'],
    'はし': ['പാലം (Bridge)', 'Hashi']
}

# --- ഹിരാഗാന (Hiragana Dictionary) ---
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

def main(page: ft.Page):
    page.title = "Mazin's Learning Quest"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    COLOR_LUFFY_RED = "#D32F2F"
    COLOR_STRAW_YELLOW = "#E0A82F"
    COLOR_ZORO_GREEN = "#2E7D32"

    # സ്ക്രീനിൽ വാക്കുകൾ കാണിക്കാനുള്ള ടെക്സ്റ്റ് ബോക്സുകൾ (Cards)
    display_character = ft.Text("Let's Learn!", size=45, weight="bold", text_align=ft.TextAlign.CENTER)
    display_meaning = ft.Text("ബട്ടണിൽ ക്ലിക്ക് ചെയ്യുക", size=20, color="grey", text_align=ft.TextAlign.CENTER)

    # Vocabulary പഠിക്കാനുള്ള ഫംഗ്ഷൻ
    def vocab_clicked(e):
        random_word = random.choice(list(n5_vocab.keys()))
        details = n5_vocab[random_word]
        meaning = details[0]
        reading = details[1]
        
        display_character.value = random_word
        display_meaning.value = f"({reading})\n{meaning}"
        display_meaning.color = COLOR_ZORO_GREEN
        page.update()

    # Hiragana പഠിക്കാനുള്ള ഫംഗ്ഷൻ
    def hiragana_clicked(e):
        random_char = random.choice(list(hiragana_dict.keys()))
        reading = hiragana_dict[random_char]
        
        display_character.value = random_char
        display_meaning.value = reading.upper()
        display_meaning.color = COLOR_LUFFY_RED
        page.update()

    # പ്രധാന ഡിസൈൻ (UI Layout)
    main_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(height=20),
            ft.Text("Mazin's Learning Quest", size=25, weight="bold", color=COLOR_LUFFY_RED),
            ft.Container(height=40),
            
            # വാക്കും അർത്ഥവും കാണിക്കുന്ന ബോക്സ്
            ft.Container(
                content=ft.Column(
                    [display_character, display_meaning], 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                height=200,
                bgcolor="#f0f0f0",
                border_radius=15,
                padding=20
            ),
            
            ft.Container(height=40),
            
            # ബട്ടണുകൾ
            ft.ElevatedButton("📚 Vocabulary Study", bgcolor=COLOR_STRAW_YELLOW, on_click=vocab_clicked, width=250, height=50),
            ft.Container(height=15),
            ft.ElevatedButton("📝 Hiragana Study", bgcolor=COLOR_STRAW_YELLOW, on_click=hiragana_clicked, width=250, height=50)
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # ആപ്പിലേക്ക് എല്ലാം ആഡ് ചെയ്യുന്നു
    page.add(
        ft.Stack(
            controls=[
                main_column,
                ft.Image(src="assets/icon.png", width=50, top=0, right=0) # ലൂഫി ഐക്കൺ
            ]
        )
    )

ft.app(target=main)

