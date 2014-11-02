from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestOraOpCode(OpCodeTestBase):

    def test_execute_ora_indirect_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_indirect_x_command, self.target.get_ora_command_executed)
        self.assert_opcode_execution(OpCodeDefinitions.ora_zero_page_command, self.target.get_ora_command_executed)

    def test_ora_immediate_command_does_or_correctly(self):
        self.target.set_accumulator(0x13)
        self.target.execute(OpCodeDefinitions.ora_immediate_command, 0x37)

        actual_value = self.target.get_accumulator()

        self.assertEqual(0x13 | 0x37, actual_value)

    def test_execute_ora_absolute_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_absolute_command, self.target.get_ora_command_executed)

    def test_execute_ora_indirect_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_indirect_y_command, self.target.get_ora_command_executed)

    def test_execute_ora_zero_page_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_zero_page_x_command, self.target.get_ora_command_executed)

    def test_execute_ora_absolute_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_absolute_y_command, self.target.get_ora_command_executed)

    def test_execute_ora_absolute_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ora_absolute_x_command, self.target.get_ora_command_executed)


