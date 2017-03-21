neschr
======

NES CHR decoder.


Usage
-----

.. code-block:: python3

  import neschr

  PALETTE = ( 0x00, 0x27, 0x21, 0x30)

  decoder = neschr.TileDecoder()
  tile  = decoder.read_tile      (buf_one,   PALETTE) # one tile  (  16 Bytes)
  tiles = decoder.read_tile_table(buf_table, PALETTE) # 256 tiles (4096 Bytes)



