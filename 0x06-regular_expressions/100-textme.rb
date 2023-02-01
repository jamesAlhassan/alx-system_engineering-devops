#!/usr/bin/env ruby
#Regex matches a given pattern

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
