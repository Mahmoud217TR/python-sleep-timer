class Timing:
    __totalTime = 0

    def __init__(self, s:int = 0, m:int = 0, h:int = 0) -> None:
        self.setTime(s, m, h)

    def __inRange(self, end, num) -> int:
        if num >= 0 and num <= end:
            return num
        return 0
    
    def getSeconds(self) -> int:
        return (self.__totalTime%3600)%60

    def setSeconds(self,value: int = 0 ) -> None:
        self.__totalTime += -self.getSeconds()+self.__inRange(59, value)

    def getMinutes(self) -> int:
        return (self.__totalTime%3600)//60

    def setMinutes(self,value: int = 0 ) -> None:
        self.__totalTime += (-self.getMinutes()*60)+(self.__inRange(59, value)*60)

    def getHours(self) -> int:
        return self.__totalTime//3600

    def setHours(self,value: int = 0 ) -> None:
        self.__totalTime += (-self.getHours()*3600)+(self.__inRange(24, value)*3600)

    def getTime(self) -> str:
        return '{:02d}:{:02d}:{:02d}'.format(self.getHours(), self.getMinutes(),self.getSeconds())

    def setTime(self, s:int = 0, m:int = 0, h:int = 0) -> None:
        self.setSeconds(s)
        self.setMinutes(m)
        self.setHours(h)
    
    def getTimeInSeconds(self) -> int:
        return self.__totalTime

    def setTimeInSeconds(self, time) -> None:
        self.setHours(time//3600)
        time %= 3600
        self.setMinutes(time//60)
        time %= 60
        self.setSeconds(time)
    
    def changeTotalTime(self, value:int = 1) -> str:
        self.__totalTime += value
        return self.getTime()
