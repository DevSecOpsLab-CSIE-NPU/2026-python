"""R03-inheritance.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR03Inheritance(unittest.TestCase):
    """確認繼承、覆寫與 super() 範例的行為。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R03-inheritance.py")

    def test_animal_and_subclasses_have_expected_speak(self):
        dog = self.module.Dog("小黑")
        cat = self.module.Cat("咪咪")

        self.assertEqual("小黑 說：汪汪！", dog.speak())
        self.assertEqual("咪咪 說：喵～", cat.speak())
        self.assertEqual("Dog('小黑')", repr(dog))

    def test_guidedog_uses_super_for_name_and_speak(self):
        guide_dog = self.module.GuideDog("阿金", "王伯伯")

        self.assertEqual("阿金", guide_dog.name)
        self.assertEqual("王伯伯", guide_dog.owner)
        self.assertEqual("阿金 說：汪汪！（導盲犬，主人：王伯伯）", guide_dog.speak())

    def test_make_sounds_collects_polymorphic_results(self):
        animals = [
            self.module.Dog("小黑"),
            self.module.Cat("咪咪"),
            self.module.GuideDog("阿金", "王伯伯"),
        ]

        self.assertEqual(
            [
                "小黑 說：汪汪！",
                "咪咪 說：喵～",
                "阿金 說：汪汪！（導盲犬，主人：王伯伯）",
            ],
            self.module.make_sounds(animals),
        )

    def test_isinstance_and_issubclass_relationships(self):
        dog = self.module.Dog("小黑")

        self.assertTrue(isinstance(dog, self.module.Dog))
        self.assertTrue(isinstance(dog, self.module.Animal))
        self.assertFalse(isinstance(dog, self.module.Cat))
        self.assertTrue(issubclass(self.module.Dog, self.module.Animal))
        self.assertFalse(issubclass(self.module.Cat, self.module.Dog))


if __name__ == "__main__":
    unittest.main()
