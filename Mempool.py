import numpy as np
import pandas as pd
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.managers import SharedMemoryManager


class SenderPort:
    def __init__(self):
        pass

    def reserve(self):
        pass

    def deliver(self):
        pass


class ReceivePort:
    def __init__(self):
        pass


class Packet:
    def __init__(self, p_mem_id, p_shape: np.shape, p_dtype: np.dtype):
        self.send_port = None
        self.receive_port = None
        self.pack_ID = p_mem_id
        self.pack_shape = p_shape
        self.pack_dtype = p_dtype

    def bind_send_port(self):
        pass

    def connect_receive_port(self):
        pass


class MemPool:
    _pool = {}

    class WriteAccess:
        def __init__(self):
            pass

    class ReadAccess:
        def __init__(self):
            pass

    def __init__(self):
        # self.chunks

        with SharedMemoryManager() as self._smm:
            pass

    def create_packet(self, p_packet_name: str, p_pack_shape: np.shape, p_pack_dtype: np.dtype):
        if p_packet_name not in self._pool.keys():
            packet_size = np.prod(p_pack_shape) * p_pack_dtype.itemsize
            self._smm.SharedMemory(name = p_packet_name, size= packet_size)
            self._pool.update(
                {p_packet_name: Packet(self._smm.SharedMemory(packet_size).name, p_pack_shape, p_pack_dtype)})

    def construct_pkt(self):
        pass

