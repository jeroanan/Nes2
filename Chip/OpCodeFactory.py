from Chip.OpCodes.OraCommand import OraCommand


class OpCodeFactory(object):

    def __init__(self, chip):
        self.__chip = chip

    def get_command(self, opcode):
        return OraCommand(self.__chip)