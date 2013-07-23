require '../string_matching'

if naive_string_matcher("I used to wonder what friendship could be", "wonder") == [10] and naive_string_matcher("Then we weak wear weeds weekly", "we") == [5, 8, 13, 18, 24]
  puts "naive string matching works"
else
  puts "naive string matching fails"
end

    
