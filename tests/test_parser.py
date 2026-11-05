import unittest

from lsystem_abop.main import parser, preprocessor, remove_non_commands


class DocumentedCommandTests(unittest.TestCase):
    def test_documented_unicode_commands_keep_parameters_separate(self):
        for symbol, command in [("−", "-"), ("∧", "^"), ("∼", "~"), ("′", "'")]:
            with self.subTest(symbol=symbol):
                self.assertEqual(
                    parser("F10" + symbol + "90F20"),
                    ["F10", command + "90", "F20"],
                )

    def test_mixed_ascii_and_unicode_commands(self):
        self.assertEqual(
            parser("F10−90f5+45∧30&60\\20/10|$[G2.{F3}]∼1!2′3%"),
            [
                "F10", "-90", "f5", "+45", "^30", "&60", "\\20", "/10",
                "|", "$", "[", "G2", ".", "{", "F3", "}", "]", "~1",
                "!2", "'3", "%",
            ],
        )

    def test_ascii_commands_are_unchanged(self):
        self.assertEqual(parser("F30+90F30-60"), ["F30", "+90", "F30", "-60"])

    def test_unicode_commands_without_parameters_can_start_input(self):
        self.assertEqual(parser("−∧∼′F1"), ["-", "^", "~", "'", "F1"])

    def test_preprocessing_normalizes_before_joining_lines(self):
        self.assertEqual(preprocessor("F10\n  −90\n F20"), "F10-90F20")

    def test_unicode_commands_in_comments_are_ignored(self):
        self.assertEqual(
            parser("F10 # −90∧45∼2′3\n −60 # F100\n F20"),
            ["F10", "-60", "F20"],
        )

    def test_command_filter_accepts_only_documented_aliases(self):
        self.assertEqual(remove_non_commands("aλ−∧∼′→☃Ｆ１２"), "-^~'")


if __name__ == "__main__":
    unittest.main()
