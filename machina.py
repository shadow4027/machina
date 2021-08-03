# imports
from binascii import crc32

class EtherFrame(object):
    """
    a class to to work with a basic 802.3 ethernet frame.
    """
    # frame constants
    ETHER_TYPE = b"\x88\x70"

    def __init__(self):
        # constants