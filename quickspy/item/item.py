class Url():
    def __init__(self):
        self.url = None
        self.cata = None #view at struct
        self.comefrom = None #Url class
        self.belongto = None #创建从属关系
        self.res = None
        self.history = None
        self.settings = None


class Res():
    def __init__(self):
        self.img_res = None
        self.text_res = None
        self.video_res = None
        self.other_res = None
        self.oother_res = None
        self.ooother_res = None