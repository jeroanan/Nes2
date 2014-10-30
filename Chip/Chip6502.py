from Chip import OpCodes


class Chip6502(object):

    def __init__(self):
        self.__accumulator = 0x0
        self.__carry_flag = 0x0
        self.__overflow_flag = 0x0
        self.__zero_flag = 0x0
        self.__negative_flag = 0x0
        self.__x_register = 0x0
        self.__y_register = 0x0

    def set_accumulator(self, value):
        self.__accumulator = value

    def get_accumulator(self):
        return self.__accumulator

    def set_carry_flag(self):
        self.__carry_flag = 0x01

    def clear_carry_flag(self):
        self.__carry_flag = 0x0

    def get_carry_flag(self):
        return self.__carry_flag

    def get_overflow_flag(self):
        return self.__overflow_flag

    def set_overflow_flag(self):
        self.__overflow_flag = 0x01

    def get_zero_flag(self):
        return self.__zero_flag

    def __set_zero_flag(self, result):
        self.__zero_flag = 0x00
        if result == 0x0:
            self.__zero_flag = 0x01

    def get_negative_flag(self):
        return self.__negative_flag

    def __set_negative_flag(self, value):
        self.__negative_flag = 0x0
        if value >= 128:
            self.__negative_flag = 0x1

    def get_x_register(self):
        return self.__x_register

    def get_y_register(self):
        return self.__y_register

    def set_y_register(self, value):
        self.__y_register = value

    def execute(self, command, operand=None):
        if command == OpCodes.brk_command:
            self.brk_command()
        elif self.__is_ora_command(command):
            self.ora_command(operand)
        elif self.__is_asl_command(command):
            self.asl_command()
        elif command == OpCodes.php_implied_command:
            self.php_command()
        elif command == OpCodes.bpl_relative_command:
            self.bpl_command()
        elif command == OpCodes.clc_implied_command:
            self.clc_command()
        elif command == OpCodes.jsr_absolute_command:
            self.jsr_command()
        elif self.__is_and_command(command):
            self.and_command(operand)
        elif self.__is_bit_command(command):
            self.bit_command()
        elif self.__is_rol_command(command):
            self.rol_command()
        elif command == OpCodes.plp_implied_command:
            self.plp_command()
        elif command == OpCodes.bmi_relative_command:
            self.bmi_command()
        elif command == OpCodes.sec_implied_command:
            self.sec_command()
        elif command == OpCodes.rti_implied_command:
            self.rti_command()
        elif self.__is_eor_command(command):
            self.eor_command(operand)
        elif self.__is_lsr_command(command):
            self.lsr_command()
        elif command == OpCodes.pha_implied_command:
            self.pha_command()
        elif command == OpCodes.bvc_relative_command:
            self.bvc_command()
        elif command == OpCodes.cli_implied_command:
            self.cli_command()
        elif command == OpCodes.rts_implied_command:
            self.rts_command()
        elif self.__is_adc_command(command):
            self.adc_command(operand)
        elif self.__is_ror_command(command):
            self.ror_command()
        elif command == OpCodes.pla_implied_command:
            self.pla_command()
        elif command == OpCodes.jmp_indirect_command:
            self.jmp_command()
        elif command == OpCodes.bvs_relative_command:
            self.bvs_command()
        elif command == OpCodes.sei_implied_command:
            self.sei_command()
        elif self.__is_sta_command(command):
            self.sta_command()
        elif self.__is_sty_command(command):
            self.sty_command()
        elif self.__is_stx_command(command):
            self.stx_command()
        elif command == OpCodes.dey_implied_command:
            self.dey_command()
        elif command == OpCodes.txa_implied_command:
            self.txa_command()
        elif command == OpCodes.bcc_relative_command:
            self.bcc_command()
        elif command == OpCodes.tya_implied_command:
            self.tya_command()
        elif command == OpCodes.txs_implied_command:
            self.txs_command()
        elif self.__is_ldy_command(command):
            self.ldy_command(operand)
        elif self.__is_lda_command(command):
            self.lda_command(operand)
        elif self.__is_ldx_command(command):
            self.ldx_command(operand)
        elif command == OpCodes.tay_implied_command:
            self.tay_command()
        elif command == OpCodes.tax_implied_command:
            self.tax_command()
        elif command == OpCodes.bcs_relative_command:
            self.bcs_command()
        elif command == OpCodes.clv_implied_command:
            self.clv_command()
        elif command == OpCodes.tsx_implied_command:
            self.tsx_command()
        elif self.__is_cpy_command(command):
            self.cpy_command(operand)
        elif self.__is_cmp_command(command):
            self.cmp_command()
        elif self.__is_dec_command(command):
            self.dec_command()
        elif command == OpCodes.iny_implied_command:
            self.iny_command()
        elif command == OpCodes.dex_implied_command:
            self.dex_command()
        elif command == OpCodes.bne_relative_command:
            self.bne_command()
        elif command == OpCodes.cld_implied_command:
            self.cld_command()
        elif self.__is_cpx_command(command):
            self.cpx_command()
        elif self.__is_sbc_command(command):
            self.sbc_command()
        elif self.__is_inc_command(command):
            self.inc_command()
        elif command == OpCodes.inx_implied_command:
            self.inx_command()
        elif command == OpCodes.nop_implied_command:
            self.nop_command()
        elif command == OpCodes.beq_relative_command:
            self.beq_command()
        elif command == OpCodes.sed_implied_command:
            self.sed_command()

    def brk_command(self):
        pass

    def __is_ora_command(self, command):
        return command in [OpCodes.ora_indirect_x_command, OpCodes.ora_zero_page_command, OpCodes.ora_immediate_command,
                           OpCodes.ora_absolute_command, OpCodes.ora_indirect_y_command,
                           OpCodes.ora_zero_page_x_command,
                           OpCodes.ora_absolute_y_command, OpCodes.ora_absolute_x_command]

    def ora_command(self, input_value):
        """Perform bitwise or on input_value and accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value | self.get_accumulator())

    def __is_asl_command(self, command):
        return command in [OpCodes.asl_zero_page_command, OpCodes.asl_accumulator_command, OpCodes.asl_absolute_command,
                           OpCodes.asl_zero_page_x_command, OpCodes.asl_absolute_x_command]

    def asl_command(self):
        pass

    def php_command(self):
        pass

    def bpl_command(self):
        pass

    def clc_command(self):
        pass

    def jsr_command(self):
        pass

    def __is_and_command(self, command):
        return command in [OpCodes.and_indirect_x_command, OpCodes.and_zero_page_command, OpCodes.and_immediate_command,
                           OpCodes.and_absolute_command, OpCodes.and_indirect_y_command,
                           OpCodes.and_zero_page_x_command,
                           OpCodes.and_absolute_y_command, OpCodes.and_absolute_x_command]

    def and_command(self, input_value):
        """Perform bitwise and on input_value and accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value & self.get_accumulator())

    def __is_bit_command(self, command):
        return command in [OpCodes.bit_zero_page_command, OpCodes.bit_absolute_command]

    def bit_command(self):
        pass

    def __is_rol_command(self, command):
        return command in [OpCodes.rol_zero_page_command, OpCodes.rol_accumulator_command, OpCodes.rol_absolute_command,
                           OpCodes.rol_zero_page_x_command, OpCodes.rol_absolute_x_command]

    def rol_command(self):
        pass

    def plp_command(self):
        pass

    def bmi_command(self):
        pass

    def sec_command(self):
        pass

    def rti_command(self):
        pass

    def __is_eor_command(self, command):
        return command in [OpCodes.eor_indirect_x_command, OpCodes.eor_zero_page_command, OpCodes.eor_immediate_command,
                           OpCodes.eor_absolute_command, OpCodes.eor_indirect_y_command,
                           OpCodes.eor_zero_page_x_command,
                           OpCodes.eor_absolute_y_command, OpCodes.eor_absolute_x_command]

    def eor_command(self, input_value):
        """Perform bitwise xor on input_value and accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value ^ self.get_accumulator())

    def __is_lsr_command(self, command):
        return command in [OpCodes.lsr_zero_page_command, OpCodes.lsr_accumulator_command, OpCodes.lsr_absolute_command,
                           OpCodes.lsr_zero_page_x_command, OpCodes.lsr_absolute_x_command]

    def lsr_command(self):
        pass

    def pha_command(self):
        pass

    def bvc_command(self):
        pass

    def cli_command(self):
        pass

    def rts_command(self):
        pass

    def __is_adc_command(self, command):
        return command in [OpCodes.adc_indirect_x_command, OpCodes.adc_zero_page_command, OpCodes.adc_immediate_command,
                           OpCodes.adc_absolute_command, OpCodes.adc_indirect_y_command,
                           OpCodes.adc_zero_page_x_command,
                           OpCodes.adc_absolute_y_command, OpCodes.adc_absolute_x_command]

    def adc_command(self, input_value):
        if input_value is None:
            return

        self.set_accumulator(input_value + self.get_accumulator())

        if self.get_accumulator() > 0xFF:
            self.set_accumulator(0xFF)
            self.set_carry_flag()
        else:
            self.clear_carry_flag()

        if self.get_accumulator() > 127:
            self.set_overflow_flag()

        self.__set_zero_flag(self.get_accumulator())

    def __is_ror_command(self, command):
        return command in [OpCodes.ror_zero_page_command, OpCodes.ror_accumulator_command, OpCodes.ror_absolute_command,
                           OpCodes.ror_zero_page_x_command, OpCodes.ror_absolute_x_command]

    def ror_command(self):
        pass

    def pla_command(self):
        pass

    def jmp_command(self):
        pass

    def bvs_command(self):
        pass

    def sei_command(self):
        pass

    def __is_sta_command(self, command):
        return command in [OpCodes.sta_indirect_x_command, OpCodes.sta_zero_page_command, OpCodes.sta_absolute_command,
                           OpCodes.sta_indirect_y_command, OpCodes.sta_zero_page_x_command,
                           OpCodes.sta_absolute_y_command, OpCodes.sta_absolute_x_command]

    def sta_command(self):
        pass

    def __is_sty_command(self, command):
        return command in [OpCodes.sty_zero_page_command, OpCodes.sty_absolute_command, OpCodes.sty_zero_page_x_command]

    def sty_command(self):
        pass

    def __is_stx_command(self, command):
        return command in [OpCodes.stx_zero_page_command, OpCodes.stx_absolute_command, OpCodes.stx_zero_page_y_command]

    def stx_command(self):
        pass

    def dey_command(self):
        pass

    def txa_command(self):
        pass

    def bcc_command(self):
        pass

    def tya_command(self):
        pass

    def txs_command(self):
        pass

    def __is_ldy_command(self, command):
        return command in [OpCodes.ldy_immediate_command, OpCodes.ldy_zero_page_command, OpCodes.ldy_absolute_command,
                           OpCodes.ldy_zero_page_x_command, OpCodes.ldy_absolute_x_command]

    def ldy_command(self, input_value):
        """load input_value into the y register"""
        if input_value is None:
            return

        self.__y_register = input_value

        self.__set_zero_flag(self.get_y_register())
        self.__set_negative_flag(self.get_y_register())

    def __is_lda_command(self, command):
        return command in [OpCodes.lda_indirect_x_command, OpCodes.lda_zero_page_command, OpCodes.lda_immediate_command,
                           OpCodes.lda_absolute_command, OpCodes.lda_indirect_y_command,
                           OpCodes.lda_zero_page_x_command, OpCodes.lda_absolute_y_command,
                           OpCodes.lda_absolute_x_command]

    def lda_command(self, input_value):
        """load input_value into the accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value)

        self.__set_zero_flag(self.get_accumulator())
        self.__set_negative_flag(self.get_accumulator())

    def __is_ldx_command(self, command):
        return command in [OpCodes.ldx_immediate_command, OpCodes.ldx_zero_page_command, OpCodes.ldx_absolute_command,
                           OpCodes.ldx_zero_page_y_command, OpCodes.ldx_absolute_y_command]

    def ldx_command(self, input_value):
        """load input_value into the x register"""
        if input_value is None:
            return

        self.__x_register = input_value
        self.__set_zero_flag(self.__x_register)
        self.__set_negative_flag(self.__x_register)

    def tay_command(self):
        pass

    def tax_command(self):
        pass

    def bcs_command(self):
        pass

    def clv_command(self):
        pass

    def tsx_command(self):
        pass

    def __is_cpy_command(self, command):
        return command in [OpCodes.cpy_immediate_command, OpCodes.cpy_zero_page_command, OpCodes.cpy_absolute_command]

    def cpy_command(self, input_value):
        if input_value is None:
            return

        self.__set_zero_flag(not input_value == self.get_y_register())
        if input_value <= self.get_y_register():
            self.__carry_flag = 0x1

    def __is_cmp_command(self, command):
        return command in [OpCodes.cmp_indirect_x_command, OpCodes.cmp_zero_page_command, OpCodes.cmp_immediate_command,
                           OpCodes.cmp_absolute_command, OpCodes.cmp_indirect_y_command,
                           OpCodes.cmp_zero_page_x_command, OpCodes.cmp_absolute_y_command,
                           OpCodes.cmp_absolute_x_command]

    def cmp_command(self):
        pass

    def __is_dec_command(self, command):
        return command in [OpCodes.dec_zero_page_command, OpCodes.dec_absolute_command, OpCodes.dec_zero_page_x_command,
                           OpCodes.dec_absolute_x_command]

    def dec_command(self):
        pass

    def iny_command(self):
        pass

    def dex_command(self):
        pass

    def bne_command(self):
        pass

    def cld_command(self):
        pass

    def __is_cpx_command(self, command):
        return command in [OpCodes.cpx_immediate_command, OpCodes.cpx_zero_page_command, OpCodes.cpx_absolute_command]

    def cpx_command(self):
        pass

    def __is_sbc_command(self, command):
        return command in [OpCodes.sbc_indirect_x_command, OpCodes.sbc_zero_page_command, OpCodes.sbc_immediate_command,
                           OpCodes.sbc_absolute_command, OpCodes.sbc_indirect_y_command,
                           OpCodes.sbc_zero_page_x_command, OpCodes.sbc_absolute_y_command,
                           OpCodes.sbc_absolute_x_command]

    def sbc_command(self):
        pass

    def __is_inc_command(self, command):
        return command in [OpCodes.inc_zero_page_command, OpCodes.inc_absolute_command, OpCodes.inc_zero_page_x_command,
                           OpCodes.inc_absolute_x_command]

    def inc_command(self):
        pass

    def inx_command(self):
        pass

    def nop_command(self):
        pass

    def beq_command(self):
        pass

    def sed_command(self):
        pass





