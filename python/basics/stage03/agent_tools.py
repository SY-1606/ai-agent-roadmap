
def search_tool(query):
    """模拟搜索工具。"""
    return f"模拟搜索结果：{query}"


def calculator_tool(a, b):
    """模拟计算器工具。"""
    return a + b


def weather_tool(city):
    """模拟天气工具，不进行真实联网。"""
    return f"{city}天气功能暂未接入"


tools = {
    "search": search_tool,
    "calculator": calculator_tool,
    "weather": weather_tool,
}


def main():
    print("===== Agent Tool Simulator =====")
    print("可选工具：search / calculator / weather")

    tool_name = input("选择工具：").strip().lower()
    tool_function = tools.get(tool_name)

    if tool_function is None:
        print("工具不存在")
        return

    if tool_name == "search":
        query = input("请输入搜索内容：")
        result = tool_function(query)

    elif tool_name == "calculator":
        a = float(input("第一个数字："))
        b = float(input("第二个数字："))
        result = tool_function(a, b)

    else:
        city = input("请输入城市：")
        result = tool_function(city)

    print("工具执行结果：", result)


if __name__ == "__main__":
    main()
