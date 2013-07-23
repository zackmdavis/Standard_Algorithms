def naive_string_matcher(text, pattern)
  n = text.length
  m = pattern.length
  shifts = []
  (0..n-m).each do |i|
    if pattern[0..m-1] == text[i..i+m-1]
      shifts.push(i)
    end
  end
  shifts
end

