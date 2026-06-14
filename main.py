import flet as ft
import random

# നിങ്ങളുടെ ഡാറ്റാബേസ് ഇവിടെയാണ് (കോഡ് വലുതാകുന്നത് ഒഴിവാക്കാൻ ഇത് ടോപ്പിൽ വെക്കുക)
hiragana_dict = {'あ': 'അ (a)', 'い': 'ഇ (i)', 'う': 'ഉ (u)'} # ... ബാക്കി ഡാറ്റ ഇവിടെ ചേർക്കുക ...
n5_vocab = {'あいさつ': ['അഭിവാദ്യം (Greeting)', 'Aisatsu']} # ... ബാക്കി ഡാറ്റ ഇവിടെ ചേർക്കുക ...

def main(page: ft.Page):
    page.title = "Straw Hat Japanese"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # ലൂഫി തീം നിറങ്ങൾ
    COLOR_LUFFY_RED = "#D32F2F"
    COLOR_STRAW_YELLOW = "#E0A82F"

    # മെയിൻ കണ്ടന്റ്
    main_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(height=50),
            ft.Text("Luffy's Learning Quest", size=30, weight="bold", color=COLOR_LUFFY_RED, text_align="center"),
            ft.ElevatedButton("Hiragana Study", bgcolor=COLOR_STRAW_YELLOW, icon="menu_book"),
            ft.ElevatedButton("Vocabulary Study", bgcolor=COLOR_STRAW_YELLOW, icon="abc"),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # ലൂഫിയുടെ Jolly Roger എപ്പോഴും കാണാൻ (Stack ഉപയോഗിക്കുന്നു)
    page.add(
        ft.Stack(
            controls=[
                main_column,
                ft.Image(
                    src="jolly_roger.png", 
                    width=60, 
                    top=10, 
                    right=10
                )
            ]
        )
    )

ft.app(target=main)
