from Chip.OpCodes.OraCommand import OraCommand


class OpCodeFactory(object):

    def get_command(self, opcode):
        return OraCommand()