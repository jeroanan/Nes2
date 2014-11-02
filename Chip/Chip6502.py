from Chip import OpCodeDefinitions
from Chip.OpCodeFactory import OpCodeFactory


class Chip6502(object):

    def __init__(self,):
        self.__accumulator = 0x0
        self.__carry_flag = 0x0
        self.__overflow_flag = 0x0
        self.__zero_flag = 0x0
        self.__negative_flag = 0x0
        self.__x_register = 0x0
        self.__y_register = 0x0
        self.__op_code_factory = OpCodeFactory(self)

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

    def clear_overflow_flag(self):
        self.__overflow_flag = 0x0

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

    def set_x_register(self, value):
        self.__x_register = value

    def get_y_register(self):
        return self.__y_register

    def set_y_register(self, value):
        self.__y_register = value

    def execute(self, opcode, operand=None):

        command = self.__op_code_factory.get_command(opcode)

        if opcode == OpCodeDefinitions.brk_command:
            self.brk_command()
        elif self.__is_ora_command(opcode):
            command.execute(operand)
            self.ora_command(operand)
        elif self.__is_asl_command(opcode):
            self.asl_command()
        elif opcode == OpCodeDefinitions.php_implied_command:
            self.php_command()
        elif opcode == OpCodeDefinitions.bpl_relative_command:
            self.bpl_command()
        elif opcode == OpCodeDefinitions.clc_implied_command:
            self.clc_command()
        elif opcode == OpCodeDefinitions.jsr_absolute_command:
            self.jsr_command()
        elif self.__is_and_command(opcode):
            self.and_command(operand)
        elif self.__is_bit_command(opcode):
            self.bit_command()
        elif self.__is_rol_command(opcode):
            self.rol_command()
        elif opcode == OpCodeDefinitions.plp_implied_command:
            self.plp_command()
        elif opcode == OpCodeDefinitions.bmi_relative_command:
            self.bmi_command()
        elif opcode == OpCodeDefinitions.sec_implied_command:
            self.sec_command()
        elif opcode == OpCodeDefinitions.rti_implied_command:
            self.rti_command()
        elif self.__is_eor_command(opcode):
            self.eor_command(operand)
        elif self.__is_lsr_command(opcode):
            self.lsr_command()
        elif opcode == OpCodeDefinitions.pha_implied_command:
            self.pha_command()
        elif opcode == OpCodeDefinitions.bvc_relative_command:
            self.bvc_command()
        elif opcode == OpCodeDefinitions.cli_implied_command:
            self.cli_command()
        elif opcode == OpCodeDefinitions.rts_implied_command:
            self.rts_command()
        elif self.__is_adc_command(opcode):
            self.adc_command(operand)
        elif self.__is_ror_command(opcode):
            self.ror_command()
        elif opcode == OpCodeDefinitions.pla_implied_command:
            self.pla_command()
        elif opcode == OpCodeDefinitions.jmp_indirect_command:
            self.jmp_command()
        elif opcode == OpCodeDefinitions.bvs_relative_command:
            self.bvs_command()
        elif opcode == OpCodeDefinitions.sei_implied_command:
            self.sei_command()
        elif self.__is_sta_command(opcode):
            self.sta_command()
        elif self.__is_sty_command(opcode):
            self.sty_command()
        elif self.__is_stx_command(opcode):
            self.stx_command()
        elif opcode == OpCodeDefinitions.dey_implied_command:
            self.dey_command()
        elif opcode == OpCodeDefinitions.txa_implied_command:
            self.txa_command()
        elif opcode == OpCodeDefinitions.bcc_relative_command:
            self.bcc_command()
        elif opcode == OpCodeDefinitions.tya_implied_command:
            self.tya_command()
        elif opcode == OpCodeDefinitions.txs_implied_command:
            self.txs_command()
        elif self.__is_ldy_command(opcode):
            self.ldy_command(operand)
        elif self.__is_lda_command(opcode):
            self.lda_command(operand)
        elif self.__is_ldx_command(opcode):
            self.ldx_command(operand)
        elif opcode == OpCodeDefinitions.tay_implied_command:
            self.tay_command()
        elif opcode == OpCodeDefinitions.tax_implied_command:
            self.tax_command()
        elif opcode == OpCodeDefinitions.bcs_relative_command:
            self.bcs_command()
        elif opcode == OpCodeDefinitions.clv_implied_command:
            self.clv_command()
        elif opcode == OpCodeDefinitions.tsx_implied_command:
            self.tsx_command()
        elif self.__is_cpy_command(opcode):
            self.cpy_command(operand)
        elif self.__is_cmp_command(opcode):
            self.cmp_command(operand)
        elif self.__is_dec_command(opcode):
            self.dec_command()
        elif opcode == OpCodeDefinitions.iny_implied_command:
            self.iny_command()
        elif opcode == OpCodeDefinitions.dex_implied_command:
            self.dex_command()
        elif opcode == OpCodeDefinitions.bne_relative_command:
            self.bne_command()
        elif opcode == OpCodeDefinitions.cld_implied_command:
            self.cld_command()
        elif self.__is_cpx_command(opcode):
            self.cpx_command(operand)
        elif self.__is_sbc_command(opcode):
            self.sbc_command(operand)
        elif self.__is_inc_command(opcode):
            self.inc_command()
        elif opcode == OpCodeDefinitions.inx_implied_command:
            self.inx_command()
        elif opcode == OpCodeDefinitions.nop_implied_command:
            self.nop_command()
        elif opcode == OpCodeDefinitions.beq_relative_command:
            self.beq_command()
        elif opcode == OpCodeDefinitions.sed_implied_command:
            self.sed_command()

    def brk_command(self):
        pass

    def __is_ora_command(self, command):
        return command in [OpCodeDefinitions.ora_indirect_x_command, OpCodeDefinitions.ora_zero_page_command, OpCodeDefinitions.ora_immediate_command,
                           OpCodeDefinitions.ora_absolute_command, OpCodeDefinitions.ora_indirect_y_command,
                           OpCodeDefinitions.ora_zero_page_x_command,
                           OpCodeDefinitions.ora_absolute_y_command, OpCodeDefinitions.ora_absolute_x_command]

    def ora_command(self, input_value):
        pass

    def __is_asl_command(self, command):
        return command in [OpCodeDefinitions.asl_zero_page_command, OpCodeDefinitions.asl_accumulator_command, OpCodeDefinitions.asl_absolute_command,
                           OpCodeDefinitions.asl_zero_page_x_command, OpCodeDefinitions.asl_absolute_x_command]

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
        return command in [OpCodeDefinitions.and_indirect_x_command, OpCodeDefinitions.and_zero_page_command, OpCodeDefinitions.and_immediate_command,
                           OpCodeDefinitions.and_absolute_command, OpCodeDefinitions.and_indirect_y_command,
                           OpCodeDefinitions.and_zero_page_x_command,
                           OpCodeDefinitions.and_absolute_y_command, OpCodeDefinitions.and_absolute_x_command]

    def and_command(self, input_value):
        """Perform bitwise and on input_value and accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value & self.get_accumulator())

    def __is_bit_command(self, command):
        return command in [OpCodeDefinitions.bit_zero_page_command, OpCodeDefinitions.bit_absolute_command]

    def bit_command(self):
        pass

    def __is_rol_command(self, command):
        return command in [OpCodeDefinitions.rol_zero_page_command, OpCodeDefinitions.rol_accumulator_command, OpCodeDefinitions.rol_absolute_command,
                           OpCodeDefinitions.rol_zero_page_x_command, OpCodeDefinitions.rol_absolute_x_command]

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
        return command in [OpCodeDefinitions.eor_indirect_x_command, OpCodeDefinitions.eor_zero_page_command, OpCodeDefinitions.eor_immediate_command,
                           OpCodeDefinitions.eor_absolute_command, OpCodeDefinitions.eor_indirect_y_command,
                           OpCodeDefinitions.eor_zero_page_x_command,
                           OpCodeDefinitions.eor_absolute_y_command, OpCodeDefinitions.eor_absolute_x_command]

    def eor_command(self, input_value):
        """Perform bitwise xor on input_value and accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value ^ self.get_accumulator())

    def __is_lsr_command(self, command):
        return command in [OpCodeDefinitions.lsr_zero_page_command, OpCodeDefinitions.lsr_accumulator_command, OpCodeDefinitions.lsr_absolute_command,
                           OpCodeDefinitions.lsr_zero_page_x_command, OpCodeDefinitions.lsr_absolute_x_command]

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
        return command in [OpCodeDefinitions.adc_indirect_x_command, OpCodeDefinitions.adc_zero_page_command, OpCodeDefinitions.adc_immediate_command,
                           OpCodeDefinitions.adc_absolute_command, OpCodeDefinitions.adc_indirect_y_command,
                           OpCodeDefinitions.adc_zero_page_x_command,
                           OpCodeDefinitions.adc_absolute_y_command, OpCodeDefinitions.adc_absolute_x_command]

    def adc_command(self, input_value):
        if input_value is None:
            return

        self.set_accumulator(input_value + self.get_accumulator())

        self.clear_carry_flag()

        if self.get_accumulator() > 0xFF:
            self.set_accumulator(0xFF)
            self.set_carry_flag()

        self.clear_overflow_flag()
        if self.get_accumulator() > 127 or self.get_accumulator() < -127:
            self.set_overflow_flag()

        self.__set_zero_flag(self.get_accumulator())

    def __is_ror_command(self, command):
        return command in [OpCodeDefinitions.ror_zero_page_command, OpCodeDefinitions.ror_accumulator_command, OpCodeDefinitions.ror_absolute_command,
                           OpCodeDefinitions.ror_zero_page_x_command, OpCodeDefinitions.ror_absolute_x_command]

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
        return command in [OpCodeDefinitions.sta_indirect_x_command, OpCodeDefinitions.sta_zero_page_command, OpCodeDefinitions.sta_absolute_command,
                           OpCodeDefinitions.sta_indirect_y_command, OpCodeDefinitions.sta_zero_page_x_command,
                           OpCodeDefinitions.sta_absolute_y_command, OpCodeDefinitions.sta_absolute_x_command]

    def sta_command(self):
        pass

    def __is_sty_command(self, command):
        return command in [OpCodeDefinitions.sty_zero_page_command, OpCodeDefinitions.sty_absolute_command, OpCodeDefinitions.sty_zero_page_x_command]

    def sty_command(self):
        pass

    def __is_stx_command(self, command):
        return command in [OpCodeDefinitions.stx_zero_page_command, OpCodeDefinitions.stx_absolute_command, OpCodeDefinitions.stx_zero_page_y_command]

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
        return command in [OpCodeDefinitions.ldy_immediate_command, OpCodeDefinitions.ldy_zero_page_command, OpCodeDefinitions.ldy_absolute_command,
                           OpCodeDefinitions.ldy_zero_page_x_command, OpCodeDefinitions.ldy_absolute_x_command]

    def ldy_command(self, input_value):
        """load input_value into the y register"""
        if input_value is None:
            return

        self.__y_register = input_value

        self.__set_zero_flag(self.get_y_register())
        self.__set_negative_flag(self.get_y_register())

    def __is_lda_command(self, command):
        return command in [OpCodeDefinitions.lda_indirect_x_command, OpCodeDefinitions.lda_zero_page_command, OpCodeDefinitions.lda_immediate_command,
                           OpCodeDefinitions.lda_absolute_command, OpCodeDefinitions.lda_indirect_y_command,
                           OpCodeDefinitions.lda_zero_page_x_command, OpCodeDefinitions.lda_absolute_y_command,
                           OpCodeDefinitions.lda_absolute_x_command]

    def lda_command(self, input_value):
        """load input_value into the accumulator"""
        if input_value is None:
            return

        self.set_accumulator(input_value)

        self.__set_zero_flag(self.get_accumulator())
        self.__set_negative_flag(self.get_accumulator())

    def __is_ldx_command(self, command):
        return command in [OpCodeDefinitions.ldx_immediate_command, OpCodeDefinitions.ldx_zero_page_command, OpCodeDefinitions.ldx_absolute_command,
                           OpCodeDefinitions.ldx_zero_page_y_command, OpCodeDefinitions.ldx_absolute_y_command]

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
        return command in [OpCodeDefinitions.cpy_immediate_command, OpCodeDefinitions.cpy_zero_page_command, OpCodeDefinitions.cpy_absolute_command]

    def cpy_command(self, input_value):
        if input_value is None:
            return

        self.__set_zero_flag(input_value != self.get_y_register())
        self.__set_carry_flag_based_on_register_compare(self.get_y_register(), input_value)
        self.__set_negative_flag_based_on_register_compare(self.get_y_register(), input_value)

    def __is_cmp_command(self, command):
        return command in [OpCodeDefinitions.cmp_indirect_x_command, OpCodeDefinitions.cmp_zero_page_command, OpCodeDefinitions.cmp_immediate_command,
                           OpCodeDefinitions.cmp_absolute_command, OpCodeDefinitions.cmp_indirect_y_command,
                           OpCodeDefinitions.cmp_zero_page_x_command, OpCodeDefinitions.cmp_absolute_y_command,
                           OpCodeDefinitions.cmp_absolute_x_command]

    def cmp_command(self, input_value):
        if input_value is None:
            return

        self.__set_zero_flag(input_value != self.get_accumulator())
        self.__set_carry_flag_based_on_register_compare(self.get_accumulator(), input_value)
        self.__set_negative_flag_based_on_register_compare(self.get_accumulator(), input_value)

    def __is_dec_command(self, command):
        return command in [OpCodeDefinitions.dec_zero_page_command, OpCodeDefinitions.dec_absolute_command, OpCodeDefinitions.dec_zero_page_x_command,
                           OpCodeDefinitions.dec_absolute_x_command]

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
        return command in [OpCodeDefinitions.cpx_immediate_command, OpCodeDefinitions.cpx_zero_page_command, OpCodeDefinitions.cpx_absolute_command]

    def cpx_command(self, input_value):
        if input_value is None:
            return

        self.__set_zero_flag(input_value != self.get_x_register())
        self.__set_carry_flag_based_on_register_compare(self.get_x_register(), input_value)
        self.__set_negative_flag_based_on_register_compare(self.get_x_register(), input_value)

    def __set_carry_flag_based_on_register_compare(self, register_value, input_value):
        if register_value > input_value:
            self.__carry_flag = 0x01

    def __set_negative_flag_based_on_register_compare(self, register_value, input_value):
        if register_value < input_value:
            self.__negative_flag = 0x01

    def __is_sbc_command(self, command):
        return command in [OpCodeDefinitions.sbc_indirect_x_command, OpCodeDefinitions.sbc_zero_page_command, OpCodeDefinitions.sbc_immediate_command,
                           OpCodeDefinitions.sbc_absolute_command, OpCodeDefinitions.sbc_indirect_y_command,
                           OpCodeDefinitions.sbc_zero_page_x_command, OpCodeDefinitions.sbc_absolute_y_command,
                           OpCodeDefinitions.sbc_absolute_x_command]

    def sbc_command(self, input_value):
        if input_value is None:
            return

        result = self.get_accumulator() - input_value
        self.set_accumulator(result)

        self.clear_carry_flag()
        if result < 0:
            self.set_carry_flag()

        self.clear_overflow_flag()
        if result < -127 or result > 127:
            self.set_overflow_flag()

        self.__set_zero_flag(result)

    def __is_inc_command(self, command):
        return command in [OpCodeDefinitions.inc_zero_page_command, OpCodeDefinitions.inc_absolute_command, OpCodeDefinitions.inc_zero_page_x_command,
                           OpCodeDefinitions.inc_absolute_x_command]

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

    def set_opcode_factory(self, factory):
        self.__op_code_factory = factory



