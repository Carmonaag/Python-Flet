import flet as ft

def main(page: ft.Page):
    def apply_shadow(e):
        if e.control.shadow:
            e.control.shadow = None
        else:
            e.control.shadow = ft.BoxShadow(
                blur_radius=20,
                color=e.control.bgcolor,
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        e.control.update()

    def notes():
        return ft.ResponsiveRow(
            columns=2,
            controls=[
                ft.Container(
                    col=2,
                    bgcolor= ft.colors.INDIGO,
                    height=200,
                    padding=ft.padding.all(20),
                    border_radius=ft.border_radius.all(10),
                    shadow=None,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value='Titulo da nota',
                                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                max_lines=3,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                value='26/08/2024',
                                style=ft.TextThemeStyle.BODY_MEDIUM,
                            )    
                        ]
                    ),
                    on_hover=apply_shadow,
                )
            ]
        )
    layout = ft.Container(
        expand=True,
        padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                ft.Text(value='NoteX', style=ft.TextThemeStyle.DISPLAY_LARGE),
                ft.Column(
                    expand=True,
                    scroll= ft.ScrollMode.HIDDEN,
                    controls=[notes()]
                )
            ]
        )
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon= ft.icons.ADD,
        shape=ft.CircleBorder(),
        tooltip='Adicionar uma nota',
        bgcolor=ft.colors.INDIGO,
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target= main)