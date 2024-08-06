class Hotel :
    sortParam ='name'
    def __init__(self) ->None:
        self.name=''
        self.roomAvl =0
        self.location=''
        self.rating=int
        self.pricePr=0
        
    def __lt__(self,other):
        getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)
        