import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_student_ranking import rank_students


class TestTask2StudentRanking(unittest.TestCase):
    """Test suite for student ranking with multi-key sorting"""

    def test_normal_case(self):
        """Test normal case from problem description"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20),
        ]
        result = rank_students(students, k=3)
        
        # Expected: eva 92 20, zoe 92 21, bob 88 19 (ian also 88 19 but comes after bob alphabetically)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], ("eva", 92, 20))
        self.assertEqual(result[1], ("zoe", 92, 21))
        self.assertEqual(result[2], ("bob", 88, 19))

    def test_top_1(self):
        """Test requesting only top 1 student"""
        students = [
            ("alice", 90, 20),
            ("bob", 85, 19),
        ]
        result = rank_students(students, k=1)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("alice", 90, 20))

    def test_all_same_score_sort_by_age(self):
        """Test tiebreak: same score sorted by age (younger first)"""
        students = [
            ("alice", 88, 25),
            ("bob", 88, 20),
            ("charlie", 88, 22),
        ]
        result = rank_students(students, k=3)
        
        # Expected order by age: bob (20), charlie (22), alice (25)
        self.assertEqual(result[0][0], "bob")
        self.assertEqual(result[1][0], "charlie")
        self.assertEqual(result[2][0], "alice")

    def test_same_score_and_age_sort_by_name(self):
        """Test tiebreak: same score and age sorted by name alphabetically"""
        students = [
            ("zoe", 88, 20),
            ("alice", 88, 20),
            ("bob", 88, 20),
        ]
        result = rank_students(students, k=3)
        
        # Expected order: alice, bob, zoe (alphabetical)
        self.assertEqual(result[0][0], "alice")
        self.assertEqual(result[1][0], "bob")
        self.assertEqual(result[2][0], "zoe")

    def test_k_greater_than_total_students(self):
        """Test when k is greater than number of students"""
        students = [
            ("alice", 90, 20),
            ("bob", 85, 19),
        ]
        result = rank_students(students, k=10)
        
        # Should return all 2 students
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], ("alice", 90, 20))
        self.assertEqual(result[1], ("bob", 85, 19))

    def test_single_student(self):
        """Test boundary case with single student"""
        students = [("alice", 88, 20)]
        result = rank_students(students, k=1)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("alice", 88, 20))

    def test_k_zero(self):
        """Test edge case where k = 0"""
        students = [
            ("alice", 90, 20),
            ("bob", 85, 19),
        ]
        result = rank_students(students, k=0)
        
        self.assertEqual(len(result), 0)

    def test_score_descending_primary_sort(self):
        """Test that score is primary sort key in descending order"""
        students = [
            ("alice", 80, 20),
            ("bob", 95, 25),
            ("charlie", 88, 19),
        ]
        result = rank_students(students, k=3)
        
        # Scores should be: 95, 88, 80 (descending)
        self.assertEqual(result[0][1], 95)
        self.assertEqual(result[1][1], 88)
        self.assertEqual(result[2][1], 80)

    def test_multiple_tiebreaks(self):
        """Test complex case with multiple tiebreak scenarios"""
        students = [
            ("zoe", 90, 20),
            ("alice", 90, 20),
            ("bob", 90, 25),
            ("charlie", 85, 20),
        ]
        result = rank_students(students, k=4)
        
        # Expected: bob (90,25), alice (90,20), zoe (90,20), charlie (85,20)
        # bob comes first (same score but older age doesn't matter, wait - age should be YOUNGER first)
        # Actually: alice (90,20), zoe (90,20), bob (90,25), charlie (85,20)
        # Scores desc: 90,90,90,85
        # Among 90s: by age asc (20 < 25): alice/zoe both (90,20), bob (90,25)
        # Among (90,20): alice < zoe alphabetically
        self.assertEqual(result[0], ("alice", 90, 20))
        self.assertEqual(result[1], ("zoe", 90, 20))
        self.assertEqual(result[2], ("bob", 90, 25))
        self.assertEqual(result[3], ("charlie", 85, 20))


if __name__ == '__main__':
    unittest.main()
