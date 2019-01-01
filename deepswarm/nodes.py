# Copyright (c) 2019 Edvinas Byla
# Licensed under MIT License


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    @classmethod
    def available_instances(cls):
        return []

    @staticmethod
    def available_transitions():
        return []

    def expand(self):
        # Reset neighbours, so we don't add same neighbours twice
        self.neighbours = []
        for node in self.available_transitions():
            self.neighbours += node.available_instances()


class InputNode(Node):
    def __init__(self):
        Node.__init__(self, "InputNode")

    @staticmethod
    def available_transitions():
        return [
            Conv2DNode,
        ]


class Conv2DNode(Node):
    def __init__(self, kernel_size):
        Node.__init__(self, "Conv2DNode")
        self.kernel_size = kernel_size

    @classmethod
    def available_instances(cls):
        return [
            cls(1),
            cls(3),
            cls(5),
        ]

    @staticmethod
    def available_transitions():
        return [
            Conv2DNode,
            MaxPool2DNode,
            FlattenNode,
        ]


class MaxPool2DNode(Node):
    def __init__(self, pool_size, strides):
        Node.__init__(self, "MaxPool2DNode")
        self.pool_size = pool_size
        self.strides = strides

    @classmethod
    def available_instances(cls):
        return [
            cls(2, 2),
            cls(2, 3),
        ]

    @staticmethod
    def available_transitions():
        return [
            Conv2DNode,
            FlattenNode,
        ]


class FlattenNode(Node):
    def __init__(self):
        Node.__init__(self, "FlattenNode")

    @classmethod
    def available_instances(cls):
        return [
            cls(),
        ]

    @staticmethod
    def available_transitions():
        return [
            DenseNode,
        ]


class DenseNode(Node):
    def __init__(self, output_size, activation):
        Node.__init__(self, "DenseNode")
        self.output_size = output_size
        self.activation = activation

    @classmethod
    def available_instances(cls):
        return [
            cls(128, "ReLu"),
            cls(256, "ReLu"),
            cls(512, "ReLu"),
        ]

    @staticmethod
    def available_transitions():
        return [
            DenseNode,
            DropoutNode
        ]


class DropoutNode(Node):
    def __init__(self, rate):
        Node.__init__(self, "DropoutNode")
        self.rate = rate

    @classmethod
    def available_instances(cls):
        return [
            cls(0.1),
            cls(0.2),
            cls(0.3),
            cls(0.4),
        ]

    @staticmethod
    def available_transitions():
        return [
            DenseNode
        ]


class ClassificationNode(Node):
    def __init__(self, output_size, activation):
        Node.__init__(self, "ClassificationNode")
        self.output_size = output_size
        self.activation = activation