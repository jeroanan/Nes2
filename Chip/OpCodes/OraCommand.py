class OraCommand(object):

    def __init__(self, chip):
        self.__chip = chip

    def execute(self, input_value):
        """Perform bitwise or on input_value and accumulator"""
        if input_value is None:
            return

        self.__chip.set_accumulator(input_value | self.__chip.get_accumulator())