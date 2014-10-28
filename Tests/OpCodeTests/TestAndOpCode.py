from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestAndOpCode(OpCodeTestBase):

    def test_execute_and_indirect_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_x_command, self.target.get_and_command_executed)

    def test_execute_and_zero_page_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_command, self.target.get_and_command_executed)

    def test_and_immediate_command_does_and_correctly(self):
        self.target.set_accumulator(0x30)
        self.target.execute(OpCodes.and_immediate_command, 0x29)

        expected_value = 0x30 & 0x29
        actual_value = self.target.get_accumulator()

        self.assertEqual(expected_value, actual_value)

    def test_execute_and_absolute_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_command, self.target.get_and_command_executed)

    def test_execute_and_indirect_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_y_command, self.target.get_and_command_executed)

    def test_execute_and_zero_page_x__command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_x_command, self.target.get_and_command_executed)

    def test_execute_and_absolute_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_y_command, self.target.get_and_command_executed)

    def test_execute_and_absolute_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_x_command, self.target.get_and_command_executed)


