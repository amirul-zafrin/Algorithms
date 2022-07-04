class VersionManager:
    def __init__(self, version = "0.0.1"):
        self.version = self.validation(version)
        self.__version_control = []

    def validation(self,version):
        if not version:
            version = "0.0.1"
        try:
            vrs = [*map(int, version.split(".")[:3])] + [0,0,0]
            del vrs[3:]
            return (vrs if any(vrs) else [0,0,1])
        except:
            raise Exception("Error occured while parsing version!")

    def __update(self, idx):
        self.__version_control.append([*self.version])
        self.version[idx] += 1
        self.version[idx+1:] = [0] * (len(self.version)-1-idx)
        return self

    def major(self):
        return self.__update(0)

    def minor(self):
        return self.__update(1)

    def patch(self):
        return self.__update(2)

    def release(self):
        return '.'.join(map(str, self.version))

    def rollback(self):
        if not self.__version_control:
            raise Exception("Cannot rollback!")
        else:
            self.version = self.__version_control.pop()
            return self

print(VersionManager("1.2.3.4").major().minor().release())