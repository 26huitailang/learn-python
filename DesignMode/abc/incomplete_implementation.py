import abc


class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return


class IncompleteImplementation(PluginBase):
    # 如果没有实现两个方法的话，该类不能实例化
    def load(self):
        return

    def save(self, output):
        return output.write("")


if __name__ == "__main__":
    print("Subclass:", issubclass(IncompleteImplementation, PluginBase))
    print("Instance:", isinstance(IncompleteImplementation(), PluginBase))
