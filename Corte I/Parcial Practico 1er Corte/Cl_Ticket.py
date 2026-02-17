class ticket:
    def __init__(self, numTicket, nameClient, cedulaClient, costTicket, cantTicket, nameMovie, buyDay):
        self.numTicket = numTicket
        self.nameClient = nameClient
        self.cedulaClient = cedulaClient
        self.costTicket = int(costTicket)
        self.cantTicket = int(cantTicket)
        self.nameMovie = nameMovie
        self.buyDay = buyDay
        
    def payToTicket(self):
        if self.buyDay == "monday":
            return (self.costTicket - (self.costTicket * 0.5))
        elif self.buyDay == "thursday":
            return (self.costTicket - (self.costTicket * 0.3)) #en los requerimientos estaba 30$ pero creo que es un error lo cambié a 30%
        else:
            return self.costTicket

    def ShowTicket(self):
        print(f"Number of Ticket: {self.numTicket}")
        print(f"Client Name: {self.nameClient}")
        print(f"Client ID: {self.cedulaClient}")
        print(f"Cost of Ticket: {self.payToTicket()}")
        print(f"Number of Tickets: {self.cantTicket}")
        print(f"Movie Name: {self.nameMovie}")
