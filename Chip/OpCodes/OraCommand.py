from Chip import OpCodeDefinitions


class OraCommand(object):

    def __init__(self, chip):
        self.__chip = chip

    def execute(self, input_value):
        """Perform bitwise or on input_value and accumulator"""
        if input_value is None:
            return

        self.__chip.set_accumulator(input_value | self.__chip.get_accumulator())

    @staticmethod
    def matches(opcode):
        return opcode in [OpCodeDefinitions.ora_indirect_x_command, OpCodeDefinitions.ora_zero_page_command]
