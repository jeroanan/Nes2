from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBplOpCode(OpCodeTestBase):

    def test_execute_bpl_relative_command_calls_bpl_method(self):
        self.assert_opcode_execution(OpCodes.bpl_relative_command, self.target.get_bpl_command_executed)
