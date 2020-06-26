class SnapshotArray:
    def __init__(self, n):
        self.snapid = 0
        self.dic = {}

    def set(self, index, val):
        self.dic[(index,self.snapid)] = val

    def snap(self):
        self.snapid += 1
        return self.snapid - 1

    def get(self, index, snap_id):

        while snap_id >=0:
            if self.dic.get((index,snap_id))!= None:
                return self.dic[(index,snap_id)]
            else:
                snap_id -= 1
        return 0

snap = SnapshotArray(3)
snap.set(0,5)
ret = snap.snap()
snap.set(0,6)
ret = snap.get(0,0)
print(ret)

