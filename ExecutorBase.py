from multiprocessing import Process


class ExecutorBase(Process):
    """
    Below tasks should be implemented in this class
    1. Data writer , reader initialization
    2. Sender ports and receiver ports initialization
    3. basic running process definition
    """
    def __init__(self):
        super(ExecutorBase, self).__init__()

    def run(self) -> None:
        pass
