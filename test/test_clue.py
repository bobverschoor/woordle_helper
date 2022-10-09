import unittest

from model.clue import Clue


class ClueTest(unittest.TestCase):
    def setUp(self):
        self.clue_6letters = Clue(["a0a0n0t0a1l0", "e0r0o1p0a1f0", "m0i0m0o2s0a2"])
        self.clue_5letters = Clue(["t0a0n0t0e1", "b0e0d0e2l2", "k0o2g0e2l2", "f0o2r0e2l2"])
        self.clue_wrong = Clue(["t2e0d0f1g1", "d2e0d0f1g1"])

    def test_clue_woordlengte(self):
        self.assertEqual(6, self.clue_6letters._woordlengte)
        self.assertEqual(5, self.clue_5letters._woordlengte)

    def test_woordenboek(self):
        self.clue_6letters.woorden_van_juiste_lengte()
        self.clue_5letters.woorden_van_juiste_lengte()
        self.assertEqual(7662, len(self.clue_6letters._woordenlijst))
        self.assertEqual(3982, len(self.clue_5letters._woordenlijst))
        self.assertTrue("flink" in self.clue_5letters.woordenlijst)

    def test_forbidden_letters(self):
        forbidden = self.clue_6letters.forbidden_letters
        self.assertEqual("efilmnprst", ''.join(sorted(forbidden)))
        forbidden = self.clue_5letters.forbidden_letters
        self.assertEqual("abdfgknrt", ''.join(sorted(forbidden)))

    def test_present_right_spot(self):
        self.assertEqual("...o.a", self.clue_6letters._get_present_right_spot())
        self.assertEqual(".o.el", self.clue_5letters._get_present_right_spot())
        self.assertRaises(Exception, self.clue_wrong._get_present_right_spot)

    def test_has_forbidden_letters(self):
        clue = Clue(["d0e0l1t0a0", "s0c0h0i1l1", "k0l2i2k1o0", "b0l2i2j0k2"])
        self.assertFalse(clue.has_forbidden_letters("flink"))
        clue = Clue(["s0p0a0a0n2", "b0e2g0i0n2", "d0e2m0o0n2", "t0e2l0e2n2", "w0e2k0e2n2", "v0e2r2e2n2"])
        self.assertFalse(clue.has_forbidden_letters("heren"))
        clue = Clue(["a0a1n0t0a2l0", "b0e0r1a2a2m0", "s2c0h0a2a2r2"])
        self.assertFalse(clue.has_forbidden_letters("sigaar"))

    def test_fit_woord(self):
        self.assertTrue(self.clue_5letters.fit_woord("motel"))
        self.assertFalse(self.clue_5letters.fit_woord("horen"))
        self.assertTrue(self.clue_6letters.fit_woord("mimosa"))
        self.assertFalse(self.clue_6letters.fit_woord("aantal"))
        clue = Clue(["s0p0a0a0n2", "b0e2g0i0n2", "d0e2m0o0n2"])
        self.assertTrue(clue.fit_woord("telen"))
        clue = Clue(["s0p0a0a0n2", "b0e2g0i0n2", "d0e2m0o0n2", "t0e2l0e2n2", "w0e2k0e2n2", "v0e2r2e2n2"])
        self.assertTrue(clue.fit_woord("heren"))
        clue = Clue(["a0a1n0t0a2l0", "b0e0r1a2a2m0", "s2c0h0a2a2r2"])
        self.assertTrue(clue.fit_woord("sigaar"))

    def test_present_wrong_spot(self):
        self.assertEqual(["....[^a].", "..[^o].[^a].", "......"], self.clue_6letters._get_present_wrong_spot())
        self.assertEqual(["....[^e]", ".....", ".....", "....."], self.clue_5letters._get_present_wrong_spot())

    def test_fit_woord_reeks(self):
        self.assertTrue(self.clue_5letters.fit_woord("motel"))
        self.assertFalse(self.clue_5letters.fit_woord("tante"))
        self.assertTrue(self.clue_6letters.fit_woord("judoka"))
        self.assertFalse(self.clue_6letters.fit_woord("gedaan"))
        clue = Clue(["b0r1e2e0d1"])
        self.assertFalse(clue.fit_reeks_woord("arend"))

    def test_present_anywhere(self):
        self.assertEqual({"a": 1, "o": 1}, self.clue_6letters._get_present_anywhere())
        self.assertEqual({"e": 1, "l": 1, "o": 1}, self.clue_5letters._get_present_anywhere())

    def test_has_required_letters(self):
        clue = Clue(["s0p0a2a2n2"])  # spaan => kraan
        self.assertFalse(clue.has_required_letters("krant"))
        self.assertTrue(clue.has_required_letters("kraan"))
        clue = Clue(["s0p0a0a0n2", "b0e2g0i0n2", "d0e2m0o0n2"])
        self.assertTrue(clue.has_required_letters("telen"))
        clue = Clue(["s0p0a0a0n2", "b0e2g0i0n2", "d0e2m0o0n2", "t0e2l0e2n2", "w0e2k0e2n2", "v0e2r2e2n2"])
        self.assertTrue(clue.has_required_letters("heren"))
        clue = Clue(["a0a1n0t0a2l0", "b0e0r1a2a2m0", "s2c0h0a2a2r2"])
        self.assertTrue(clue.has_required_letters("sigaar"))


if __name__ == '__main__':
    unittest.main()
