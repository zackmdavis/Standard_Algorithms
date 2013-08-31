class MaxHeap
  def initialize(data)
    @data = data
    @heap_size = data.length
    (@heap_size/2).downto(1) do |i|
      max_heapify(i)
    end
  end

  def at(i)
    @data[i-1]
  end

  def parent(i)
    i/2
  end

  def left(i)
    2*i
  end

  def right(i)
    2*i + 1
  end

  def max_heapify(i)
    l = left(i)
    r = right(i)
    if l <= @heap_size and at(l) > at(i)
      largest = l
    else
      largest = i
    end
    if r <= @heap_size and at(r) > at(largest)
      largest = r
    end
    if largest != i
      ati = at(i)
      atl = at(largest)
      @data[i-1] = atl
      @data[largest-1] = ati
      max_heapify(largest)
    end
  end

  def maximum
    at(1)
  end

  def extract_max
    if @heap_size < 1
      return :underflow_error
    end
    max = at(1)
    @data[0] = at(@heap_size)
    @heap_size -= 1
    max_heapify(1)
    max
  end
end

def heapsort(data)
  heap = MaxHeap.new(data)
  data.length.downto(1) do |i|
    data[i-1] = heap.extract_max
  end
  data
end
