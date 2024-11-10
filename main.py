import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    product_images = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhWHb6LIXteIW7in7OORLdf8yaJ056JJQeig&s'
                ),

                ft.Row(
                    controls=[
                        ft.Container(
                            image_src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhWHb6LIXteIW7in7OORLdf8yaJ056JJQeig&s',
                            width=80,
                            height=80,
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container()

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.YELLOW_600),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)