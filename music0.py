while True:
    path1 = ["D:\\music\\music0\\稻香.mp3",
             "D:\\music\\music0\\董小姐.mp3",
             "D:\\music\\music0\\反方向的钟.mp3",
             "D:\\music\\music0\\花海.mp3",
             "D:\\music\\music0\\蒲公英的约定.mp3",
             "D:\\music\\music0\\七里香.mp3",
             "D:\\music\\music0\\水星记.mp3",
             "D:\\music\\music0\\走马.mp3"]

    path2 = ['[稻香]',
             '[董小姐]',
             '[反方向的钟]',
             '[花海]',
             '[蒲公英的约定]',
             '[七里香]',
             '[水星记]',
             '[走马]']

    import random
    i = random.randint(0, 7)
    print(path2[i], '\n')

    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(path1[i])
    pygame.mixer.music.set_volume(0.5)  # 声音大小[0<j<1]  J = float(input("调节音量：J="))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
