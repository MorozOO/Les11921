class contactTelegram():
    userName = ""
    phone = ""
class contactViber():
    name = ""
    phone = ""
class contactList(contactTelegram,contactViber):
    name = ""
    phone = ""
    category =""
    def __init__(self,n,p,c):
        self.name = n
        self.phone = p
        self.category = c
        self.userName = contactTelegram.userName

    def __init__(self, c):
        self.name = contactViber.name
        self.phone = contactViber.phone
        self.category = c
        self.userName = contactTelegram.userName
