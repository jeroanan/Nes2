from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBneOpCode(OpCodeTestBase):

    def test_bne_relative_command_calls_bne_method(self):
        self.assert_opcode_execution(OpCodes.bne_relative_command, self.target.get_bne_command_executed)
