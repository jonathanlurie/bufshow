# Bufshow
Print your data binary files in terminal, as numbers.

## Usage
`./bufshow.py -t float32 -f /somepath/myfloatfile.raw`  

In advance, make sure you `chmod 750 bufshow.py` before. You can also put the parent folder in your `PATH` to not have to write the `./` from `./bufshow.py`.  

Bufshow was made/tested with Python3.6 and uses only standard library.


## Features
```
-h, --help            show this help message and exit
-f FILE_PATH          Path of the file
-t {uint8,int8,uint16,int16,uint32,int32,uint64,int64,float32,float64}
                      Data type (default: uint8)
-e {little,big}       Endianess used for encoding the file: little or big
                      (default: little)
-o BYTE_OFFSET        Offset where to start reading the file, in byte
-g GROUP_BY           Grouping elements on the same line (default: 1 = no
                      grouping)
-s GROUP_SEPARATOR    Separator used for grouping (default: \t = tab)
```
Bufshow comes with some options, here is the full list:
- `--help` to print the help menu (that contains the same as this section)
- `-f` followed by a file path: the input file to be shown as a list of number (**mandatory**)
- `-t` followed by a type such as: (*optional*)
  - `uint8` 8 bits unsigned integer (1 byte) *<-- default*
  - `int8` 8 bit signed integer (1 byte)
  - `uint16` 16 bits unsigned integer (2 bytes)
  - `int16` 16 bits signed integer (2 bytes)
  - `uint32` 32 bits unsigned integer (4 bytes)
  - `int32` 32 bits signed integer (4 bytes)
  - `uint64` 64 bits unsigned integer (8 bytes)
  - `int64` 64 bits signed integer (8 bytes)
  - `float32` 32 bits floating point number (4 bytes)
  - `float64` 64 bits floating point number (4 bytes)
- `-e` the endianness, followed by `little` or `big` (default: `little`)
- `-o` offset in bytes, followed by a number (default: `0`)
- `-g` for grouping value on every row, followed by a number (default: `1`)
- `-s` separator, used for when grouping 2 values of more (default: `\t`)


## Usecases
You have a binary file that contains raw numerical values and you want to know what are the values and `cat`/`more`/`less` will generally interpret numerical values in a non-sense way.  

An other usecase is to convert binary encoded numerical series into CSV file, because it's more human readable:  
`./bufshow.py -t float32 -g 3 -s "; " -f /somepath/myfloatfile.raw`  
Here we are reading the binary file `/somepath/myfloatfile.raw` (`-f`) that we interpret as containing `float32` (`-t`) values and we want to display 3 number per line (`-g`), separated by a semicolon (`-s`).

will output something like that:  
```
3462.420654296875; 4598.78369140625; 4568.7685546875
3450.847900390625; 4637.18212890625; 4556.02880859375
3417.24951171875; 4603.84033203125; 4537.3271484375
3436.3359375; 4593.5546875; 6823.4755859375
3405.074462890625; 4674.28955078125; 6794.36328125
...
```

So to output that as a CSV file:  
`./bufshow.py -t float32 -g 3 -s "; " -f /somepath/myfloatfile.raw > /somepath/myfloatfile.csv`  
