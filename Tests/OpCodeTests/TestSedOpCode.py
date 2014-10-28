from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSedOpCode(OpCodeTestBase):

    def test_sed_implied_command_calls_sed_method(self):
        self.assert_opcode_execution(OpCodes.sed_implied_command, self.target.get_sed_command_executed)
