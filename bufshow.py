#!/usr/bin/env python3

import argparse
import struct
import sys
import codecs

explicit_type_to_struct_type = {
    "uint8": "B",
    "int8": "b",
    "uint16": "H",
    "int16": "h",
    "uint32": "I",
    "int32": "i",
    "uint64": "Q",
    "int64": "q",
    "float32": "f",
    "float64": "d"
}


type_to_byte_size = {
    "uint8": 1,
    "int8": 1,
    "uint16": 2,
    "int16": 2,
    "uint32": 4,
    "int32": 4,
    "uint64": 8,
    "int64": 8,
    "float32": 4,
    "float64": 8
}


explicit_endianness_to_byteorder = {
    "little": "<",
    "big": ">"
}


def unescaped_str(arg_str):
    return codecs.decode(str(arg_str), 'unicode_escape')


if __name__ == "__main__":

    description = """
    Show the content of binary files, interpreted as numbers.
    Fork it! https://github.com/jonathanlurie/bufshow
    """

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", required=True, dest="file_path", help="Path of the file")
    parser.add_argument("-t", required=False, dest="data_type", default="uint8", choices=["uint8", "int8", "uint16", "int16", "uint32", "int32", "uint64", "int64", "float32", "float64"], help="Data type (default: %(default)s)")
    parser.add_argument("-e", required=False, dest="endianess", default="little", choices=["little", "big"], help="Endianess used for encoding the file: little or big (default: %(default)s)")
    parser.add_argument("-o", required=False, dest="byte_offset", default=0, help="Offset where to start reading the file, in byte")
    parser.add_argument("-g", required=False, dest="group_by", default=1, help="Grouping elements on the same line (default: 1 = no grouping)")
    parser.add_argument("-s", required=False, dest="group_separator", default="\t", type=unescaped_str, help="Separator used for grouping (default: \\t = tab)")

    args = vars(parser.parse_args())

    group_by = int(args["group_by"])
    separator = args["group_separator"]
    data_type = args["data_type"]
    endianess = args["endianess"]

    try:
        with open(args["file_path"], 'rb') as f:
            f.seek(int(args["byte_offset"]))

            bin_data = f.read()
            nb_elements = int( len(bin_data) / type_to_byte_size[data_type])
            struct_type = explicit_endianness_to_byteorder[endianess] + str(nb_elements)  + explicit_type_to_struct_type[data_type]
            numbers = struct.unpack(struct_type, bin_data)

            if group_by == 1:
                for i in numbers:
                    print(i)
            else:
                for i in range(0, len(numbers), group_by):
                    row = []

                    for n in range(0, group_by):
                        try:
                            row.append(str(numbers[i+n]))
                        except:
                            pass
                    print( separator.join(row) )

    except BrokenPipeError as e:
        sys.stderr.close()
        exit(1)

    except KeyboardInterrupt as e:
        exit(1)
