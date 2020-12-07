import os
# list all include directories
include_directories = [os.path.sep.join(x.split('/')) for x in ['extension/fts/include', 'third_party/snowball']]
# source files
source_files = [os.path.sep.join(x.split('/')) for x in ['extension/fts/fts-extension.cpp', 'extension/fts/fts_indexing.cpp']]
# snowball
source_files += [os.path.sep.join(x.split('/')) for x in ['third_party/snowball/libstemmer/libstemmer.c', 'third_party/snowball/runtime/utilities.c', 'third_party/snowball/runtime/api.c', 'third_party/snowball/src_c/stem_UTF_8_arabic.c', 'third_party/snowball/src_c/stem_UTF_8_basque.c', 'third_party/snowball/src_c/stem_UTF_8_catalan.c', 'third_party/snowball/src_c/stem_UTF_8_danish.c', 'third_party/snowball/src_c/stem_UTF_8_dutch.c', 'third_party/snowball/src_c/stem_UTF_8_english.c', 'third_party/snowball/src_c/stem_UTF_8_finnish.c', 'third_party/snowball/src_c/stem_UTF_8_french.c', 'third_party/snowball/src_c/stem_UTF_8_german.c', 'third_party/snowball/src_c/stem_UTF_8_german2.c', 'third_party/snowball/src_c/stem_UTF_8_greek.c', 'third_party/snowball/src_c/stem_UTF_8_hindi.c', 'third_party/snowball/src_c/stem_UTF_8_hungarian.c', 'third_party/snowball/src_c/stem_UTF_8_indonesian.c', 'third_party/snowball/src_c/stem_UTF_8_irish.c', 'third_party/snowball/src_c/stem_UTF_8_italian.c', 'third_party/snowball/src_c/stem_UTF_8_kraaij_pohlmann.c', 'third_party/snowball/src_c/stem_UTF_8_lithuanian.c', 'third_party/snowball/src_c/stem_UTF_8_lovins.c', 'third_party/snowball/src_c/stem_UTF_8_nepali.c', 'third_party/snowball/src_c/stem_UTF_8_norwegian.c', 'third_party/snowball/src_c/stem_UTF_8_porter.c', 'third_party/snowball/src_c/stem_UTF_8_portuguese.c', 'third_party/snowball/src_c/stem_UTF_8_romanian.c', 'third_party/snowball/src_c/stem_UTF_8_russian.c', 'third_party/snowball/src_c/stem_UTF_8_serbian.c', 'third_party/snowball/src_c/stem_UTF_8_spanish.c', 'third_party/snowball/src_c/stem_UTF_8_swedish.c', 'third_party/snowball/src_c/stem_UTF_8_tamil.c', 'third_party/snowball/src_c/stem_UTF_8_turkish.c']]

