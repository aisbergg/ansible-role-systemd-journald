class TestModule(object):
    def tests(self):
        return {
            'boolean': self.is_boolean,
        }

    def is_boolean(self, value):
        """Tests if a value is of type boolean.

        Jinja2 >= 2.11 comes a built-in boolean test, but most systems will ship
        an older version. This test function will be kept, until the majority of
        distributions ship version >= 2.11.

        Args:
            value: A value, that shall be type tested

        Returns:
            bool: True, if value is of type boolean, False otherwise.
        """
        return isinstance(value, bool)
