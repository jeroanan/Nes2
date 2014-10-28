from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestRolOpCode(OpCodeTestBase):

    def test_execute_rol_zero_page_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_zero_page_command, self.target.get_rol_command_executed)

    def test_execute_rol_accumulator_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_accumulator_command, self.target.get_rol_command_executed)

    def test_execute_rol_absolute_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_absolute_command, self.target.get_rol_command_executed)

    def test_execute_rol_zero_page_x_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_zero_page_x_command, self.target.get_rol_command_executed)

    def test_execute_rol_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.rol_absolute_x_command, self.target.get_rol_command_executed)