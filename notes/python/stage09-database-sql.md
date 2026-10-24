# Python 第九关：数据库、SQL、SQLite 与 FastAPI

## 1. 学习目标

从零掌握关系型数据库的核心概念，使用 Python 自带的 sqlite3 模块操作 SQLite，并实现 FastAPI + SQLite 数据持久化。

主要知识点：

- Database / DBMS
- SQLite、PostgreSQL、MySQL
- Table、Row、Column
- Primary Key、Foreign Key
- SQL 和 CRUD
- CREATE TABLE
- SELECT、INSERT、UPDATE、DELETE
- WHERE、ORDER BY、LIMIT、OFFSET
- commit 和事务
- sqlite3.Row
- 参数化 SQL 与 SQL 注入
- 数据库约束和表之间的关系

## 2. 数据库是什么？

Database（数据库）是按照一定结构组织、存储的数据集合。

DBMS（Database Management System，数据库管理系统）是管理这些数据的软件。

常见数据库系统：

| 名称 | 主要特点 |
|---|---|
| SQLite | 轻量、嵌入式、通常使用单个数据库文件 |
| PostgreSQL | 功能丰富的关系型数据库服务器 |
| MySQL | 广泛使用的关系型数据库服务器 |

当前先使用 SQLite，后续学习 PostgreSQL。

## 3. 为什么不能一直使用 JSON？

JSON 文件适合少量数据的保存和交换。

随着数据规模与并发操作增加，可能出现：

- 查询需要自己遍历大量数据
- 多条件筛选复杂
- 修改、保存管理困难
- 多个程序同时写入需要自己协调
- 缺少数据库所提供的事务与约束等功能

数据库可以提供专门的数据查询、事务和约束管理能力。

## 4. 关系型数据库

关系型数据库（Relational Database）主要通过表（Table）组织数据。

例如任务表：

| id | title | priority | done |
|---|---|---|---|
| 1 | 学习Python | high | 0 |
| 2 | 学习FastAPI | medium | 1 |
| 3 | 学习SQL | high | 0 |

- Table：表，一类记录的集合
- Row：行，一条具体记录
- Column：列，一种数据属性

## 5. 主键 Primary Key

主键用于唯一标识表中的每条记录。

例如：

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

这里 id 作为主键，由 SQLite 自动生成。

主键应具有唯一性，不能用容易重复的任务标题充当主键。

## 6. SQL 是什么？

SQL 全称 Structured Query Language，结构化查询语言。

用于定义、查询和修改关系型数据库数据。

最重要的 CRUD 对应关系：

| CRUD | SQL |
|---|---|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

## 7. 创建表 CREATE TABLE

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    priority TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
);
```

逐项解释：

- CREATE TABLE：创建表
- IF NOT EXISTS：不存在时才创建
- INTEGER：整数类型
- TEXT：文本类型
- PRIMARY KEY：主键
- AUTOINCREMENT：自动分配递增的行 ID
- NOT NULL：不允许 NULL
- DEFAULT 0：默认值为 0

SQLite 中经常用整数 0/1 保存布尔状态。

## 8. 插入 INSERT

```sql
INSERT INTO tasks (title, priority, done)
VALUES ('学习SQL', 'high', 0);
```

表示新增一条任务记录。

在 Python 中不要直接把用户输入拼进 SQL 字符串，应使用参数绑定。

```python
cursor.execute(
    "INSERT INTO tasks (title, priority, done) VALUES (?, ?, ?)",
    ("学习SQL", "high", 0)
)
```

`?` 是参数占位符。

## 9. 查询 SELECT

查询全部：

```sql
SELECT * FROM tasks;
```

查询指定列：

```sql
SELECT id, title FROM tasks;
```

`*` 表示选取所有列。

## 10. WHERE 筛选条件

```sql
SELECT * FROM tasks
WHERE done = 0;
```

只查询未完成任务。

多条件：

```sql
SELECT * FROM tasks
WHERE priority = 'high'
AND done = 0;
```

## 11. ORDER BY 排序

```sql
SELECT * FROM tasks
ORDER BY id ASC;
```

- ASC：升序
- DESC：降序

例如：

```sql
SELECT * FROM tasks
ORDER BY id DESC;
```

按 ID 从大到小排序。

## 12. LIMIT 与 OFFSET

```sql
SELECT * FROM tasks
ORDER BY id DESC
LIMIT 20 OFFSET 0;
```

- LIMIT 20：最多取 20 条
- OFFSET 0：跳过前 0 条

第二页：

```sql
LIMIT 20 OFFSET 20;
```

分页最好配合明确的 ORDER BY，避免结果顺序不稳定。

## 13. UPDATE 修改

```sql
UPDATE tasks
SET done = 1
WHERE id = 1;
```

只修改 id 为 1 的任务。

注意：如果删除 WHERE 条件，可能会修改表中所有行。

## 14. DELETE 删除

```sql
DELETE FROM tasks
WHERE id = 1;
```

删除指定任务。

危险写法：

```sql
DELETE FROM tasks;
```

它会删除整张表的所有记录，但不会删除表结构。

## 15. SQLite 与 Python

Python 自带 sqlite3 模块，不需要额外安装 SQLite Python 驱动。

```python
import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()

connection.close()
```

- connect：创建数据库连接
- cursor：创建执行 SQL 的游标
- execute：执行 SQL
- fetchall：获取剩余查询结果
- fetchone：获取一条查询结果
- close：关闭连接

## 16. sqlite3.Row

默认查询结果通常以元组形式表示。

例如：

```python
(1, "学习SQL", "high", 0)
```

如果设置：

```python
connection.row_factory = sqlite3.Row
```

查询出的每一行可使用列名访问：

```python
row["title"]
```

也可以转换成字典：

```python
dict(row)
```

更适合后续向 FastAPI 返回 JSON。

## 17. commit 与事务

修改数据后通常需要提交事务：

```python
connection.commit()
```

commit 表示提交事务，使修改持久保存。

如果操作失败，事务可以回滚：

```python
connection.rollback()
```

Transaction（事务）可以将多次数据库修改作为一个整体管理。

## 18. 参数化查询与 SQL 注入

错误写法：

```python
sql = f"SELECT * FROM tasks WHERE title = '{title}'"
```

用户输入可能改变 SQL 结构，产生 SQL 注入风险。

正确写法：

```python
cursor.execute(
    "SELECT * FROM tasks WHERE title = ?",
    (title,)
)
```

`(title,)` 是只含一个元素的元组。

参数绑定也可以正确处理引号和特殊字符。

注意：参数占位符用于数据值，不能直接代替表名或列名。

## 19. lastrowid 与 rowcount

```python
cursor.lastrowid
```

可取得最近一次插入行的 ID。

```python
cursor.rowcount
```

对于 UPDATE / DELETE 等操作，可用于检查受影响行数。

## 20. 常见约束 Constraint

| 约束 | 作用 |
|---|---|
| PRIMARY KEY | 唯一标识记录 |
| NOT NULL | 不允许 NULL |
| UNIQUE | 不允许出现重复值 |
| DEFAULT | 提供默认值 |
| CHECK | 检查字段值 |
| FOREIGN KEY | 关联其他表 |

## 21. 外键与表之间的关系

例如：

```text
users
id | name
1  | Tom
2  | Alice
```

```text
tasks
id | title | user_id
1  | 学习SQL | 1
2  | 学习Python | 1
```

tasks.user_id 可以引用 users.id。

这就是外键（Foreign Key）。

常见关系：

- One-to-One：一对一
- One-to-Many：一对多
- Many-to-Many：多对多

使用 SQLite 时，还需要注意外键约束的启用配置。

## 22. NULL 与空字符串

NULL 表示缺少值。

空字符串 `""` 是一个实际存在的字符串值，只是长度为 0。

两者不同。

## 23. SQL 常用统计函数

```sql
SELECT COUNT(*) FROM tasks;
```

计算总记录数量。

```sql
SELECT AVG(score) FROM students;
```

计算平均成绩。

```sql
SELECT MAX(score) FROM students;
```

查询最高成绩。

```sql
SELECT MIN(score) FROM students;
```

查询最低成绩。

## 24. LIKE 模糊匹配

```sql
SELECT * FROM tasks
WHERE title LIKE '%Python%';
```

`%` 表示任意长度的字符序列。

Python 参数化写法：

```python
cursor.execute(
    "SELECT * FROM tasks WHERE title LIKE ?",
    ("%Python%",)
)
```

## 25. Schema 与数据库迁移

Schema 是数据库的结构定义，包括表、列、数据类型与约束。

修改表结构可以使用：

```sql
ALTER TABLE tasks ADD COLUMN created_at TEXT;
```

以后正式项目会学习数据库迁移（Migration）。

## 26. ORM

ORM 全称 Object-Relational Mapping，对象关系映射。

它让数据库表、行与 Python 类和对象建立映射关系。

以后会学习 SQLAlchemy，但这一关先直接使用 SQL，理解数据库底层操作。

## 27. FastAPI + SQLite

以前的 API：

```python
tasks = []
```

任务存储在内存。

升级之后：

```text
HTTP Request
    ↓
FastAPI
    ↓
database.py
    ↓
SQLite tasks.db
    ↓
查询或修改记录
    ↓
返回 JSON Response
```

服务器重启后，数据库文件中的任务仍然存在。

## 28. 本关项目

- [ ] SQLite 创建数据库和表
- [ ] INSERT 插入数据
- [ ] SELECT 查询数据
- [ ] WHERE 条件筛选
- [ ] UPDATE 修改数据
- [ ] DELETE 删除数据
- [ ] ORDER BY / LIMIT / OFFSET
- [ ] sqlite3.Row
- [ ] 参数化 SQL 查询
- [ ] FastAPI + SQLite Task API
- [ ] 重启服务器后数据仍然存在
- [ ] PR 合并 main

## 29. 自测题

**Q1：数据库和 DBMS 有什么区别？**

数据库是组织好的数据集合，DBMS 是管理数据库的软件。

**Q2：什么是主键？**

唯一标识一条记录的字段或字段组合。

**Q3：INSERT 和 SELECT 的区别？**

INSERT 插入数据，SELECT 查询数据。

**Q4：为什么 UPDATE 和 DELETE 要注意 WHERE？**

因为没有 WHERE 可能会影响整张表的所有行。

**Q5：commit() 是什么？**

提交数据库事务。

**Q6：fetchone() 与 fetchall() 区别？**

前者取一条，后者获取剩余的全部结果。

**Q7：为什么使用 ? 占位符？**

避免把用户输入直接当成 SQL 语法的一部分，并正确绑定数据值。

**Q8：sqlite3.Row 有什么作用？**

让查询结果支持按列名访问，也方便转为字典。

**Q9：lastrowid 有什么作用？**

取得最近一次插入行的 ID。

**Q10：Foreign Key 是什么？**

一个表中用于引用其他表记录的字段或字段组合。

## 30. 验收标准

能够使用 SQLite 建表、增删改查，掌握条件查询、排序、分页和安全的参数化 SQL，并完成 FastAPI + SQLite 任务持久化项目。