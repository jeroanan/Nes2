from Chip import OpCodes


class Chip6502(object):

    def __init__(self):
        self.accumulator = 0x00

    def set_accumulator(self, value):
        self.accumulator = value

    def get_accumulator(self):
        return self.accumulator

    def execute(self, command, operand=None):
        if command == OpCodes.brk_command:
            self.brk_command()
        elif self.is_ora_command(command):
            self.ora_command(operand)
        elif self.is_asl_command(command):
            self.asl_command()
        elif command == OpCodes.php_implied_command:
            self.php_command()
        elif command == OpCodes.bpl_relative_command:
            self.bpl_command()
        elif command == OpCodes.clc_implied_command:
            self.clc_command()
        elif command == OpCodes.jsr_absolute_command:
            self.jsr_command()
        elif self.is_and_command(command):
            self.and_command()
        elif self.is_bit_command(command):
            self.bit_command()
        elif self.is_rol_command(command):
            self.rol_command()
        elif command == OpCodes.plp_implied_command:
            self.plp_command()
        elif command == OpCodes.bmi_relative_command:
            self.bmi_command()
        elif command == OpCodes.sec_implied_command:
            self.sec_command()
        elif command == OpCodes.rti_implied_command:
            self.rti_command()
        elif self.is_eor_command(command):
            self.eor_command()
        elif self.is_lsr_command(command):
            self.lsr_command()
        elif command == OpCodes.pha_implied_command:
            self.pha_command()
        elif command == OpCodes.bvc_relative_command:
            self.bvc_command()
        elif command == OpCodes.cli_implied_command:
            self.cli_command()
        elif command == OpCodes.rts_implied_command:
            self.rts_command()
        elif self.is_adc_command(command):
            self.adc_command()
        elif self.is_ror_command(command):
            self.ror_command()
        elif command == OpCodes.pla_implied_command:
            self.pla_command()
        elif command == OpCodes.jmp_indirect_command:
            self.jmp_command()
        elif command == OpCodes.bvs_relative_command:
            self.bvs_command()
        elif command == OpCodes.sei_implied_command:
            self.sei_command()
        elif self.is_sta_command(command):
            self.sta_command()
        elif self.is_sty_command(command):
            self.sty_command()
        elif self.is_stx_command(command):
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
        elif self.is_ldy_command(command):
            self.ldy_command()
        elif self.is_lda_command(command):
            self.lda_command()
        elif self.is_ldx_command(command):
            self.ldx_command()
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
        elif self.is_cpy_command(command):
            self.cpy_command()
        elif self.is_cmp_command(command):
            self.cmp_command()
        elif self.is_dec_command(command):
            self.dec_command()
        elif command == OpCodes.iny_implied_command:
            self.iny_command()
        elif command == OpCodes.dex_implied_command:
            self.dex_command()
        elif command == OpCodes.bne_relative_command:
            self.bne_command()
        elif command == OpCodes.cld_implied_command:
            self.cld_command()
        elif self.is_cpx_command(command):
            self.cpx_command()
        elif self.is_sbc_command(command):
            self.sbc_command()
        elif self.is_inc_command(command):
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

    def is_ora_command(self, command):
        return command in [OpCodes.ora_indirect_x_command, OpCodes.ora_zero_page_command, OpCodes.ora_immediate_command,
                           OpCodes.ora_absolute_command, OpCodes.ora_indirect_y_command,
                           OpCodes.ora_zero_page_x_command,
                           OpCodes.ora_absolute_y_command, OpCodes.ora_absolute_x_command]

    def ora_command(self, input_value):
        if input_value is None:
            return

        self.set_accumulator(input_value | self.get_accumulator())

    def is_asl_command(self, command):
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

    def is_and_command(self, command):
        return command in [OpCodes.and_indirect_x_command, OpCodes.and_zero_page_command, OpCodes.and_immediate_command,
                           OpCodes.and_absolute_command, OpCodes.and_indirect_y_command,
                           OpCodes.and_zero_page_x_command,
                           OpCodes.and_absolute_y_command, OpCodes.and_absolute_x_command]

    def and_command(self):
        pass

    def is_bit_command(self, command):
        return command in [OpCodes.bit_zero_page_command, OpCodes.bit_absolute_command]

    def bit_command(self):
        pass

    def is_rol_command(self, command):
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

    def is_eor_command(self, command):
        return command in [OpCodes.eor_indirect_x_command, OpCodes.eor_zero_page_command, OpCodes.eor_immediate_command,
                           OpCodes.eor_absolute_command, OpCodes.eor_indirect_y_command,
                           OpCodes.eor_zero_page_x_command,
                           OpCodes.eor_absolute_y_command, OpCodes.eor_absolute_x_command]

    def eor_command(self):
        pass

    def is_lsr_command(self, command):
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

    def is_adc_command(self, command):
        return command in [OpCodes.adc_indirect_x_command, OpCodes.adc_zero_page_command, OpCodes.adc_immediate_command,
                           OpCodes.adc_absolute_command, OpCodes.adc_indirect_y_command,
                           OpCodes.adc_zero_page_x_command,
                           OpCodes.adc_absolute_y_command, OpCodes.adc_absolute_x_command]

    def adc_command(self):
        pass

    def is_ror_command(self, command):
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

    def is_sta_command(self, command):
        return command in [OpCodes.sta_indirect_x_command, OpCodes.sta_zero_page_command, OpCodes.sta_absolute_command,
                           OpCodes.sta_indirect_y_command, OpCodes.sta_zero_page_x_command,
                           OpCodes.sta_absolute_y_command, OpCodes.sta_absolute_x_command]

    def sta_command(self):
        pass

    def is_sty_command(self, command):
        return command in [OpCodes.sty_zero_page_command, OpCodes.sty_absolute_command, OpCodes.sty_zero_page_x_command]

    def sty_command(self):
        pass

    def is_stx_command(self, command):
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

    def is_ldy_command(self, command):
        return command in [OpCodes.ldy_immediate_command, OpCodes.ldy_zero_page_command, OpCodes.ldy_absolute_command,
                           OpCodes.ldy_zero_page_x_command, OpCodes.ldy_absolute_x_command]

    def ldy_command(self):
        pass

    def is_lda_command(self, command):
        return command in [OpCodes.lda_indirect_x_command, OpCodes.lda_zero_page_command, OpCodes.lda_immediate_command,
                           OpCodes.lda_absolute_command, OpCodes.lda_indirect_y_command,
                           OpCodes.lda_zero_page_x_command, OpCodes.lda_absolute_y_command,
                           OpCodes.lda_absolute_x_command]

    def lda_command(self):
        pass

    def is_ldx_command(self, command):
        return command in [OpCodes.ldx_immediate_command, OpCodes.ldx_zero_page_command, OpCodes.ldx_absolute_command,
                           OpCodes.ldx_zero_page_y_command, OpCodes.ldx_absolute_y_command]

    def ldx_command(self):
        pass

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

    def is_cpy_command(self, command):
        return command in [OpCodes.cpy_immediate_command, OpCodes.cpy_zero_page_command, OpCodes.cpy_absolute_command]

    def cpy_command(self):
        pass

    def is_cmp_command(self, command):
        return command in [OpCodes.cmp_indirect_x_command, OpCodes.cmp_zero_page_command, OpCodes.cmp_immediate_command,
                           OpCodes.cmp_absolute_command, OpCodes.cmp_indirect_y_command,
                           OpCodes.cmp_zero_page_x_command, OpCodes.cmp_absolute_y_command,
                           OpCodes.cmp_absolute_x_command]

    def cmp_command(self):
        pass

    def is_dec_command(self, command):
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

    def is_cpx_command(self, command):
        return command in [OpCodes.cpx_immediate_command, OpCodes.cpx_zero_page_command, OpCodes.cpx_absolute_command]

    def cpx_command(self):
        pass

    def is_sbc_command(self, command):
        return command in [OpCodes.sbc_indirect_x_command, OpCodes.sbc_zero_page_command, OpCodes.sbc_immediate_command,
                           OpCodes.sbc_absolute_command, OpCodes.sbc_indirect_y_command,
                           OpCodes.sbc_zero_page_x_command, OpCodes.sbc_absolute_y_command,
                           OpCodes.sbc_absolute_x_command]

    def sbc_command(self):
        pass

    def is_inc_command(self, command):
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




