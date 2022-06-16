from conDB import Con

c = Con
class Action:
    def gethard_ware3():
        data = c.gethard_ware3()
        return data

    def updatehard_ware3(ID, name):
        data = c.updatehard_ware3(ID, name)
        return data

    def inserthard_ware3(ID, name, hw_name):
        data = c.inserthard_ware3(ID, name, hw_name)
        return data

    def gethard_ware3(ID):
        data = c.gethard_ware3(ID)
        return data

    def addHW(name, hw_name):
        ID = c.addHW(name, hw_name)
        data = c.getHWByID(ID)
        return data

    def updatehard_ware3(ID, status):
        t = c.updatehard_ware3(ID,status)
        if(t == True):
            data = c.gethard_ware3(ID)
        else:
            data = {"error": True}
        return data

    def selecthard_ware3(ID):
        t = c.selecthard_ware3(ID)
        if(t == True):
            data = c.gethard_ware3(ID)
        else:
            data = {"error": True}
        return data
        
    def inserthard_ware3(name, hw_name):
        t = c.inserthard_ware3(name, hw_name)
        if(t == True):
            data = c.gethard_ware3(ID)
        else:
            data = {"error": True}
        return data

       