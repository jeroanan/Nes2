from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class Test6502(OpCodeTestBase):

    def test_tay_implied_command_calls_tay_method(self):
        self.assert_opcode_execution(OpCodes.tay_implied_command, self.target.get_tay_command_executed)

    def test_tax_implied_command_calls_tax_method(self):
        self.assert_opcode_execution(OpCodes.tax_implied_command, self.target.get_tax_command_executed)

    def test_bcs_relative_command_calls_bcs_method(self):
        self.assert_opcode_execution(OpCodes.bcs_relative_command, self.target.get_bcs_command_executed)

    def test_clv_implied_command_calls_clv_method(self):
        self.assert_opcode_execution(OpCodes.clv_implied_command, self.target.get_clv_command_executed)

    def test_tsx_implied_command_calls_tsx_method(self):
        self.assert_opcode_execution(OpCodes.tsx_implied_command, self.target.get_tsx_command_executed)

    def test_dec_zero_page_command_calls_dec_method(self):
        self.assert_opcode_execution(OpCodes.dec_zero_page_command, self.target.get_dec_command_executed)

    def test_iny_implied_command_calls_iny_method(self):
        self.assert_opcode_execution(OpCodes.iny_implied_command, self.target.get_iny_command_executed)

    def test_dex_implied_command_calls_dex_method(self):
        self.assert_opcode_execution(OpCodes.dex_implied_command, self.target.get_dex_command_executed)

    def test_bne_relative_command_calls_bne_method(self):
        self.assert_opcode_execution(OpCodes.bne_relative_command, self.target.get_bne_command_executed)

    def test_cld_implied_command_calls_cld_method(self):
        self.assert_opcode_execution(OpCodes.cld_implied_command, self.target.get_cld_command_executed)

    def test_inx_implied_command_calls_inx_method(self):
        self.assert_opcode_execution(OpCodes.inx_implied_command, self.target.get_inx_command_executed)

    def test_nop_implied_command_calls_nop_method(self):
        self.assert_opcode_execution(OpCodes.nop_implied_command, self.target.get_nop_command_executed)

    def test_beq_relative_command_calls_beq_method(self):
        self.assert_opcode_execution(OpCodes.beq_relative_command, self.target.get_beq_command_executed)

    def test_sed_implied_command_calls_sed_method(self):
        self.assert_opcode_execution(OpCodes.sed_implied_command, self.target.get_sed_command_executed)


