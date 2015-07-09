#!/bin/bash
# Update the source code

[ `hostname` != 'seaman-chute' ] && cat $pt/update.correct && exit

doc-diff-all $jack src-jack
#doc-pull    $jack src-jack

