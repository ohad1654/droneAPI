class DB:

    def getStatus(self):
        return {
            'position': (1257, 3672),
            'height': 180,
            'angle': 63,
            'streaming': False,
            'battery': 76,
        }

    def setStatus(self, newStatus):
        pass

    def setTarget(self, target):
        pass

    def getTarget(self):
        return (321, 454)

    def getRoomList(self):
        return [{"סלון": (322, 100)}]
