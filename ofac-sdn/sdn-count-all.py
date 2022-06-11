# Count OFACs SDN list (text version)
#  - Get totals for each type of crypto asset on the SDN list

# https://www.treasury.gov/ofac/downloads/sdnlist.txt
# https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists
# https://home.treasury.gov/policy-issues/financial-sanctions/faqs/topic/1626

import re
from collections import Counter

sdn_filename = 'sdnlist.txt'
sdn_entity = [] # Each entity on the list is separated by empty line
all_matches = []
all_matches_uniq = []

pattern_address_and_sybmol = "Digital Currency Address\s-\s[A-Z]{3,6}\s[a-zA-z0-9]+"
pattern_symbol_only = "\s[A-Z]{3,6}\s"

with open(sdn_filename) as f:
    lines = f.read()
    paragraph = lines.split("\n\n")

    # We still have line breaks so put each para into a string
    for line in paragraph:
        single_line = ' '.join( line.splitlines())
        sdn_entity.append(single_line)
        # if 'DASH ' in single_line:
        #         print('BINGO', single_line)

# Find all addrs
for sdn in sdn_entity:
    matches = re.findall(pattern_address_and_sybmol, sdn, flags=re.IGNORECASE)
    if matches:
        for m in matches:
            all_matches.append(m)

# Remove duplicate addrs
all_matches_uniq = sorted(set(all_matches))

# Addresses are only needed to get uniq count, so now get symbols
all_matches_uniq_symbols = []
total_uniq_matches = 0
for p2 in all_matches_uniq:
    matches = re.findall(pattern_symbol_only, p2)
    if matches:
        for m in matches:
            total_uniq_matches += 1
            all_matches_uniq_symbols.append(m)

# print(all_matches_uniq_symbols)

c = Counter( all_matches_uniq_symbols )
# Sort by address count
sorted = sorted(c.items(), key=lambda tup: tup[1], reverse=True)

# Print output for twitter
print('Unique addresses on US Treasury OFAC sanction list')
for name, count in sorted:
    print(name, '\t', count)
print('Number of SDN addrs: ', len(all_matches))
print('Number of uniq SDN addrs: ', len(all_matches_uniq))
print('@USTreasury #OFAC #AML #KYC') #twitter

# Sample output - with added names
#  XBT  277 (Bitcoin)
#  ETH  30 (Ethereum)
#  LTC  8 (Litecoin)
#  BCH  4 (Bitcoin Cash)
#  DASH 4 (Dash)
#  XMR  3 (Monero)
#  ZEC  3 (Zcash)
#  BSV  1 (Bitcoin SV)
#  BTG  1 (Bitcoin Gold)
#  ETC  1 (Ethereum Classic)
#  XRP  1 (Ripple)
#  XVG  1 (Verge)
