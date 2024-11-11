import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE60

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                elem.width = 90
                elem.height = 90
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        main_image.update()
        options.update()

    product_images = ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                main_image := ft.Image(
                    src="https://files.tecnoblog.net/wp-content/uploads/2024/09/iphone-16-cores-edited.png",
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/41CEGtQGb7L._AC_SX679_.jpg",
                            width=150,
                            height=150,
                            opacity=1,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/41CF19h72cL._AC_SX679_.jpg",
                            width=150,
                            height=150,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/511gwck8Z6L._AC_SX679_.jpg",
                            width=150,
                            height=150,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/51Bf5xVXQgL._AC_SX679_.jpg",
                            width=150,
                            height=150,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/51m8qUn-4tL._AC_SX679_.jpg",
                            width=150,
                            height=150,
                            opacity=0.5,
                            on_click=change_main_image,
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container()

    layout = ft.Container(
        width=950,
        margin=ft.margin.all(30),
        content=ft.ResponsiveRow(
            columns=0,
            spacing=0,
            run_spacing=0,
            controls=[product_images, product_details],
        ),
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
