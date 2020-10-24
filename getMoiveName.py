import csv

csvFile = open("productName.csv", 'r')
reader = csv.reader(csvFile)

result = {}

# key word to delete   [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP]
# 除了一些括号表示特别收藏版之类的，括号里面还有其他语言翻译的名字，可以认为是另一个版本的电影，收到各个国家的政策影响，认为不同语言版本也是不同的电影
# Remastered 重制版认为是新的电影
# 引号也要删掉"" ''
# 另外，不同的vol也认为是不同的movie
