from mars_patcher.constants.game_data import tileset_entries
from mars_patcher.rom import Rom


class Tileset(object):
    def __init__(self, rom: Rom, id: int):
        self.rom = rom
        self.addr = tileset_entries(rom) + id * 0x14

    def rle_tilemap_addr(self) -> int:
        return self.rom.read_ptr(self.addr + 0xC)
