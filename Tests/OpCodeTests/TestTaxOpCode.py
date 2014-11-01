from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTaxOpCode(OpCodeTestBase):
    def test_tax_implied_command_calls_tax_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.tax_implied_command, self.target.get_tax_command_executed)
