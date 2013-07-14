class Node
  attr_accessor :key
  attr_accessor :parent
  attr_accessor :left
  attr_accessor :right

  def initialize(k, p, l, r)
    @key = k
    @parent = p
    @left = l
    @right = r
  end

  def inspect
    print "key ", @key, "\n"
  end
end

class BinarySearchTree
  attr_accessor :root

  def initialize(r)
    @root = r
  end

  def inorder_walk(x)
    unless x.nil?
      inorder_walk(x.left)
      puts x.key
      inorder_walk(x.right)
    end
  end

  def insert(z)
    y = nil
    x = @root
    while not x.nil?
      y = x
      if z.key < x.key
        x = x.left
      else
        x = x.right
      end
    end
    z.parent = y
    if y.nil?
      @root = z # tree was empty
    elsif z.key < y.key
      y.left = z
    else
      y.right = z
    end
  end

  def transplant(u, v)
    if u.parent.nil?
      @root = v
    elsif u == u.parent.left
      u.parent.left = v
    else
      u.parent.right = v
    end
    unless v.nil?
      v.parent = u.parent
    end
  end

  def delete(z)
    if z.left.nil?
      transplant(z, z.right)
    elsif z.right.nil?
      transplant(z, z.left)
    else
      y = subtree_minimum(z.right)
      if y.parent != z
        transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      end
      transplant(z, y)
      y.left = z.left
      y.left.parent = y
    end
  end

  def search(k)
    searcher(@root, k)
  end

  def searcher(x, k)
    if x.nil? or k == x.key
      return x
    elsif k < x.key
      return searcher(x.left, k)
    else
      return searcher(x.right, k)
    end
  end

  def minimum
    subtree_minimum(@root)
  end

  def subtree_minimum(x)
    while not x.left.nil?
      x = x.left
    end
    x
  end

  def maximum
    subtree_maximum(@root)
  end

  def subtree_maximum(x)
    while not x.right.nil?
      x = x.right
    end
    x
  end

  def successor(x)
    unless x.right.nil?
      return subtree_minimum(x.right)
    end
    y = x.parent
    while !y.nil? and x == y.right
      x = y
      y = y.parent
    end
    y
  end
end
