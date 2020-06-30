
class Rent(NavigationStrat):

    __balance = '$1710.00';

    def fetch_total(self, password):
        
        if (input('Include Rent? [y/n]: ').lower() == 'n') {
            self.__balance = '$0.00';
        }

        balance_numeric = float(self.__balance[1:])

        return 'Rent:\t' + str(self.__balance), balance_numeric
