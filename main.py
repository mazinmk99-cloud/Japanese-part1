import flet as ft
import random

# --- വൊക്കാബുലറി ഡാറ്റ (100 വാക്കുകൾ) ---
vocab_data = {
    "お母さん": ["അമ്മ (Mother)", "Mother", "Okaasan"],
    "お父さん": ["അച്ഛൻ (Father)", "Father", "Otousan"],
    "ありがとう": ["നന്ദി", "Thank you", "Arigatou"],
    "こんにちは": ["നമസ്കാരം (ഉച്ചയ്ക്ക്)", "Hello/Good afternoon", "Konnichiwa"],
    "おはよう": ["സുപ്രഭാതം", "Good morning", "Ohayou"],
    "さようなら": ["വിട", "Goodbye", "Sayounara"],
    "行く": ["പോകുക", "Go", "Iku"],
    "来る": ["വരുക", "Come", "Kuru"],
    "食べる": ["കഴിക്കുക", "Eat", "Taberu"],
    "飲む": ["കുടിക്കുക", "Drink", "Nomu"],
    "見る": ["കാണുക", "See/Watch", "Miru"],
    "聞く": ["കേൾക്കുക", "Listen/Ask", "Kiku"],
    "読む": ["വായിക്കുക", "Read", "Yomu"],
    "書く": ["എഴുതുക", "Write", "Kaku"],
    "話す": ["സംസാരിക്കുക", "Speak", "Hanasu"],
    "買う": ["വാങ്ങുക", "Buy", "Kau"],
    "教える": ["പഠിപ്പിക്കുക", "Teach", "Oshieru"],
    "寝る": ["ഉറങ്ങുക", "Sleep", "Neru"],
    "起きる": ["ഉണരുക", "Wake up", "Okiru"],
    "座る": ["ഇരിക്കുക", "Sit", "Suwaru"],
    "立つ": ["നിൽക്കുക", "Stand", "Tatsu"],
    "走る": ["ഓടുക", "Run", "Hashiru"],
    "歩く": ["നടക്കുക", "Walk", "Aruku"],
    "待つ": ["കാത്തിരിക്കുക", "Wait", "Matsu"],
    "遊ぶ": ["കളിക്കുക", "Play", "Asobu"],
    "泳ぐ": ["നീന്തുക", "Swim", "Oyogu"],
    "入る": ["പ്രവേശിക്കുക", "Enter", "Hairu"],
    "出る": ["പുറത്തുപോവുക", "Exit/Leave", "Deru"],
    "開ける": ["തുറക്കുക", "Open", "Akeru"],
    "閉める": ["അടയ്ക്കുക", "Close", "Shimeru"],
    "仕事": ["ജോലി", "Work/Job", "Shigoto"],
    "勉強": ["പഠനം", "Study", "Benkyou"],
    "水": ["വെള്ളം", "Water", "Mizu"],
    "お茶": ["ചായ", "Tea", "Ocha"],
    "ご飯": ["ഭക്ഷണം", "Rice/Meal", "Gohan"],
    "パン": ["റൊട്ടി", "Bread", "Pan"],
    "魚": ["മത്സ്യം", "Fish", "Sakana"],
    "肉": ["ഇറച്ചി", "Meat", "Niku"],
    "卵": ["മുട്ട", "Egg", "Tamago"],
    "りんご": ["ആപ്പിൾ", "Apple", "Ringo"],
    "車": ["കാർ", "Car", "Kuruma"],
    "電車": ["ട്രെയിൻ", "Train", "Densha"],
    "自転車": ["സൈക്കിൾ", "Bicycle", "Jitensha"],
    "飛行機": ["വിമാനം", "Airplane", "Hikouki"],
    "駅": ["സ്റ്റേഷൻ", "Station", "Eki"],
    "学校": ["സ്കൂൾ", "School", "Gakkou"],
    "先生": ["അধ്യാപകൻ", "Teacher", "Sensei"],
    "学生": ["വിദ്യാർത്ഥി", "Student", "Gakusei"],
    "犬": ["നായ", "Dog", "Inu"],
    "猫": ["പൂച്ച", "Cat", "Neko"],
    "本": ["പുസ്തകം", "Book", "Hon"],
    "手紙": ["കത്ത്", "Letter", "Tegami"],
    "時計": ["ക്ലോക്ക്", "Clock/Watch", "Tokei"],
    "靴": ["ഷൂസ്", "Shoes", "Kutsu"],
    "服": ["വസ്ത്രം", "Clothes", "Fuku"],
    "家": ["വീട്", "House", "Ie"],
    "部屋": ["മുറി", "Room", "Heya"],
    "窓": ["ജനൽ", "Window", "Mado"],
    "ドア": ["വാതിൽ", "Door", "Doa"],
    "机": ["മേശ", "Desk", "Tsukue"],
    "椅子": ["കസേര", "Chair", "Isu"],
    "お金": ["പണം", "Money", "Okane"],
    "今日": ["ഇന്ന്", "Today", "Kyou"],
    "明日": ["നാളെ", "Tomorrow", "Ashita"],
    "昨日": ["ഇന്നലെ", "Yesterday", "Kinou"],
    "今": ["ഇപ്പോൾ", "Now", "Ima"],
    "朝": ["രാവിലെ", "Morning", "Asa"],
    "昼": ["ഉച്ച", "Noon/Daytime", "Hiru"],
    "夜": ["രാത്രി", "Night", "Yoru"],
    "月曜日": ["തിങ്കൾ", "Monday", "Getsuyoubi"],
    "火曜日": ["ചൊവ്വ", "Tuesday", "Kayoubi"],
    "水曜日": ["ബുധൻ", "Wednesday", "Suiyoubi"],
    "木曜日": ["വ്യാഴം", "Thursday", "Mokuyoubi"],
    "金曜日": ["വെള്ളി", "Friday", "Kinyoubi"],
    "土曜日": ["ശനി", "Saturday", "Doyoubi"],
    "日曜日": ["ഞായർ", "Sunday", "Nichiyoubi"],
    "春": ["വസന്തം", "Spring", "Haru"],
    "夏": ["വേനൽക്കാലം", "Summer", "Natsu"],
    "秋": ["ശരത്കാലം", "Autumn", "Aki"],
    "冬": ["ശൈത്യകാലം", "Winter", "Fuyu"],
    "天気": ["കാലാവസ്ഥ", "Weather", "Tenki"],
    "雨": ["മഴ", "Rain", "Ame"],
    "雪": ["മഞ്ഞ്", "Snow", "Yuki"],
    "風": ["കാറ്റ്", "Wind", "Kaze"],
    "山": ["മല", "Mountain", "Yama"],
    "川": ["പുഴ", "River", "Kawa"],
    "海": ["കടൽ", "Sea", "Umi"],
    "空": ["ആകാശം", "Sky", "Sora"],
    "花": ["പൂവ്", "Flower", "Hana"],
    "赤い": ["ചുവന്ന", "Red", "Akai"],
    "青い": ["നീല", "Blue", "Aoi"],
    "白い": ["വെളുത്ത", "White", "Shiroi"],
    "黒い": ["കറുത്ത", "Black", "Kuroi"],
    "大きい": ["വലിയ", "Big", "Ookii"],
    "小さい": ["ചെറിയ", "Small", "Chiisai"],
    "新しい": ["പുതിയ", "New", "Atarashii"],
    "古い": ["പഴയ", "Old", "Furui"],
    "高い": ["വിലകൂടിയ", "High/Expensive", "Takai"],
    "安い": ["വിലകുറഞ്ഞ", "Cheap", "Yasui"],
    "好き": ["ഇഷ്ടം", "Like", "Suki"],
    "嫌い": ["ഇഷ്ടമില്ലാത്ത", "Dislike", "Kirai"]
}

hiragana_chars = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
katakana_chars = ["ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メモ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン"]

kanji_n5 = {
    "一": "One (Ichi)", "二": "Two (Ni)", "三": "Three (San)", "四": "Four (Yon)", "五": "Five (Go)",
    "六": "Six (Roku)", "七": "Seven (Nana)", "八": "Eight (Hachi)", "九": "Nine (Kyuu)", "十": "Ten (Juu)",
    "日": "Day/Sun (Nichi)", "月": "Month/Moon (Tsuki)", "火": "Fire (Hi)", "水": "Water (Mizu)", "木": "Tree (Ki)"
}

grammar_lessons = [
    {"title": "Lesson 1: Particles は (wa) & です (desu)", "content": "A は B です (A wa B desu) means 'A is B'.\nEx: 私は学生です (Watashi wa gakusei desu) - I am a student (ഞാൻ ഒരു വിദ്യാർത്ഥിയാണ്)."},
    {"title": "Lesson 2: Question Particle か (ka)", "content": "Add 'ka' at the end of a sentence to make it a question.\nEx: お元気ですか (Ogenki desu ka?) - Are you well? (സുഖമാണോ?)"},
    {"title": "Lesson 3: Particle を (wo)", "content": "Indicates the direct object of a verb.\nEx: ご飯を食べる (Gohan wo taberu) - Eat rice (ചോറ് കഴിക്കുന്നു)."}
]

def main(page: ft.Page):
    page.title = "Muzan"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    def route_change(e):
        page.views.clear()
        
        # --- HOME PAGE ---
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Muzan"), bgcolor=ft.colors.RED_900, automatically_imply_leading=False),
                        ft.Column([
                            ft.ElevatedButton("Vocabulary Study", on_click=lambda _: page.go("/vocab"), width=300),
                            ft.ElevatedButton("Hiragana Letters", on_click=lambda _: page.go("/hiragana"), width=300),
                            ft.ElevatedButton("Katakana Letters", on_click=lambda _: page.go("/katakana"), width=300),
                            ft.ElevatedButton("N5 Kanji", on_click=lambda _: page.go("/kanji"), width=300),
                            ft.ElevatedButton("Grammar Lessons", on_click=lambda _: page.go("/grammar"), width=300),
                            ft.ElevatedButton("Quiz Section", on_click=lambda _: page.go("/quiz"), width=300),
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        # --- VOCABULARY PAGE ---
        elif page.route == "/vocab":
            current_word = random.choice(list(vocab_data.keys()))
            word_txt = ft.Text(current_word, size=40, weight="bold")
            meaning_txt = ft.Text(f"{vocab_data[current_word][0]}\n{vocab_data[current_word][1]}\n({vocab_data[current_word][2]})", size=20, text_align="center")

            def next_vocab(e):
                w = random.choice(list(vocab_data.keys()))
                word_txt.value = w
                meaning_txt.value = f"{vocab_data[w][0]}\n{vocab_data[w][1]}\n({vocab_data[w][2]})"
                page.update()

            page.views.append(
                ft.View(
                    "/vocab",
                    [
                        ft.AppBar(title=ft.Text("Vocabulary"), bgcolor=ft.colors.RED_900, automatically_imply_leading=False),
                        ft.Column([
                            word_txt,
                            meaning_txt,
                            ft.ElevatedButton("Next Word", on_click=next_vocab),
                            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ]
                )
            )

        # --- HIRAGANA PAGE ---
        elif page.route == "/hiragana":
            char_txt = ft.Text(random.choice(hiragana_chars), size=80, weight="bold")
            def next_hira(e):
                char_txt.value = random.choice(hiragana_chars)
                page.update()

            page.views.append(
                ft.View(
                    "/hiragana",
                    [
                        ft.AppBar(title=ft.Text("Hiragana"), bgcolor=ft.colors.BLUE_900, automatically_imply_leading=False),
                        ft.Column([
                            char_txt,
                            ft.ElevatedButton("Next Letter", on_click=next_hira),
                            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ]
                )
            )

        # --- KATAKANA PAGE ---
        elif page.route == "/katakana":
            char_txt_k = ft.Text(random.choice(katakana_chars), size=80, weight="bold")
            def next_kata(e):
                char_txt_k.value = random.choice(katakana_chars)
                page.update()

            page.views.append(
                ft.View(
                    "/katakana",
                    [
                        ft.AppBar(title=ft.Text("Katakana"), bgcolor=ft.colors.GREEN_900, automatically_imply_leading=False),
                        ft.Column([
                            char_txt_k,
                            ft.ElevatedButton("Next Letter", on_click=next_kata),
                            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ]
                )
            )

        # --- KANJI PAGE ---
        elif page.route == "/kanji":
            k = random.choice(list(kanji_n5.keys()))
            kanji_txt = ft.Text(k, size=80, weight="bold")
            kanji_mean = ft.Text(kanji_n5[k], size=25)
            def next_kanji(e):
                nk = random.choice(list(kanji_n5.keys()))
                kanji_txt.value = nk
                kanji_mean.value = kanji_n5[nk]
                page.update()

            page.views.append(
                ft.View(
                    "/kanji",
                    [
                        ft.AppBar(title=ft.Text("N5 Kanji"), bgcolor=ft.colors.PURPLE_900, automatically_imply_leading=False),
                        ft.Column([
                            kanji_txt, 
                            kanji_mean,
                            ft.ElevatedButton("Next Kanji", on_click=next_kanji),
                            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ]
                )
            )

        # --- GRAMMAR PAGE ---
        elif page.route == "/grammar":
            lessons_ui = [ft.Card(content=ft.Container(padding=15, content=ft.Column([
                ft.Text(l["title"], size=18, weight="bold", color=ft.colors.YELLOW_700),
                ft.Text(l["content"], size=15)
            ]))) for l in grammar_lessons]
            
            page.views.append(
                ft.View(
                    "/grammar",
                    [
                        ft.AppBar(title=ft.Text("Grammar Lessons"), bgcolor=ft.colors.ORANGE_900, automatically_imply_leading=False),
                        ft.Column(lessons_ui, scroll=ft.ScrollMode.AUTO, expand=True),
                        ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        # --- QUIZ PAGE ---
        elif page.route == "/quiz":
            quiz_lang = "Malayalam"
            score = 0
            
            question_txt = ft.Text("", size=24, weight="bold", text_align="center")
            result_txt = ft.Text("", size=18, color=ft.colors.GREEN)
            
            def generate_question():
                correct_word = random.choice(list(vocab_data.keys()))
                options = [correct_word]
                while len(options) < 4:
                    wrong_word = random.choice(list(vocab_data.keys()))
                    if wrong_word not in options:
                        options.append(wrong_word)
                random.shuffle(options)
                return correct_word, options

            current_q, current_opts = generate_question()

            def update_quiz_ui():
                if quiz_lang == "Malayalam":
                    question_txt.value = f"Translate to Japanese:\n{vocab_data[current_q][0]}"
                elif quiz_lang == "English":
                    question_txt.value = f"Translate to Japanese:\n{vocab_data[current_q][1]}"
                else:
                    question_txt.value = f"What is the meaning of:\n{current_q}?"
                
                for i, btn in enumerate(option_buttons):
                    if quiz_lang in ["Malayalam", "English"]:
                        btn.text = current_opts[i]
                        btn.data = current_opts[i] == current_q
                    else:
                        btn.text = vocab_data[current_opts[i]][1]
                        btn.data = current_opts[i] == current_q
                page.update()

            def check_answer(e):
                nonlocal current_q, current_opts, score
                if e.control.data:
                    score += 1
                    result_txt.value = f"Correct! Score: {score}"
                    result_txt.color = ft.colors.GREEN
                else:
                    result_txt.value = f"Wrong! Correct was: {current_q if quiz_lang != 'Japanese' else vocab_data[current_q][1]}"
                    result_txt.color = ft.colors.RED
                
                current_q, current_opts = generate_question()
                update_quiz_ui()

            option_buttons = [ft.ElevatedButton("", on_click=check_answer, width=280) for _ in range(4)]

            def change_lang(e):
                nonlocal quiz_lang
                quiz_lang = e.control.value
                update_quiz_ui()

            lang_dropdown = ft.Dropdown(
                width=150,
                options=[ft.dropdown.Option("Malayalam"), ft.dropdown.Option("English"), ft.dropdown.Option("Japanese")],
                value="Malayalam",
                on_change=change_lang
            )

            page.views.append(
                ft.View(
                    "/quiz",
                    [
                        ft.AppBar(title=ft.Text("Quiz"), bgcolor=ft.colors.TEAL_900, automatically_imply_leading=False),
                        ft.Column([
                            ft.Row([ft.Text("Language:"), lang_dropdown], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Divider(),
                            question_txt,
                            ft.Column(option_buttons, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            result_txt,
                            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"), bgcolor=ft.colors.BLUE_GREY_900)
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
                    ]
                )
            )
            update_quiz_ui()

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
