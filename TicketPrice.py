class Movie:
    def __init__(self,movie_name:str,ticket_price:int,total_seat:int):
        self.movie_name=movie_name
        self.ticket_price=ticket_price
        self.total_seat=total_seat
        self.availableseat=self.total_seat
    def bookshow(self,bookseat:int):
        if self.availableseat<=0:
            print("hall is full u can not book ticket")
        else:
            price=self.ticket_price*bookseat
            print(f"price is {price} and seat {bookseat} is booked")
    def showStatus(self):

        print(f'Movie name is {self.movie_name} Ticket price is {self.ticket_price} and total seat is {self.total_seat}')

    
m=Movie("jai ho",200,100)
m.showStatus()
m.bookshow(110)
m.showStatus()