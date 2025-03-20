import flet as ft

def main(page: ft.Page):
    page.title = "hppt://"
    page.bgcolor = "white"

    def on_submit(e):
        pass

    topbar=ft.Container(
        content=ft.Row([
            ft.Text("App Title", size=20, weight=ft.FontWeight.BOLD, color="black")
        ], alignment=ft.MainAxisAlignment.START),
        bgcolor="white",
        padding=10,
        border_radius=ft.border_radius.all(8),
        shadow=ft.BoxShadow(blur_radius=4, color="lightgrey")
    )

    input_field = ft.CupertinoTextField(placeholder_text="Enter text", bgcolor="white", border_color="lightgrey", color="black")
    submit_button = ft.ElevatedButton("Submit", on_click=on_submit, bgcolor="lightgrey", color="black")
    page.add(topbar, input_field, submit_button)

ft.app(main)