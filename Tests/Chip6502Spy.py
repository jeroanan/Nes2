from Chip.Chip6502 import Chip6502


class Chip6502Spy(Chip6502):

    def brk_command(self):
        self.__brk_command_executed = True

    def get_brk_command_executed(self):
        return self.__brk_command_executed

    def ora_command(self):
        self.__ora_command_executed = True

    def get_ora_command_executed(self):
        return self.__ora_command_executed

    def asl_command(self):
        self.__asl_command_executed = True

    def get_asl_command_executed(self):
        return self.__asl_command_executed

    def php_command(self):
        self.__php_command_executed = True

    def get_php_command_executed(self):
        return self.__php_command_executed

    def bpl_command(self):
        self.__bpl_command_executed = True

    def get_bpl_command_executed(self):
        return self.__bpl_command_executed

    def clc_command(self):
        self.__clc_command_executed = True

    def get_clc_command_executed(self):
        return self.__clc_command_executed

    def jsr_command(self):
        self.__jsr_command_executed = True

    def get_jsr_command_executed(self):
        return self.__jsr_command_executed

    def and_command(self):
        self.__and_command_executed = True

    def get_and_command_executed(self):
        return self.__and_command_executed

    def bit_command(self):
        self.__bit_command_executed = True

    def get_bit_command_executed(self):
        return self.__bit_command_executed

    def rol_command(self):
        self.__rol_command_executed = True

    def get_rol_command_executed(self):
        return self.__rol_command_executed

    def plp_command(self):
        self.__plp_command_executed = True

    def get_plp_command_executed(self):
        return self.__plp_command_executed

    def bmi_command(self):
        self.__bmi_command_executed = True

    def get_bmi_command_executed(self):
        return self.__bmi_command_executed

    def sec_command(self):
        self.__sec_command_executed = True

    def get_sec_command_executed(self):
        return self.__sec_command_executed

    def rti_command(self):
        self.__rti_command_executed = True

    def get_rti_command_executed(self):
        return self.__rti_command_executed

    def __init__(self):
        self.__asl_command_executed = False
        self.__ora_command_executed = False
        self.__brk_command_executed = False
        self.__php_command_executed = False
        self.__bpl_command_executed = False
        self.__clc_command_executed = False
        self.__jsr_command_executed = False
        self.__and_command_executed = False
        self.__bit_command_executed = False
        self.__rol_command_executed = False
        self.__plp_command_executed = False
        self.__bmi_command_executed = False
        self.__sec_command_executed = False
        self.__rti_command_executed = False