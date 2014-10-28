from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestDexOpCode(OpCodeTestBase):

    def test_dex_implied_command_calls_dex_method(self):
        self.assert_opcode_execution(OpCodes.dex_implied_command, self.target.get_dex_command_executed)
