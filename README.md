# Extra-Zip

Zip compressors and decompressors are surprisingly nieve and will trust that the data they are given is indeed correct with minimal verification. 
Of particular interest is the extrafield found inside the local file header. In the specification this field is described by:

> This is for expansion. If additional information
> needs to be stored for special needs or for specific
> platforms, it should be stored here. Earlier versions
> of the software can then safely skip this file, and
> find the next file or header. This field will be 0
> length in version 1.0.

Rather surprisingly most if not all zip tools completely ignore this field (despite there being potentially useful information) 
and if the extra field contradicts the local header they tend to follow the local header (this is extremely rare anyway)
The upshot of this is that we can store additional data inside the extrafield without effecting the zip files decompression. 
This utility is more of a POC rather than a final product however it does infact have the ability to add data to compressed files that 
the following utilties fail to notice (on default settings of compression):
- Winrar
- gzip
- zip
- 7zip

## Usage
``extra-hide.py`` contains the script to add information to a given zip file with the call signature ``python extra-hide.py file_to_hide file_to_hide_in``

Similarly ``extra-reveal.py`` gets that information via ``python extra-reveal.py zip_file output_file``

Currently limited to ~6000 bytes of data to hide.

## References:
- http://www.idea2ic.com/File_Formats/ZIP%20File%20Format%20Specification.pdf
