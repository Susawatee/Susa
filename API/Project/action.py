from conDB import Con

c = Con
class Action:
    def gethard_ware4():
        data = c.gethard_ware4()
        return data

    def getupdatehard_ware4(ID, name):
        data = c.updatehard_ware4(ID, name)
        return data

    def inserthard_ware4(name, hw_name):
        data = c.inserthard_ware4(name, hw_name)
        return data

    def gethard_ware4_ID(ID):
        data = c.gethard_ware4(ID)
        return data

    def addhw(name, hw_name):
        ID = c.addhw(name, hw_name)
        data = c.gethw(ID)
        return data

    def updatehard_ware4(ID, value):
        t = c.updatehard_ware4(ID,value)
        if(t == True):
            data = c.gethard_ware4(ID)
        else:
            data = {"error": True}
        return data

    def selecthard_ware4(ID):
        t = c.selecthard_ware4(ID)
        if(t == True):
            data = c.gethard_ware4(ID)
        else:
            data = {"error": True}
        return data
        
    def inserthard_ware4(name, hw_name):
        t = c.inserthard_ware4(name, hw_name)
        if(t == True):
            data = c.gethard_ware4()
        else:
            data = {"error": True}
        return data

       