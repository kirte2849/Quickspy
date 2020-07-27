import time


class Url:
    def __init__(self, url, comefrom, cata):
        self.id = None
        self.title = None
        self.url = url
        self.meta = None
        self.settings = None
        self.history = []  # [time, time, time]
        self.domain = None
        self.cata = cata  # main_page
        self.comefrom = comefrom
        self.belongto = None

class Item:
    def __init__(self, url, comefrom, cata, res):
        self.id = None
        self.title = None
        self.url = url
        self.domain = None
        self.meta = None
        self.settings = None
        self.res = res
        self.history = [] #[time, time, time]
        self.cata = cata #main_page
        self.src = None
        self.comefrom = comefrom
        self.belongto = None

        self.history.append(time.time())


class Res:
    def __init__(self):
        self.img_res = None #[]
        self.text_res = None
        self.video_res = None
        self.other_res = None
        self.oother_res = None
        self.ooother_res = None

def obj_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict

def dict_to_obj(dict):
    myClassReBuild = json.loads(myClassJson)
    print(myClassReBuild)
    myClass2 = MyClass()
    myClass2.__dict__ = myClassReBuild