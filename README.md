# rohc_python
Experimental Python bindings for the ROHC library

ROHC Library found at https://rohc-lib.org/

This extension is written in C and tries to simplify the interface.  Feedback still needs to be handled manualy if traffic is unidirectional.

Example:

hc = rohc.ROHC(True)
hc.activate_profiles(["IP","UDP"])

// Get an IP packet to compress and store it in ip_data
data_to_send = hc.compress(ip_data)
hc_info = hc.last_compressed_info()

// Receive a compressed packet from a different compressor
decompressed_pkt = hc.decompress(rohc_pkt)
hc_info = hc.last_decompressed_info()

// Show available general stats from the ROHC library
hc_info = hc.general_info()
