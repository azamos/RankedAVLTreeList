#username - amoszohar
#id1      - 311402812
#name1    - amos zohar
#id2      - complete info
#name2    - complete info  

from random import randrange

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1 # Balance factor
		self.key = 0 # Rank
		self.size = 1
		self.real = True

	def setAsVirtual(self):
		self.real = False
		self.size = 0
		self.left = None
		self.right = None

	def getRank(self):
		return self.key

	def getSize(self):
		return self.size

	def setRank(self,r):
		self.key = r

	def setSize(self,s):
		self.size = s

		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.real

	def makeLeaf(self):
		leftVirtualSon = AVLNode(None)
		rightVirtualSon = AVLNode(None)
		leftVirtualSon.setAsVirtual()
		rightVirtualSon.setAsVirtual()
		self.setLeft(leftVirtualSon)
		self.setRight(rightVirtualSon)
		leftVirtualSon.setParent(self)
		rightVirtualSon.setParent(self)

	def getBalanceFactor(self):
		return self.left.getHeight() - self.right.getHeight()

	def isLeftSon(self):
		return self.parent.left is self



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		# add your fields here
		self.minimum = None
		self.maximum = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.root is None

	def updateRanksInPathRec(self,node):
		if node is self.root:
			return node.getLeft().getSize()
		if node.isLeftSon():
			newRank = self.updateRanksInPathRec(node.getParent())-1-node.getRight().getSize()
		else:
			newRank = node.getParent().getRank()+1+node.getLeft().getSize()
		return newRank

	def defUpdateRanksinPath(self,i):
		self.root.setRank(self.root.getRank()+1)
		p = self.root.getRight() if self.root.getRank() > i else self.root
		while p.isRealNode():
			parentRank = p.getParent().getRank()
			if p.isLeftChild():
				p.setRank(p.getRank()-1-p.getRight().size)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return self.internalReachNode(i).getValue()


	def internalReachNode(self,i):
		p = self.root
		while not p.getRank() == i:
			if p.getRank() == i:
				return p
			elif p.getRank() > i:
				p = p.getLeft()
			elif p.getRank() < i:
				p = p.getRight()
		return p

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def rotateLeft(self, criminalNode):
		rightSonOfCriminal = criminalNode.right
		newRightSonOfProblemNode = rightSonOfCriminal.left
		parent = criminalNode.parent
		if criminalNode is parent.right:
			parent.right = rightSonOfCriminal
		elif criminalNode is parent.left:
			parent.left = rightSonOfCriminal
		criminalNode.parent = rightSonOfCriminal
		rightSonOfCriminal.parent = parent
		newRightOfCriminal = rightSonOfCriminal.left
		rightSonOfCriminal.left = criminalNode
		criminalNode.right = newRightOfCriminal

	def rotateRight(self, criminalNode):
		leftSonOfCriminal = criminalNode.left
		newLeftSonOfProblemNode = leftSonOfCriminal.right
		parent = criminalNode.parent
		if criminalNode is parent.right:
			parent.right = leftSonOfCriminal
		elif criminalNode is parent.left:
			parent.left = leftSonOfCriminal
		criminalNode.parent = leftSonOfCriminal
		leftSonOfCriminal.parent = parent
		newLeftOfCriminal = leftSonOfCriminal.right
		leftSonOfCriminal.right = criminalNode
		criminalNode.left = newLeftOfCriminal

	#TODO: finish this
	def determineOperationAndExecute(self,criminalNode):
		counter = 0;
		bf = criminalNode.getBalanceFactor()
		if bf == -2:
			rightChildBalanceFactor = criminalNode.getRight().getBalanceFactor()
			if rightChildBalanceFactor == 1:
				self.rotateRight(criminalNode)
				counter += 1
			self.rotateLeft(criminalNode)
		if bf == 2:
			leftChildBalanceFactor = criminalNode.getRight().getBalanceFactor()
			if leftChildBalanceFactor == -1:
				self.rotateLeft(criminalNode)
				counter+=1
			self.rotateRight(criminalNode)
		counter += 1
		return counter

	def rebalanceTree(self, leaf):
		rebalances = 0
		p = leaf
		while not p is None:
			if abs(p.getBalanceFactor())>1:
				rebalances += self.determineOperationAndExecute(p)
			p = p.getParent()
		return rebalances

	def rotateLeft(self):
		return

	def rotateRight(self):
		return

	def insert(self, i, val):
		rotationsCounter = 0

		newNode = AVLNode(val)
		newNode.setRank(i)
		newNode.makeLeaf()
		if self.empty():
			self.root = newNode
			self.size = 1
			self.maximum = newNode
			self.minimum = newNode
			return rotationsCounter

		oldArrI = self.internalReachNode(i)#Needs to be reinserted later
		rotationsCounter += self.delete(i)

		# insertionPoint = self.internalReachInsertionPoint(i)
		# if insertionPoint.getRank() < i:
		# 	insertionPoint.setRight(newNode)
		# elif insertionPoint.getRank() > i:
		# 	insertionPoint.setLeft(newNode)
		# newNode.setParent(insertionPoint)
		#newNode is a leaf now with rank=key=i.Need to check if Rebalances are needed
		# rotationsCounter += self.rebalanceTree(newNode)
		# if i == 0:
		# 	self.minimum = newNode
		# if i == self.size-1:
		# 	self.maximum = newNode
		# return rotationsCounter
		rotationsCounter += self.attachNode(newNode)
		oldArrI.setRank(i+1)
		rotationsCounter += self.attachNode(oldArrI)
		return rotationsCounter

	def attachNode(self,node):
		i = node.getRank
		node.setRank(i)
		insertionPoint = self.internalReachInsertionPoint(i)
		if i > insertionPoint.getRank():
			insertionPoint.setRight(node)
		elif i < insertionPoint.getRank():
			insertionPoint.setLeft(node)
		node.setParent(insertionPoint)
		rotationsCounter = 0
		rotationsCounter += self.rebalanceTree(node)
		if i == 0:
			self.minimum = node
		if i == self.size - 1:
			self.maximum = node
		return rotationsCounter


	def internalReachInsertionPoint(self,i):
		p = self.root
		while p.isRealNode():
			if p.getRank() < i:
				p = p.getRight()
			else:
				p=p.getLeft()
		return p.getParent()


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		if self.empty():
			return 0

		rotationsCounter = 0
		p = self.root
		while p.isRealNode():
			if p.getRank()==i:
				break
			if p.getRank() > i:
				p = p.getLeft()
			elif p.getRank() < i :
				p = p.getRight()
		if p is self.root:
			l = p.getLeft()
			r = p.getRight()
			if l.getHeight() > r.getHeight():
				l.setParent(None)
				self.root.setAsVirtual()
				self.root = l
				baggage = l.getRight()
				l.setRight(r)
				r.setParent(l)
				self.minInSubTree(r).setLeft(baggage)
				self.rebalanceTree(self.first())
			else:
				r.setParent(None)
				self.root.setAsVirtual()
				self.root = r
				baggage = r.getLeft()
				attachPoint = self.minInSubTree(r)
				attachPoint.setLeft(l)
				l.setParent(attachPoint)
				self.rebalanceTree(self.first())





		return rotationsCounter
	def minInSubTree(self, node):
		p = node
		while p.isRealNode():
			p = p.getLeft()
		return p


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.minimum

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.maximum

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		arr = [""]*self.size
		p = self.minimum
		while (not p is None) and p.isRealNode():
			arr[p.getRank()] = str(p.getValue())
			p = self.successor(p)
		return arr


	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		sortedArr = self.quickSort(self.listToArray())
		sortedAVLlist = AVLTreeList()
		n = len(sortedArr)
		for i in range(n):
			sortedAVLlist.insert(sortedArr[i])

	def quickSort(self,arr):
		pIndex = randrange(0,arr.size())
		pivot = arr[pIndex]
		smallerElements = []
		equalElemens = []
		biggerElements = []
		for info in arr:
			if info < pivot:
				smallerElements.append(info)
			elif info == pivot:
				equalElemens.append(info)
			elif info > pivot:
				biggerElements.append(info)
		return self.quickSort(smallerElements) + equalElemens + self.quickSort(biggerElements)

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		arr = self.listToArray()
		n = len(arr)
		permutatonTheta = AVLTreeList()
		wasAllreadyRolled = [False] * n
		i = 0
		while i < n:
			randRes = randrange(n)
			if wasAllreadyRolled[randRes] == False:
				permutatonTheta.insert(0,arr[randRes])
				wasAllreadyRolled[randRes] = True
				i += 1
		return permutatonTheta

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		leftTree = self
		rightTree = lst
		x = rightTree.first()
		pointerTree2 = x.getParent()
		x.setParent(None)
		virtSon = AVLNode(None)
		virtSon.setAsVirtual()
		pointerTree2.setLeft(virtSon)
		delta = rightTree.size - leftTree.size
		if delta > 0:
			x.setLeft(leftTree.root)
			while pointerTree2.getHeight() > leftTree.root.getHeight():
				pointerTree2 = pointerTree2.getParent()
			x.setParent(pointerTree2.getParent())
			pointerTree2.getParent().setLeft(x)
			pointerTree2.setParent(x)
			self.rebalanceTree(x)
		if delta == 0:
			x.setLeft(leftTree.root)
			x.setRight(rightTree.root)
			leftTree.setParent(x)
			rightTree.setParent(x)
		if delta < 0:
			x=5



		return abs(delta)

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		p = self.minimum
		while p.isRealNode():
			if p.getValue() == val:
				return p.getRank()-1
			p = self.successor(p)
		return -1



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root

	def successor(self, node):
		p = node
		if not node.getRight().isRealNode():
			while not p.getParent() is None:
				if p.isLeftSon():
					return p
				p = p.getParent()
		else:
			p = p.getRight()
			while p.isRealNode():
				p = p.getLeft()
			return p.getParent()



L = AVLTreeList()
L.insert(0,34)
L.insert(1,15)
L.insert(2,12)
print(L.retrieve(0))