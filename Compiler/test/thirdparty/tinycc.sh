tinycc=`pwd`/tinycc
repo='git@github.com:TinyCC/tinycc.git'
. test/thirdparty/common
git reset --hard df67d8617b7d1d03a480a28f9f901848ffbfb7ec
./configure --cc=$tinycc
$make clean
$make
$make CC=$tinycc test
