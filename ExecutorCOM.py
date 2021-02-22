from ExecutorBase import ExecutorBase
from abc import abstractmethod
import os
import time


class DataCollectInterface:
    def __init__(self):
        pass

    @abstractmethod
    def collect(self):
        pass


class DataOutsideInterfaceEth(DataCollectInterface):
    def __init__(self, p_socket):
        super(DataOutsideInterfaceEth, self).__init__()
        self.if_socket = p_socket

    def collect(self):
        pass


class ExecutorCOM(ExecutorBase):
    def __init__(self, p_data_collect_if: DataCollectInterface):
        super(ExecutorCOM, self).__init__()
        # Process.__init__(self)
        self._data_outside = p_data_collect_if

    def run(self) -> None:
        print("subprocess，pid=%d，father process：%d" % (os.getpid(), os.getppid()))
        t_start = time.time()

        t_end = time.time()
        print("subprocess end，time cost：%0.2fs" % (t_end - t_start))
