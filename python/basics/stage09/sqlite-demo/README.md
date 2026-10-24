# SQLite Demo — Python Stage 09

Python sqlite3 数据库基础练习。

## 学习内容

- 创建 SQLite 数据库和表
- INSERT、SELECT、UPDATE、DELETE
- WHERE、ORDER BY、LIMIT、OFFSET
- 参数化 SQL
- sqlite3.Row
- commit 与事务

## 运行

```bash
uv run python main.py
```

程序会生成本地 `tasks.db`，并执行一轮数据库增删改查练习。

每次运行都会新插入三条任务，因此数据库中的记录数量会发生变化。