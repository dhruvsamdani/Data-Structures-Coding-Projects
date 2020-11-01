import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = None
      self.prevBlock = None
      self.nextBlock = None


class BlockChain:
    def __init__(self):
        self.head = None
        self.lastBlock = None
        

    def __str__(self):
        returnList = []
        while self.head:
            returnList.append([self.head.data, self.head.timestamp, self.head.previous_hash,self.head.hash])
            self.head = self.head.nextBlock
        lst = ('\n'.join([str(item) for item in returnList]))
        return str(lst)

    def addBlock(self, value, timestamp):

      if value == None or timestamp == None:
        print("Uh Oh, Please enter a valid string")
        return

      if not isinstance(value, str) or not isinstance(timestamp, str):
        print("Uh Oh, Please enter a valid string")
        return

      block = Block(timestamp, value, None)

      if self.head == None:
          block.hash = calc_hash(value, timestamp,'0')
          self.head = block
          self.lastBlock = block
          self.head.nextBlock = self.lastBlock
          block.previous_hash = '0'
          block.prevBlock = None
      else:
          self.lastBlock.nextBlock = block
          block.previous_hash = self.lastBlock.hash
          block.hash = calc_hash(value, timestamp, block.previous_hash)
          
          block.prevBlock = self.lastBlock
          self.lastBlock = block



    
def calc_hash(s, ts, prevhash):
      sha = hashlib.sha256()
      encodedString = s+ts+prevhash
      hash_str = encodedString.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

bc = BlockChain()
bc.addBlock('Test', '1:35 05/31/2020')
bc.addBlock('Alligator', '8:42 05/31/2020')
bc.addBlock('Peach', '4:11 05/31/2020')
bc.addBlock('Apple', '6:29 05/31/2020')


# Expected Outcome
# ['Test', '1:35 05/31/2020', '0', '727854185aa279c7120ab01a68fa5e794440410c524158b33649fa15aff5e088']
# ['Alligator', '8:42 05/31/2020', '727854185aa279c7120ab01a68fa5e794440410c524158b33649fa15aff5e088', 'fda71383909b8d7d9fe07ea64c1effe9ee2368d7c534141cee2ee984c02b737c']
# ['Peach', '4:11 05/31/2020', 'fda71383909b8d7d9fe07ea64c1effe9ee2368d7c534141cee2ee984c02b737c', '603626124ed4500dc55d13d97eb0d32cb901156dc1c781598c21d098ebc0c60d']
# ['Apple', '6:29 05/31/2020', '603626124ed4500dc55d13d97eb0d32cb901156dc1c781598c21d098ebc0c60d', 'c4648a4889f4c9c9c2e219f041002ceebc234852b4dc2f994d6948edf751ad69']

blockchainTest1 = BlockChain()

blockchainTest1.addBlock(None, '6:29 05/31/2020') # Uh Oh, Please enter a valid string

blockchainTest2 = BlockChain()

blockchainTest1.addBlock((6,7), '6:29 05/31/2020') # Uh Oh, Please enter a valid string

print(bc)
