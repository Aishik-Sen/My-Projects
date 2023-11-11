# Rename the chibicc variable
tinycc=`pwd`/tinycc

# Update the Git Repository Setup
repo='git@github.com:python/cpython.git'
. test/thirdparty/common
git reset --hard c75330605d4795850ec74fdc4d69aa5d92f76c00

# Workaround for configure Issue
sed -i -e 1996,2011d configure.ac
autoreconf

# Configure and Build with tinycc
CC=$tinycc ./configure
$make clean
$make

# Run Tests
$make test
