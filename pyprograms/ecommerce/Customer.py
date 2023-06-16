class Customer():
    """
    properties
    """
    #id, name, email, mobile, address, location

    id:int=0
    #code=0
    name:str
    email:str
    mobile:int
    address: str
    location: str
    """
    constructor in python
    """
    def __init__(self,id, name, email, mobile, address, location):
        self.id = id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.location =location


    def __str__(self):
        return f"\n Id:{self.id} \n Name: {self.name} "

