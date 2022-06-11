# Convert OFACs SDN list (text version) to a JSON
#  - Each address can have multiple entries

# https://www.treasury.gov/ofac/downloads/sdnlist.txt
# https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists
# https://home.treasury.gov/policy-issues/financial-sanctions/faqs/topic/1626

category = 'OFAC/SDN'

final_array = []
with open("sdnlist.txt") as f:
    lines = f.read()

    paragraph = lines.split("\n\n")

    i = 0

    for line in paragraph:
        single_line = ' '.join( line.splitlines())
        if '- ETH' in single_line:
            meta, second = single_line.split('Digital Currency Address', 1)

            words = second.split()
            for addr in words:
                if '0x' in addr:
                    i += 1
                    # print('--->', i, addr, category, meta)
                    obj = {
                        'address': addr,
                        'category': category,
                        'meta': meta
                    }
                    final_array.append(obj)

print("----------------------------------")
print(final_array)
