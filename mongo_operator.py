import pymongo

host = "localhost"  # 服务器主机名
port = 27017  # 端口号
username = "admin"  # 您的用户名
password = "admin"  # 您的密码
auth_source = "admin"

# 连接到 MongoDB 服务器
client = pymongo.MongoClient(host=host, port=port, username=username, password=password, authSource=auth_source)


def mongo_client():
    return client


# 指定要使用的数据库
db = client["mydatabase"]

# 选择要插入数据的集合（类似于关系型数据库中的表）
collection = db["mycollection"]

# 插入单个文档
data = {"name": "John", "age": 30}
inserted_doc = collection.insert_one(data)

# 插入多个文档
data_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
inserted_docs = collection.insert_many(data_list)

# 查询单个文档
query = {"name": "John"}
result = collection.find_one(query)

# 查询多个文档
query = {"age": {"$gte": 30}}  # 查询年龄大于等于30的文档
results = collection.find(query)

# 遍历结果
for doc in results:
    print(doc)

# 删除单个文档
query = {"name": "John"}
collection.delete_one(query)

# 删除多个文档
query = {"age": {"$gte": 40}}  # 查询年龄大于等于40的文档
collection.delete_many(query)

# 插入操作后，inserted_doc 和 inserted_docs 可以用来获取插入文档的信息
