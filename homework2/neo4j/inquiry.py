# result = tx.run("match (u:User)-[r:REVIEW]-(p:Product)-[b:Belong]-(m:Movie) "
#                 "where m.Movie=~\".*$message.*\""
#                 "return u,count(r) order by count(r) desc", message=message)
# mname = 'Tavener: Fall And Resurrection'

from py2neo import Graph

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="NEO4J"
)

mname = input("请输入要查询的关键词：")
print("结果是：")

data1 = graph.run(
    "match (u:User)-[r:REVIEW]-(p:Product)-[b:Belong]-(m:Movie) where m.Movie=~\".*" + mname + ".*\" return u,count(r) order by count(r) desc"
)
maxCount = 0
data = data1.data()
result = set()
for item in data:
    if item['count(r)'] >= maxCount:
        maxCount = item['count(r)']
        result.add(item['u'])
        print(item['u'])
    else:
        break
