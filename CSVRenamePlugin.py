class CSVRenamePlugin:
   def input(self, filename):
      self.parameters = dict()
      filestuff = open(filename, 'r')
      for myline in filestuff:
         line = myline.strip()
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1]

   def run(self):
      replace = self.parameters["replace"]
      file1 = open(self.parameters["file1"], 'r')
      file2 = open(self.parameters["file2"], 'r')
      self.contents = []
      i = 0
      for myline in file1:
         line = myline.strip()
         data = line.split(',')
         self.contents.append(data)

      replacementcontents = []
      file2.readline()
      for myline in file2:
         line = myline.strip()
         stuff = line.split(',')
         replacementcontents.append(stuff[1])

      if (replace == "columns"):
         for column in range(1, len(self.contents[0])):
            self.contents[0][column] = replacementcontents[column-1]
      else:
         for row in range(1, len(self.contents)):
            self.contents[row][0] = replacementcontents[row-1]

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(len(self.contents)):
         for j in range(len(self.contents[i])):
            filestuff2.write(self.contents[i][j])
            if (j == len(self.contents[i])-1):
               filestuff2.write('\n')
            else:
               filestuff2.write(',')



