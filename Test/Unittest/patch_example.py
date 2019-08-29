from unittest import TestCase, mock


class ToMockObject:
    def get_sth_by_id(self):
        return 1


def to_test_func():
    o = ToMockObject()
    return o.get_sth_by_id()


class TestObject(TestCase):
    @mock.patch("patch_example.ToMockObject")
    def test_get_sth_by_id(self, MockObject):
        instance = MockObject.return_value
        instance.get_sth_by_id.return_value = 2

        self.assertEqual(to_test_func(), 2)
