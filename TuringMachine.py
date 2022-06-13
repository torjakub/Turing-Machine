# Maszyna Turinga realizujaca zamiane liczby dziesietnej na szesnastkową
from abc import ABC, abstractmethod, abstractproperty

class AbstrackMaszynaTuringa(ABC):

    def __init__(self, alfabet, pustyZnak, stany, stanPoczatkowy, przejscia, tasma):
        self.alfabet = alfabet
        self.pustyZnak = pustyZnak # '#'
        self.stany = stany
        self.stanPoczatkowy = stanPoczatkowy # 'start'
        self.przejscia = przejscia
        self.tasma = tasma
    
    @abstractproperty
    def ListaStanow(self):
        pass

    @abstractproperty
    def Przejscia(self):
        pass

####################################

    @abstractmethod
    def WykonajKrok(self, ZnakZTasmy):
        pass

    @abstractmethod
    def Uruchom(self, Tasma):
        pass

    @abstractmethod
    def CzyStanPoczątkowy(self, stan):
        pass

    @abstractmethod
    def CzyStanKoncowy(self, stan):
        pass

class MaszynaTuringa(AbstrackMaszynaTuringa):
    def __init__(self, alfabet, stany, stanPoczatkowy):
        self.alfabet = alfabet
        self.stany = stany
        self.stanPoczatkowy = stanPoczatkowy
        self.stanTymczasowy = self.stanPoczatkowy
        self.glowica = 0                                # polozenie glowicy/tasmy

    def ListaStanow(self):
        pass

    def Przejscia(self):
        pass

    def CzyStanPoczątkowy(self, stan):
        return stan == self.stanPoczatkowy

    def CzyStanKoncowy(self, stan):
        return stan == 'stop'

    def NumerStanu(self, stan, przejscie):
        
        for i in range(0, len(self.stany[stan])):
            
            if self.stany[stan][i][0] == przejscie:
                return i

    def WykonajKrok(self, ZnakZTasmy):
        stanAktualny = self.stanTymczasowy
 
        stanKolejny = self.stany[stanAktualny][self.NumerStanu(stanAktualny, ZnakZTasmy)][3]

        self.tasma[self.glowica] = self.stany[stanAktualny][self.NumerStanu(stanAktualny, ZnakZTasmy)][1]
        self.glowica += self.stany[stanAktualny][self.NumerStanu(stanAktualny, ZnakZTasmy)][2]
        
        self.stanTymczasowy = stanKolejny

    def Uruchom(self, tasma):

        self.tasma = tasma
        print(self.tasma, self.glowica)
        while True:
            if (self.CzyStanKoncowy(self.stanTymczasowy)):
                break

            self.WykonajKrok(tasma[self.glowica])
            print(self.tasma, self.glowica)

############################
if __name__ == "__main__":
    # alfabet:
    # '@' - koncowy znak tasmy
    # '#' - znak pusty
    # '-1' - przejscie w lewo
    # '1'- przejscie w prawo
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', '#', '@',]

    # Lista stanów z przejsciami
    # stany = ['start', 's1', 's2', 's3', 's3', 's4', 's5', 's6', 's7', 'stop']
    stanPoczatkowy = 'start'
    stany = {'start': [[0, 0, 1, 'start'],
                       [1, 1, 1, 'start'],
                       [2, 2, 1, 'start'],
                       [3, 3, 1, 'start'],
                       [4, 4, 1, 'start'],
                       [5, 5, 1, 'start'],
                       [6, 6, 1, 'start'],
                       [7, 7, 1, 'start'],
                       [8, 8, 1, 'start'],
                       [9, 9, 1, 'start'],
                       ['#', '#', 1, 'start'],
                       ['a', 'a', 1, 'start'],
                       ['b', 'b', 1, 'start'],
                       ['c', 'c', 1, 'start'],
                       ['d', 'd', 1, 'start'],
                       ['e', 'e', 1, 'start'],
                       ['f', 'f', 1, 'start'],
                       ['@', '@', -1, 's1']],

                's1': [[0, 0, -1, 's5'],
                       [1, 0, -1, 's2'],
                       [2, 1, -1, 's2'],
                       [3, 2, -1, 's2'],
                       [4, 3, -1, 's2'],
                       [5, 4, -1, 's2'],
                       [6, 5, -1, 's2'],
                       [7, 6, -1, 's2'],
                       [8, 7, -1, 's2'],
                       [9, 8, -1, 's2']],

               's2': [[0, 0, -1, 's2'],
                      [1, 1, -1, 's2'],
                      [2, 2, -1, 's2'],
                      [3, 3, -1, 's2'],
                      [4, 4, -1, 's2'],
                      [5, 5, -1, 's2'],
                      [6, 6, -1, 's2'],
                      [7, 7, -1, 's2'],
                      [8, 8, -1, 's2'],
                      [9, 9, -1, 's2'],
                      ['@', '@', -1, 's2'],
                      ['#', '#', -1, 's3']],

               's3': [[0, 1, 1, 'start'],
                      [1, 2, 1, 'start'],
                      [2, 3, 1, 'start'],
                      [3, 4, 1, 'start'],
                      [4, 5, 1, 'start'],
                      [5, 6, 1, 'start'],
                      [6, 7, 1, 'start'],
                      [7, 8, 1, 'start'],
                      [8, 9, 1, 'start'],
                      [9, 'a', 1, 'start'],
                      ['a', 'b', 1, 'start'],
                      ['b', 'c', 1, 'start'],
                      ['c', 'd', 1, 'start'],
                      ['d', 'e', 1, 'start'],
                      ['e', 'f', 1, 'start'],
                      ['f', 0, -1, 's4']],

               's4': [['f', 0, -1, 's4'],
                      [0, 1, 1, 'start'],
                      [1, 2, 1, 'start'],
                      [2, 3, 1, 'start'],
                      [3, 4, 1, 'start'],
                      [4, 5, 1, 'start'],
                      [5, 6, 1, 'start'],
                      [6, 7, 1, 'start'],
                      [7, 8, 1, 'start'],
                      [8, 9, 1, 'start'],
                      [9, 'a', 1, 'start'],
                      ['a', 'b', 1, 'start'],
                      ['b', 'c', 1, 'start'],
                      ['c', 'd', 1, 'start'],
                      ['d', 'e', 1, 'start'],
                      ['e', 'f', 1, 'start']],

               's5': [[0, 0, -1, 's5'],
                      [1, 0, 1, 's6'],
                      [2, 1, 1, 's6'],
                      [3, 2, 1, 's6'],
                      [4, 3, 1, 's6'],
                      [5, 4, 1, 's6'],
                      [6, 5, 1, 's6'],
                      [7, 6, 1, 's6'],
                      [8, 7, 1, 's6'],
                      [9, 8, 1, 's6'],
                      ['#','#', 1, 'stop']],

               's6': [[0, 9, 1, 's6'],
                      ['@','@',-1,'s2']],

             'stop': 'stop'}
    #####  liczbaSzesnastkowa, znakPusty, liczbaDziesietna, koniecTasmy
    tasma = [0, 0, 0, 0, 0, '#', 0, 0, 6, 6, 6, '@']

    maszyna = MaszynaTuringa(a, stany, stanPoczatkowy)
    maszyna.Uruchom(tasma)
























































































    
"""
class TuringAbstrakcyjny(ABC):
    def __init__(self, alfabet, stany, przejscia):
        self.alfabet = '[0-9]'+'[a-f]'
        self.liczby = '[0-9]'
        self.znaki = '[a-f]'
        self.stany = stany
        self.przejscia = przejscia
    '''
    @abstractmethod
    def tasma(self, tasma):
        self.tasma = tasma
    '''
    @abstractmethod
    def uruchom(self, tasma):
        self.tasma = list(tasma)
    
    @abstractmethod
    def wykonajKrok(self):
        pass
    
"""


