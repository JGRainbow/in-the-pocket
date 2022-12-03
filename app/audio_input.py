from abc import ABC, abstractmethod

class AbstractAudioInput(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def stream_buffer(self):
        pass


class ComputerAudioInput(AbstractAudioInput):
    pass


