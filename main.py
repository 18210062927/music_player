try:
    import os
    try:
        import pygame  # pip install pygame
    except ImportError:
        select = input("电脑内缺失pygame模块\n是否修复[y/n]:")
        if select == "y" or select == "Y":
            try:
                os.system("pip install pygame")
                print("修复成功")
            except:
                print("修复失败\n请联系18210062927")
        if select == "n" or select == "N":
            exit()

    def get_listen_list():
        lists = os.listdir("./播放列表")
        if lists:
            return["y",lists]
        else:
            return["n",lists]
            
    folders = os.path.exists("播放列表")
    if not folders:
        os.mkdir("播放列表")
# except:
#     pass
    have, lists = get_listen_list()
    if have == "y":
        print("请选择播放列表内的音乐")
        for num in range(0,len(lists)):
            print(str(num+1)+"."+lists[num])
        select_filename = input()
        filename = lists[int(select_filename)-1]
        filenames = "./播放列表/"+filename
    else:
        filenames = input("请输入音乐文件路径\n")

    def playMusic(filename, replays, loops=0, start=0.0, value=0.5):
        """
        :param filename: 文件名
        :param loops: 循环次数
        :param start: 从多少秒开始播放
        :param value: 设置播放的音量，音量value的范围为0.0到1.0
        :return:
        """
        def player(filename, replays, loops=0, start=0.0, value=0.5):
            flag = False  # 是否播放过
            pygame.mixer.init()  # 音乐模块初始化
            while 1:
                if flag == 0:
                    pygame.mixer.music.load(filename)
                    # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
                    pygame.mixer.music.play(loops=loops, start=start)
                    pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
                if pygame.mixer.music.get_busy() == True:
                    flag = True
                else:
                    if flag:
                        pygame.mixer.music.stop()  # 停止播放
                        break
        if replays == "d":
            while True:
                player(filename=filenames, replays="y")
        else:
            player(filename=filenames, replays="n")
            replay()


    def replay():
        replay_cho = input("是否重播?[Y/N/D]")
        if replay_cho == "Y" or replay_cho == "y":
            playMusic(filename=filenames, replays="n")
        elif replay_cho == "N" or replay_cho =="n":
            print("感谢使用")
            exit()
        elif replay_cho == "D" or replay_cho == "D":
            playMusic(filename=filenames, replays="d")



    playMusic(filename=filenames, replays="n")
except KeyboardInterrupt:
    print("已终止操作\n")