import numpy as np
import pandas as pd
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.managers import SharedMemoryManager


class MemPoolType:
    _pool = {}
    _datatype = None

    def __init__(self, p_chunk_shape: np.shape, p_chunk_dtype: np.dtype):
        self.chunk_shape = p_chunk_shape
        self.chunk_dtype = p_chunk_dtype
        with SharedMemoryManager() as self._smm:
            pass

    def create_packet(self, p_packet_name: str, ):
        if p_packet_name not in self._pool.keys():
            packet_size = np.prod(p_pack_shape) * p_pack_dtype.itemsize
            self._smm.SharedMemory(name=p_packet_name, size=packet_size)
            self._pool.update(
                {p_packet_name: Packet(self._smm.SharedMemory(packet_size).name, p_pack_shape, p_pack_dtype)})

    def construct_pkt(self):
        pass


class SenderPort:
    def __init__(self):
        self.mempool = None

    def connect_mempool(self, p_mempool: MemPoolType):
        self.mempool = p_mempool

    def is_mempool_connected(self) -> bool:
        pass

    def connect(self, p_subscriber: SubscriberType):
        pass

    def is_connected(self) -> bool:
        pass

    def reserve(self, default_construct=True):
        pass

    def reserve_last_delivery(self):
        pass

    def is_reserved(self):
        pass

    def deliver(self):
        pass


class ReceivePort:
    def __init__(self):
        pass

    def is_connected(self) -> bool:
        pass

    def update(self):
        pass

    def has_new_data(self) -> bool:
        pass

    def has_data(self) -> bool:
        pass

    def peek_new_data(self) -> bool:
        pass

    def get_data(self):
        pass

    def cleanup(self):
        pass

class WrappedSharedMemory:
    def __init__(self, p_mem_id, p_shape: np.shape, p_dtype: np.dtype):
        self.send_port = None
        self.receive_ports = []
        self.pack_ID = p_mem_id
        self.pack_shape = p_shape
        self.pack_dtype = p_dtype

    def bind_send_port(self):
        pass

    def connect_receive_port(self):
        pass




