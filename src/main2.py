import flet as ft

def main(page: ft.Page):
    page.add(MeuBotao(text="OK"), MeuBotao("Cancel"))


class MeuBotao(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text


ft.app(main)