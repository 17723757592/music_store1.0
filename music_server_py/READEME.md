联合类型； Union[X, Y] 等价于 X | Y ，意味着满足 X 或 Y 之一。`

xxx.title:用于将首字符大写


is：比较两个对象是否指向同一存储单元
==：判断值或内容是否相等
in：在指定的序列（列表、范围、字符串等）中找到值，返回True，否则返回False。

查询参数:
声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数


使用Query为变量添加约束，默认值等
第一个参数是默认值，...表示是必须的
pattern:添加正则表达式
alias="item-query",为变量添加别名

    gt：大于（greater than）
    ge：大于等于（greater than or equal）
    lt：小于（less than）
    le：小于等于（less than or equal）


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
//async def read_items(q: Union[List[str], None] = Query(default=None)):
//可以通过这样的方式接收多个值
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


如果有两个及其以上pydantic参数模型，FastAPI 将注意到该函数中有多个请求体参数（两个 Pydantic 模型参数）。
因此，它将使用参数名称作为请求体中的键（字段名称），并期望一个类似于以下内容的请求体：

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
而如果只有一个pydantic 期待一个具有Item的属性的JSON请求体：
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}

而只有一个pydantic模型同时期待拥有 item 键并在值中包含模型内容的 JSON的请求体可以这样：
async def update_item(item: Annotated[Item, Body(embed=True)]):
    return

xxx.updata()


依赖
commons: CommonQueryParams(这里通常可以添加dict等类型) = Depends(CommonQueryParams)
FastAPI 对此做了简化，你可以写成：
commons=Depends(CommonQueryParams) 或 commons: CommonQueryParams = Depends()

callable:可调用的

sqlalchemy 查询 
    query.filter() 过滤query.filter_by() 根据关键字过滤query.all() 返回列表query.first() 返回第一个元素query.one() 有且只有一个元素时才正确返回 
    query.one_or_none()，类似one，但如果没有找到结果，则不会引发错误 query.scalar()，调用one方法，并在成功时返回行的第一列
    query.count() 计数query.order_by() 排序


前单下划线：
下划线前缀的含义是告知其他程序员：以单个下划线开头的变量或方法仅供内部使用

单末尾下划线 var_：
单个末尾下划线（后缀）是一个约定，用来避免与Python关键字产生命名冲突，比如：class_

双前导下划线 __var:Python解释器所做的名称修饰。 它这样做是为了防止变量在子类中被重写。
class Test:
   def __init__(self):
       self.foo = 11
       self._bar = 23
       self.__baz = 2

t = Test()
>>>t._Test__baz
2

双前导和双末尾下划线 _var_:
不会应用名称修饰。 由双下划线前缀和后缀包围的变量不会被Python解释器修改：

单下划线 _
有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的。
除了用作临时变量之外，"_"是大多数Python REPL中的一个特殊变量，它表示由解释器评估的最近一个表达式的结果