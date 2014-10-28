from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLsrOpCode(OpCodeTestBase):
    def test_lsr_accumulator_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_accumulator_command, self.target.get_lsr_command_executed)

    def test_lsr_absolute_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_absolute_command, self.target.get_lsr_command_executed)

    def test_lsr_absolute_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.lsr_absolute_x_command, self.target.get_lsr_command_executed)

    def test_lsr_zero_page_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_zero_page_command, self.target.get_lsr_command_executed)

    def test_lsr_zero_page_x_command_calls_lsr_method(self):
        self.assert_opcode_execution(OpCodes.lsr_zero_page_x_command, self.target.get_lsr_command_executed)
