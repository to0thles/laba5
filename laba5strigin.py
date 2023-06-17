
class btr:
    def __init__(self, engine):
        self.dvigatel = engine

    def start(self):
        self.dvigatel.start()

    def stop(self):
        self.dvigatel.stop()


class dvigatel:
    def __init__(self, starter):
        self.fuel = starter

    def start(self):
        self.starter.fuel()
        print("Dvigatel started")

    def stop(self):
        print("Dvigatel stopped")

class Fuel:
    def fuel(self):
        print("Fuel")