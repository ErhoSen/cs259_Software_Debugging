#
# Implement checkRep on this ZIPCode class
#
# Valid zip codes are 5 digits long, where each digit
# is between 0-9


class ZIPCode:
    # US Only
    
    def __init__(self, zip):
        self._zip = zip
        self.checkRep()

    def zip(self):
        return self._zip
    
    def checkRep(self):
        assert len(self.zip()) == 5
        assert all([ch.isdigit() and (0 <= int(ch) <= 9) for ch in self.zip()])
        # add in your asserts to ensure this is a valid ZIP code

z = ZIPCode("13456")
