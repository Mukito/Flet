import flet as ft

def main(page: ft.Page):
    chat = ft.Column()
    new_menssage = ft.TextField()


    def send_click(e):
        chat.controls.append(ft.Text(new_menssage.value))
        new_menssage.value = ""
        page.update()

    page.add(
        chat,
        ft.Row(
            controls=[new_menssage, ft.ElevatedButton("Enviar", on_click=send_click)]
        )
    )

ft.app(target=main)