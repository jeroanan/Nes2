from Chip.Chip6502 import Chip6502


class Chip6502Spy(Chip6502):

    def brk_command(self):
        self.__brk_command_executed = True

    def get_brk_command_executed(self):
        return self.__brk_command_executed

    def ora_command(self, input_value):
        super().ora_command(input_value)
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

    def and_command(self, input_value):
        super().and_command(input_value)
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

    def eor_command(self, input_value):
        super().eor_command(input_value)
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

    def adc_command(self, input_value):
        super().adc_command(input_value)
        self.__adc_command_executed = True

    def get_ror_command_executed(self):
        return self.__ror_command_executed

    def ror_command(self):
        self.__ror_command_executed = True

    def get_pla_command_executed(self):
        return self.__pla_command_executed

    def pla_command(self):
        self.__pla_command_executed = True

    def get_jmp_command_executed(self):
        return self.__jmp_command_executed

    def jmp_command(self):
        self.__jmp_command_executed = True

    def get_bvs_command_executed(self):
        return self.__bvs_command_executed

    def bvs_command(self):
        self.__bvs_command_executed = True

    def get_sei_command_executed(self):
        return self.__sei_command_executed

    def sei_command(self):
        self.__sei_command_executed = True

    def get_sta_command_executed(self):
        return self.__sta_command_executed

    def sta_command(self):
        self.__sta_command_executed = True

    def get_sty_command_executed(self):
        return self.__sty_command_executed

    def sty_command(self):
        self.__sty_command_executed = True

    def get_stx_command_executed(self):
        return self.__stx_command_executed

    def stx_command(self):
        self.__stx_command_executed = True

    def get_dey_command_executed(self):
        return self.__dey_command_executed

    def dey_command(self):
        self.__dey_command_executed = True

    def get_txa_command_executed(self):
        return self.__txa_command_executed

    def txa_command(self):
        self.__txa_command_executed = True

    def get_bcc_command_executed(self):
        return self.__bcc_command_executed

    def bcc_command(self):
        self.__bcc_command_executed = True

    def get_tya_command_executed(self):
        return self.__tya_command_executed

    def tya_command(self):
        self.__tya_command_executed = True

    def get_txs_command_executed(self):
        return self.__txs_command_executed

    def txs_command(self):
        self.__txs_command_executed = True

    def get_ldy_command_executed(self):
        return self.__ldy_command_executed

    def ldy_command(self):
        self.__ldy_command_executed = True

    def get_lda_command_executed(self):
        return self.__lda_command_executed

    def lda_command(self):
        self.__lda_command_executed = True

    def get_ldx_command_executed(self):
        return self.__ldx_command_executed

    def ldx_command(self):
        self.__ldx_command_executed = True

    def get_tay_command_executed(self):
        return self.__tay_command_executed

    def tay_command(self):
        self.__tay_command_executed = True

    def get_tax_command_executed(self):
        return self.__tax_command_executed

    def tax_command(self):
        self.__tax_command_executed = True

    def get_bcs_command_executed(self):
        return self.__bcs_command_executed

    def bcs_command(self):
        self.__bcs_command_executed = True

    def get_clv_command_executed(self):
        return self.__clv_command_executed

    def clv_command(self):
        self.__clv_command_executed = True

    def get_tsx_command_executed(self):
        return self.__tsx_command_executed

    def tsx_command(self):
        self.__tsx_command_executed = True

    def get_cpy_command_executed(self):
        return self.__cpy_command_executed

    def cpy_command(self):
        self.__cpy_command_executed = True

    def get_cmp_command_executed(self):
        return self.__cmp_command_executed

    def cmp_command(self):
        self.__cmp_command_executed = True

    def get_dec_command_executed(self):
        return self.__dec_command_executed

    def dec_command(self):
        self.__dec_command_executed = True

    def get_iny_command_executed(self):
        return self.__iny_command_executed

    def iny_command(self):
        self.__iny_command_executed = True

    def get_dex_command_executed(self):
        return self.__dex_command_executed

    def dex_command(self):
        self.__dex_command_executed = True

    def get_bne_command_executed(self):
        return self.__bne_command_executed

    def bne_command(self):
        self.__bne_command_executed = True

    def get_cld_command_executed(self):
        return self.__cld_command_executed

    def cld_command(self):
        self.__cld_command_executed = True

    def get_cpx_command_executed(self):
        return self.__cpx_command_executed

    def cpx_command(self):
        self.__cpx_command_executed = True

    def get_sbc_command_executed(self):
        return self.__sbc_command_executed

    def sbc_command(self):
        self.__sbc_command_executed = True

    def get_inc_command_executed(self):
        return self.__inc_command_executed

    def inc_command(self):
        self.__inc_command_executed = True

    def get_inx_command_executed(self):
        return self.__inx_command_executed

    def inx_command(self):
        self.__inx_command_executed = True

    def get_nop_command_executed(self):
        return self.__nop_command_executed

    def nop_command(self):
        self.__nop_command_executed = True

    def get_beq_command_executed(self):
        return self.__beq_command_executed

    def beq_command(self):
        self.__beq_command_executed = True

    def get_sed_command_executed(self):
        return self.__sed_command_executed

    def sed_command(self):
        self.__sed_command_executed = True

    def __init__(self):
        super().__init__()
        self.__clv_command_executed = False
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
        self.__bvs_command_executed = False
        self.__sei_command_executed = False
        self.__sta_command_executed = False
        self.__sty_command_executed = False
        self.__stx_command_executed = False
        self.__dey_command_executed = False
        self.__txa_command_executed = False
        self.__bcc_command_executed = False
        self.__tya_command_executed = False
        self.__txs_command_executed = False
        self.__ldy_command_executed = False
        self.__lda_command_executed = False
        self.__ldx_command_executed = False
        self.__tay_command_executed = False
        self.__tax_command_executed = False
        self.__bcs_command_executed = False
        self.__tsx_command_executed = False
        self.__cpy_command_executed = False
        self.__cmp_command_executed = False
        self.__dec_command_executed = False
        self.__iny_command_executed = False
        self.__dex_command_executed = False
        self.__bne_command_executed = False
        self.__cld_command_executed = False
        self.__cpx_command_executed = False
        self.__sbc_command_executed = False
        self.__inc_command_executed = False
        self.__inx_command_executed = False
        self.__nop_command_executed = False
        self.__beq_command_executed = False
        self.__sed_command_executed = False
        self.__accumulator = 0x0