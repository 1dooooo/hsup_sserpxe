import unittest
import sys

sys.path.append("..")
import handle


class TestHandle(unittest.TestCase):
    def test_fix_time(self):
        time_strs = ["2019-9-3 22:23:36", "1902-1-5 00:00:00",
                     "2999-12-31 23:59:59", "3999-8-5 15:36:59"]
        seconds_to_add = [2234, 1163, 22365598, 11536683]
        import time
        expec_results = ["2019-09-03 23:00:50", "1902-01-05 00:19:23",
                         "3000-09-16 20:39:57", "3999-12-17 04:15:02"]
        for i in range(0, len(time_strs)):
            self.assertEqual(handle.fix_time(
                time_strs[i], seconds_to_add[i]), expec_results[i])


if __name__ == "__main__":
    unittest.main()
