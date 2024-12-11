class India :
    def capital(self):
        print("New Delhi")

class USA :
    def capital(self):
        print("Washigston DC ")


object_India=India() 
object_USA=USA()
 for country in (object_India,object_USA):
    country.capital()

