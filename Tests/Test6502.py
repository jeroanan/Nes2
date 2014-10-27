import unittest
from Chip import OpCodes

from Tests.Chip6502Spy import Chip6502Spy


class Test6502(unittest.TestCase):

    def setUp(self):
        self.__target = Chip6502Spy()

    def test_execute_brk_command_calls_brk_method(self):
        self.assert_opcode_execution(OpCodes.brk_command, self.__target.get_brk_command_executed)

    def test_execute_ora_indirect_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_x_command, self.__target.get_ora_command_executed)

    def test_execute_ora_zero_page_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_command, self.__target.get_ora_command_executed)

    def test_execute_asl_zero_page_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_zero_page_command, self.__target.get_asl_command_executed)

    def test_execute_php_implied_command_calls_php_method(self):
        self.assert_opcode_execution(OpCodes.php_implied_command, self.__target.get_php_command_executed)

    def test_execute_ora_immediate_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_immediate_command, self.__target.get_ora_command_executed)

    def test_execute_asl_accumulator_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_accumulator_command, self.__target.get_asl_command_executed)

    def test_execute_ora_absolute_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_command, self.__target.get_ora_command_executed)

    def test_execute_asl_absolute_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_absolute_command, self.__target.get_asl_command_executed)

    def test_execute_bpl_relative_command_calls_bpl_method(self):
        self.assert_opcode_execution(OpCodes.bpl_relative_command, self.__target.get_bpl_command_executed)

    def test_execute_ora_indirect_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_y_command, self.__target.get_ora_command_executed)

    def test_execute_ora_zero_page_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_x_command, self.__target.get_ora_command_executed)

    def test_execute_asl_zero_page_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_zero_page_x_command, self.__target.get_asl_command_executed)

    def test_execute_clc_implied_command_calls_clc_method(self):
        self.assert_opcode_execution(OpCodes.clc_implied_command, self.__target.get_clc_command_executed)

    def test_execute_ora_absolute_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_y_command, self.__target.get_ora_command_executed)

    def test_execute_ora_absolute_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_x_command, self.__target.get_ora_command_executed)

    def test_execute_asl_absolute_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_absolute_x_command, self.__target.get_asl_command_executed)

    def test_execute_jsr_absolute_command_calls_jsr_method(self):
        self.assert_opcode_execution(OpCodes.jsr_absolute_command, self.__target.get_jsr_command_executed)

    def test_execute_and_indirect_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_x_command, self.__target.get_and_command_executed)

    def test_execute_bit_zero_page_calls_bit_method(self):
        self.assert_opcode_execution(OpCodes.bit_zero_page_command, self.__target.get_bit_command_executed)

    def test_execute_and_zero_page_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_command, self.__target.get_and_command_executed)

    def test_execute_rol_zero_page_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_zero_page_command, self.__target.get_rol_command_executed)

    def test_execute_plp_implied_command_calls_plp_method(self):
        self.assert_opcode_execution(OpCodes.plp_implied_command, self.__target.get_plp_command_executed)

    def test_execute_and_immediate_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_immediate_command, self.__target.get_and_command_executed)

    def test_execute_rol_accumulator_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_accumulator_command, self.__target.get_rol_command_executed)

    def test_execute_bit_absolute_command_calls_bit_method(self):
        self.assert_opcode_execution(OpCodes.bit_absolute_command, self.__target.get_bit_command_executed)

    def test_execute_and_absolute_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_command, self.__target.get_and_command_executed)

    def test_execute_rol_absolute_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_absolute_command, self.__target.get_rol_command_executed)

    def test_execute_bmi_relative_command_calls_bmi_method(self):
        self.assert_opcode_execution(OpCodes.bmi_relative_command, self.__target.get_bmi_command_executed)

    def test_execute_and_indirect_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_y_command, self.__target.get_and_command_executed)

    def test_execute_and_zero_page_x__command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_x_command, self.__target.get_and_command_executed)

    def test_execute_rol_zero_page_x_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_zero_page_x_command, self.__target.get_rol_command_executed)

    def test_execute_sec_implied_command_calls_sec_method(self):
        self.assert_opcode_execution(OpCodes.sec_implied_command, self.__target.get_sec_command_executed)

    def test_execute_and_absolute_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_y_command, self.__target.get_and_command_executed)

    def test_execute_and_absolute_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_x_command, self.__target.get_and_command_executed)

    def test_execute_and_rol_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.rol_absolute_x_command, self.__target.get_rol_command_executed)

    def test_execute_and_rti_implied_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.rti_implied_command, self.__target.get_rti_command_executed)

    def test_eor_indirect_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_indirect_x_command, self.__target.get_eor_command_executed)

    def test_eor_zero_page_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_zero_page_command, self.__target.get_eor_command_executed)

    def test_lsr_zero_page_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_zero_page_command, self.__target.get_lsr_command_executed)

    def test_pha_implied_command_calls_pha_method(self):
        self.assert_opcode_execution(OpCodes.pha_implied_command, self.__target.get_pha_command_executed)

    def test_eor_immediate_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_immediate_command, self.__target.get_eor_command_executed)

    def test_lsr_accumulator_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_accumulator_command, self.__target.get_lsr_command_executed)

    def test_eor_absolute_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_command, self.__target.get_eor_command_executed)

    def test_lsr_absolute_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_absolute_command, self.__target.get_lsr_command_executed)

    def test_bvc_relative_command_calls_bvc_method(self):
        self.assert_opcode_execution(OpCodes.bvc_relative_command, self.__target.get_bvc_command_executed)

    def test_eor_indirect_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_indirect_y_command, self.__target.get_eor_command_executed)

    def test_eor_zero_page_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_zero_page_x_command, self.__target.get_eor_command_executed)

    def test_lsr_zero_page_x_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_zero_page_x_command, self.__target.get_lsr_command_executed)

    def test_cli_implied_command_calls_cli_method(self):
        self.assert_opcode_execution(OpCodes.cli_implied_command, self.__target.get_cli_command_executed)

    def test_eor_absolute_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_y_command, self.__target.get_eor_command_executed)

    def test_eor_absolute_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_x_command, self.__target.get_eor_command_executed)

    def test_lsr_absolute_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.lsr_absolute_x_command, self.__target.get_lsr_command_executed)

    def test_rts_implied_command_calls_rts_method(self):
        self.assert_opcode_execution(OpCodes.rts_implied_command, self.__target.get_rts_command_executed)

    def test_adc_indirect_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_indirect_x_command, self.__target.get_adc_command_executed)

    def test_adc_zero_page_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_zero_page_command, self.__target.get_adc_command_executed)

    def test_ror_zero_page_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.ror_zero_page_command, self.__target.get_ror_command_executed)

    def test_pla_implied_command_calls_pla_method(self):
        self.assert_opcode_execution(OpCodes.pla_implied_command, self.__target.get_pla_command_executed)

    def test_adc_immediate_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_immediate_command, self.__target.get_adc_command_executed)

    def test_ror_accumulator_command_calls_ror_method(self):
        self.assert_opcode_execution(OpCodes.ror_accumulator_command, self.__target.get_ror_command_executed)

    def test_jmp_indirect_command_calls_jmp_method(self):
        self.assert_opcode_execution(OpCodes.jmp_indirect_command, self.__target.get_jmp_command_executed)

    def test_adc_absolute_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_command, self.__target.get_adc_command_executed)

    def test_ror_absolute_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.ror_absolute_command, self.__target.get_ror_command_executed)

    def test_bvs_relative_command_calls_bvs_method(self):
        self.assert_opcode_execution(OpCodes.bvs_relative_command, self.__target.get_bvs_command_executed)

    def test_adc_indirect_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_indirect_y_command, self.__target.get_adc_command_executed)

    def test_adc_zero_page_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_zero_page_x_command, self.__target.get_adc_command_executed)

    def test_ror_zero_page_x_command_calls_ror_method(self):
        self.assert_opcode_execution(OpCodes.ror_zero_page_x_command, self.__target.get_ror_command_executed)

    def test_sei_implied_command_calls_sei_method(self):
        self.assert_opcode_execution(OpCodes.sei_implied_command, self.__target.get_sei_command_executed)

    def test_adc_absolute_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_y_command, self.__target.get_adc_command_executed)

    def test_adc_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_x_command, self.__target.get_adc_command_executed)

    def test_ror_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.ror_absolute_x_command, self.__target.get_ror_command_executed)

    def test_sta_indirect_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_indirect_x_command, self.__target.get_sta_command_executed)

    def test_sty_zero_page_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodes.sty_zero_page_command, self.__target.get_sty_command_executed)

    def test_sta_zero_page_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_zero_page_command, self.__target.get_sta_command_executed)

    def test_stx_zero_page_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodes.stx_zero_page_command, self.__target.get_stx_command_executed)

    def test_dey_implied_command_calls_dey_method(self):
        self.assert_opcode_execution(OpCodes.dey_implied_command, self.__target.get_dey_command_executed)

    def test_txa_implied_command_calls_txa_method(self):
        self.assert_opcode_execution(OpCodes.txa_implied_command, self.__target.get_txa_command_executed)

    def test_sty_absolute_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodes.sty_absolute_command, self.__target.get_sty_command_executed)

    def test_sta_absolute_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_absolute_command, self.__target.get_sta_command_executed)

    def test_stx_absolute_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodes.stx_absolute_command, self.__target.get_stx_command_executed)

    def test_bcc_relative_command_calls_bcc_method(self):
        self.assert_opcode_execution(OpCodes.bcc_relative_command, self.__target.get_bcc_command_executed)

    def test_sta_indirect_y_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_indirect_y_command, self.__target.get_sta_command_executed)

    def test_sty_zero_page_x_command_calls_sty_method(self):
        self.assert_opcode_execution(OpCodes.sty_zero_page_x_command, self.__target.get_sty_command_executed)

    def test_sta_zero_page_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_zero_page_x_command, self.__target.get_sta_command_executed)

    def test_stx_zero_page_y_command_calls_stx_method(self):
        self.assert_opcode_execution(OpCodes.stx_zero_page_y_command, self.__target.get_stx_command_executed)

    def test_tya_implied_command_calls_tya_method(self):
        self.assert_opcode_execution(OpCodes.tya_implied_command, self.__target.get_tya_command_executed)

    def test_sta_absolute_y_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_absolute_y_command, self.__target.get_sta_command_executed)

    def test_txs_implied_command_calls_txs_method(self):
        self.assert_opcode_execution(OpCodes.txs_implied_command, self.__target.get_txs_command_executed)

    def test_sta_absolute_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodes.sta_absolute_x_command, self.__target.get_sta_command_executed)

    def test_ldy_immediate_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_immediate_command, self.__target.get_ldy_command_executed)

    def test_lda_indirect_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_indirect_x_command, self.__target.get_lda_command_executed)

    def test_ldx_immediate_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_immediate_command, self.__target.get_ldx_command_executed)

    def test_ldy_zero_page_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_command, self.__target.get_ldy_command_executed)

    def test_lda_zero_page_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_zero_page_command, self.__target.get_lda_command_executed)

    def test_ldx_zero_page_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_command, self.__target.get_ldx_command_executed)

    def test_tay_implied_command_calls_tay_method(self):
        self.assert_opcode_execution(OpCodes.tay_implied_command, self.__target.get_tay_command_executed)

    def test_lda_immediate_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_immediate_command, self.__target.get_lda_command_executed)

    def test_tax_implied_command_calls_tax_method(self):
        self.assert_opcode_execution(OpCodes.tax_implied_command, self.__target.get_tax_command_executed)

    def test_ldy_absolute_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_command, self.__target.get_ldy_command_executed)

    def test_lda_absolute_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_command, self.__target.get_lda_command_executed)

    def test_ldx_absolute_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_command, self.__target.get_ldx_command_executed)

    def test_bcs_relative_command_calls_bcs_method(self):
        self.assert_opcode_execution(OpCodes.bcs_relative_command, self.__target.get_bcs_command_executed)

    def test_lda_indirect_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_indirect_y_command, self.__target.get_lda_command_executed)

    def test_ldy_zero_page_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_x_command, self.__target.get_ldy_command_executed)

    def test_lda_zero_page_x_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_zero_page_x_command, self.__target.get_lda_command_executed)

    def test_ldx_zero_page_y_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_y_command, self.__target.get_ldx_command_executed)

    def test_clv_implied_command_calls_clv_method(self):
        self.assert_opcode_execution(OpCodes.clv_implied_command, self.__target.get_clv_command_executed)

    def test_lda_absolute_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_y_command, self.__target.get_lda_command_executed)

    def test_tsx_implied_command_calls_tsx_method(self):
        self.assert_opcode_execution(OpCodes.tsx_implied_command, self.__target.get_tsx_command_executed)

    def test_ldy_absolute_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_x_command, self.__target.get_ldy_command_executed)

    def test_lda_absolute_x_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_x_command, self.__target.get_lda_command_executed)

    def test_ldx_absolute_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_y_command, self.__target.get_ldx_command_executed)

    def test_cpy_immediate_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_immediate_command, self.__target.get_cpy_command_executed)

    def test_cmp_indirect_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_indirect_x_command, self.__target.get_cmp_command_executed)

    def test_cpy_zero_page_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_zero_page_command, self.__target.get_cpy_command_executed)

    def test_cmp_zero_page_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_zero_page_command, self.__target.get_cmp_command_executed)

    def test_dec_zero_page_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_zero_page_command, self.__target.get_dec_command_executed)

    def test_iny_implied_command_calls_iny_method(self):
        self.assert_opcode_execution(OpCodes.iny_implied_command, self.__target.get_iny_command_executed)

    def test_cmp_immediate_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_immediate_command, self.__target.get_cmp_command_executed)

    def test_dex_implied_command_calls_dex_method(self):
        self.assert_opcode_execution(OpCodes.dex_implied_command, self.__target.get_dex_command_executed)

    def test_cpy_absolute_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_absolute_command, self.__target.get_cpy_command_executed)

    def test_cmp_absolute_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_command, self.__target.get_cmp_command_executed)

    def test_dec_absolute_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_absolute_command, self.__target.get_dec_command_executed)

    def test_bne_relative_command_calls_bne_method(self):
        self.assert_opcode_execution(OpCodes.bne_relative_command, self.__target.get_bne_command_executed)

    def test_cmp_indirect_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_indirect_y_command, self.__target.get_cmp_command_executed)

    def test_cmp_zero_page_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_zero_page_x_command, self.__target.get_cmp_command_executed)

    def test_dec_zero_page_x_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_zero_page_x_command, self.__target.get_dec_command_executed)

    def test_cld_implied_command_calls_cld_method(self):
        self.assert_opcode_execution(OpCodes.cld_implied_command, self.__target.get_cld_command_executed)

    def test_cmp_absolute_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_y_command, self.__target.get_cmp_command_executed)

    def test_cmp_absolute_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_x_command, self.__target.get_cmp_command_executed)

    def test_dec_absolute_x_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_absolute_x_command, self.__target.get_dec_command_executed)

    def test_cpx_immediate_command_calls_cpx_method(self):
        self.assert_opcode_execution(OpCodes.cpx_immediate_command, self.__target.get_cpx_command_executed)

    def test_sbc_indirect_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_x_command, self.__target.get_sbc_command_executed)

    def test_cpx_zero_page_command_calls_cpx_method(self):
        self.assert_opcode_execution(OpCodes.cpx_zero_page_command, self.__target.get_cpx_command_executed)

    def test_sbc_zero_page_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_command, self.__target.get_sbc_command_executed)

    def test_inc_zero_page_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodes.inc_zero_page_command, self.__target.get_inc_command_executed)

    def test_inx_implied_command_calls_inx_method(self):
        self.assert_opcode_execution(OpCodes.inx_implied_command, self.__target.get_inx_command_executed)

    def test_sbc_immediate_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_immediate_command, self.__target.get_sbc_command_executed)

    def test_nop_implied_command_calls_nop_method(self):
        self.assert_opcode_execution(OpCodes.nop_implied_command, self.__target.get_nop_command_executed)

    def test_cpx_absolute_command_calls_cpx_method(self):
        self.assert_opcode_execution(OpCodes.cpx_absolute_command, self.__target.get_cpx_command_executed)

    def test_sbc_absolute_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_command, self.__target.get_sbc_command_executed)

    def test_inc_absolute_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodes.inc_absolute_command, self.__target.get_inc_command_executed)

    def test_beq_relative_command_calls_beq_method(self):
        self.assert_opcode_execution(OpCodes.beq_relative_command, self.__target.get_beq_command_executed)

    def test_sbc_indirect_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_y_command, self.__target.get_sbc_command_executed)

    def test_sbc_zero_page_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_x_command, self.__target.get_sbc_command_executed)

    def test_inc_zero_page_x_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodes.inc_zero_page_x_command, self.__target.get_inc_command_executed)

    def test_sed_implied_command_calls_sed_method(self):
        self.assert_opcode_execution(OpCodes.sed_implied_command, self.__target.get_sed_command_executed)

    def test_sbc_absolute_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_y_command, self.__target.get_sbc_command_executed)

    def test_sbc_absolute_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_x_command, self.__target.get_sbc_command_executed)

    def test_inc_absolute_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.inc_absolute_x_command, self.__target.get_inc_command_executed)

    def assert_opcode_execution(self, op_code, status_method):
        self.__target.execute(op_code)
        self.assertTrue(status_method())

