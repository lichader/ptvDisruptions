import unittest
from url_builder import UrlBuilder

class TestUrlBuilder(unittest.TestCase):

    def test_calculate_signature(self):
        builder = UrlBuilder("ajdlajflsadjflsadj", "9423423")

        signature = builder.calculateSignature("/v3/route_types")
        self.assertEqual("AE1CB78FD7AA80885803B1B3CBFC126A53325972", signature)


if __name__ == '__main__':
    unittest.main()
