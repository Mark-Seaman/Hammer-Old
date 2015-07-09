#!/usr/bin/perl

$count='0';
while ($line = <>) {
    $count='1'+$count;
    if ($line=~s/^(.*\/)([^\/]*)(\.rcp)\n$/mv \1\2\3 \1$count\3/) {
        print "$line\n";
    }
}
