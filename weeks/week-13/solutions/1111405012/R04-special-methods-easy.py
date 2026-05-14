"""R04 特殊方法詳細註解版。"""

from functools import total_ordering


@total_ordering
class Score:
    # 加上 total_ordering 後，
    # 只要寫 __eq__ 和一個大小比較方法，
    # 其他像 >、<=、>= 會自動幫你推導出來。
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add(self, student):
        self.students.append(student)

    def __len__(self):
        # len(classroom) 時會呼叫這裡。
        return len(self.students)

    def __contains__(self, student):
        # "Alice" in classroom 時會呼叫這裡。
        return student in self.students

    def __iter__(self):
        # for student in classroom 時會呼叫這裡。
        return iter(self.students)


def main():
    scores = [Score("Alice", 90), Score("Bob", 75), Score("Carol", 90)]
    print(sorted(scores))

    classroom = Classroom("資工一甲")
    classroom.add("Alice")
    classroom.add("Bob")
    classroom.add("Carol")
    print(len(classroom))
    print("Alice" in classroom)
    for student in classroom:
        print(student)


if __name__ == "__main__":
    main()
