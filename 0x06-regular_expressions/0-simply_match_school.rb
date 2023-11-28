#!/usr/bin/env ruby

regex = /School/
input = ARGV[0]

match = input.match(regex)
if match
  puts "School"
end
