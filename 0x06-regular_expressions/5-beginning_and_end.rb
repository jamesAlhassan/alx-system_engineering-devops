#!/usr/bin/env ruby
#Regex matching a string that starts with h ends with n and can have any single character in between

put ARGV[0].scan(/h.n/).join
