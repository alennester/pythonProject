class House():
    """Описание дома"""
    def __init__(self, street, number):
        """Свойства дома"""
        self.street=street
        self.number=number
        self.age=0
    def build(self):
        """строит дом"""
        print('дом на улице '+ self.street+' под номером '+ str(self.number)+' построен')
    def age_of_house(self,year):
        '''Возраст дома'''
        self.age+=year
House1=House('Московская', 20)
House2=House('Московская', 21)

House1.age_of_house(5)
print(House1.age)
class ProspectHouse(House):
    '''Дома на проспекте'''
    def __init__(self,prospect,number):
        super().__init__(self,number)
        self.prospect=prospect
PrHouse=ProspectHouse('Lenina',5)
print(PrHouse.prospect)