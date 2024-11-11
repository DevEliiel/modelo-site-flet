import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
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
                            image_src="https://files.tecnoblog.net/wp-content/uploads/2024/09/iphone-16-cores-edited.png",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/41CEGtQGb7L._AC_SX679_.jpg",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/41CF19h72cL._AC_SX679_.jpg",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/511gwck8Z6L._AC_SX679_.jpg",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/51Bf5xVXQgL._AC_SX679_.jpg",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src="https://m.media-amazon.com/images/I/51m8qUn-4tL._AC_SX679_.jpg",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container(
        bgcolor=ft.colors.BLACK87,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='LANÇAMENTOS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Apple Iphone 16',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Smartphones',
                    color=ft.colors.GREY,
                    italic=True
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs' : 12, 'sm' : 6},
                            value='R$ 000',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Row(
                            col={'xs' : 12, 'sm' : 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER,
                                ),
                                 ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER,
                                ),
                                 ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER,
                                ),
                                 ft.Icon(
                                    name=ft.icons.STAR_HALF,
                                    color=ft.colors.AMBER,
                                ),
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.WHITE,
                                )
                            ]
                        )
                    ]
                ),

                ft.Tabs(
                    selected_index=0,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='O iPhone 16 apresenta um design refinado e inovações tecnológicas impressionantes. Disponível em diversas cores, o modelo conta com uma tela Super Retina XDR OLED de bordas ultrafinas, proporcionando uma experiência visual imersiva e nítida, com cores vibrantes e alto brilho. \nCom o chip A18 Bionic, o iPhone 16 oferece desempenho incomparável em velocidade, eficiência energética e capacidade gráfica, garantindo uma performance fluida em jogos, multitarefa e aplicativos exigentes. O sistema iOS 18 traz novas funcionalidades, melhorando a integração do dispositivo com outros aparelhos Apple e otimizando a inteligência artificial para personalizar a experiência do usuário. \nA câmera traseira tripla possui sensores avançados, com melhorias significativas em fotografia em baixa luminosidade, modo retrato e gravação de vídeos em 8K. A câmera frontal de 12 MP também é capaz de capturar selfies com maior clareza e detalhes, além de novos recursos de foco automático.',
                                    color=ft.colors.WHITE,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='O iPhone 16 chega com um design elegante e melhorias em desempenho, câmera e bateria. Ele possui uma tela Super Retina XDR OLED, com cores vibrantes e brilho intenso, disponível em versões de 6,1" e 6,7". O iPhone 16 é equipado com o chip A18 Bionic, que garante uma performance mais rápida e eficiente, ideal para multitarefa e jogos pesados. A câmera traseira tem um sistema triplo, com uma lente principal de 48 MP, uma ultra-angular de 12 MP e uma teleobjetiva de 12 MP. A gravação de vídeos em 8K e fotos em baixa luz melhoraram bastante. A câmera frontal de 12 MP tem foco automático e gravação de vídeos em 4K. A duração da bateria foi aprimorada, com até 20 horas de reprodução de vídeo. O carregamento rápido e sem fio também está disponível. Com estrutura de alumínio (ou aço inoxidável para modelos Pro) e vidro, o iPhone 16 é resistente à água e poeira (certificação IP68). Está disponível em várias cores. Suporta 5G, Wi-Fi 6E e Bluetooth 5.3. O modelo continua usando o conector Lightning, sem mudanças para USB-C. Oferece opções de 128GB, 256GB, 512GB e até 1TB (modelos Pro). O Face ID foi melhorado e garante mais segurança e rapidez no reconhecimento facial. O iPhone 16 começa em 799 dólares para a versão padrão e pode chegar até 1.499 dólares para o modelo Pro Max com maior capacidade de armazenamento.',
                                    color=ft.colors.WHITE,
                                )
                            )
                        )
                    ]
                ),
            ]
        )
    )

    layout = ft.Container(
        width=800,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[ #product_images,
                 product_details],
        ),
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
