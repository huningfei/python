import pickle
class MyPickle:
    def __init__(self,filepath):
        self.filepath = filepath

    def dump(self,sch_obj):
        with open(self.filepath,'ab') as f:
            pickle.dump(sch_obj,f)

    def load(self):
        with open(self.filepath, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except Exception:
                    break

    def get_item(self,num):
        with open(self.filepath, 'rb') as f:
            while num>0:
                try:
                    obj = pickle.load(f)
                except Exception:
                    break
                num -=1
        return obj