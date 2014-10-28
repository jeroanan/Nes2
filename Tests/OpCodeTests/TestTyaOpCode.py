from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTyaOpCode(OpCodeTestBase):
    def test_tya_implied_command_calls_tya_method(self):
        self.assert_opcode_execution(OpCodes.tya_implied_command, self.target.get_tya_command_executed)
