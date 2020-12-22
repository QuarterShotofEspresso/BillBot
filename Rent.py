from NavigationStrat import NavigationStrat
class Rent(NavigationStrat):

    balance = '$1713.00';

    def fetch_total(self, password):
        
        if (input('Include Rent? [y/n]: ').lower() == 'n'):
            self.balance = '$0.00'

        balance_numeric = float(self.balance[1:])

        return 'Rent:\t\t' + str(self.balance), balance_numeric
