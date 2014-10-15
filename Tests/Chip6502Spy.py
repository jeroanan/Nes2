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

    def eor_command(self):
        self.__eor_command_executed = True

    def get_eor_command_executed(self):
        return self.__eor_command_executed

    def get_lsr_command_executed(self):
        return self.__lsr_command_executed

    def lsr_command(self):
        self.__lsr_command_executed = True

    def get_pha_command_executed(self):
        return self.__pha_command_executed

    def pha_command(self):
        self.__pha_command_executed = True

    def get_bvc_command_executed(self):
        return self.__bvc_command_executed

    def bvc_command(self):
        self.__bvc_command_executed = True

    def get_cli_command_executed(self):
        return self.__cli_command_executed

    def cli_command(self):
        self.__cli_command_executed = True

    def get_rts_command_executed(self):
        return self.__rts_command_executed

    def rts_command(self):
        self.__rts_command_executed = True

    def get_adc_command_executed(self):
        return self.__adc_command_executed

    def adc_command(self):
        self.__adc_command_executed = True

    def get_ror_command_executed(self):
        return self.__ror_command_executed

    def ror_command(self):
        self.__ror_command_executed = True

    def get_pla_command_executed(self):
        return self.__pla_command_executed

    def pla_command(self):
        self.__pla_command_executed = True

    def jmp_command(self):
        self.__jmp_command_executed = True

    def get_jmp_command_executed(self):
        return self.__jmp_command_executed

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
        self.__eor_command_executed = False
        self.__lsr_command_executed = False
        self.__pha_command_executed = False
        self.__bvc_command_executed = False
        self.__cli_command_executed = False
        self.__rts_command_executed = False
        self.__adc_command_executed = False
        self.__ror_command_executed = False
        self.__pla_command_executed = False
        self.__jmp_command_executed = False