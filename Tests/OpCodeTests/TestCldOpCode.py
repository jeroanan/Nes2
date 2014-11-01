from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCldOpCode(OpCodeTestBase):

    def test_cld_implied_command_calls_cld_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cld_implied_command, self.target.get_cld_command_executed)
