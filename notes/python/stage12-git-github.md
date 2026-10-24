# Python 第十二关：Git、GitHub 与真实项目版本管理

## 1. 学习目标

理解 Git 的版本管理原理，掌握日常项目开发的完整 Git 工作流。

核心知识点：

- Git 与 GitHub
- Repository 和 .git
- Working Directory
- Staging Area
- Commit 与 HEAD
- Branch 与 Merge
- Merge Conflict
- Remote 与 origin
- Push、Pull、Fetch、Clone
- Pull Request、Code Review
- .gitignore
- git diff 与 git log
- git restore、git revert
- README、Issues、Actions、CI

## 2. Git 是什么？

Git 全称 Version Control System（版本控制系统）中的一种具体工具。

它负责记录文件修改历史、管理分支、比较版本以及合并代码。

Git 可以完全在本地运行，不依赖 GitHub。

## 3. Git 与 GitHub 的区别

| Git | GitHub |
|---|---|
| 本地版本控制工具 | 在线仓库托管与协作平台 |
| 管理提交历史 | 托管远程 Git 仓库 |
| 创建和合并分支 | 提供 Pull Request |
| 比较和恢复版本 | 支持 Code Review、Issues、Actions |

Git 不等于 GitHub。

## 4. Repository 仓库

Repository，简称 Repo。

Git 仓库通常包含一个用于保存内部数据的 `.git` 目录。

```text
project/
├── .git/
├── README.md
└── main.py
```

`.git/` 包含版本历史、对象、引用和仓库配置等信息。

不要随意删除 `.git/`。

## 5. 检查 Git

```bash
git --version
git config --global user.name
git config --global user.email
```

`--global` 表示用户级配置，可以影响当前用户的多个 Git 仓库。

如果需要设置：

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

提交邮箱可以使用 GitHub 提供的 noreply 邮箱。

## 6. Git 的三个重要区域

```text
Working Directory
工作区
    ↓ git add
Staging Area
暂存区
    ↓ git commit
Local Repository
本地仓库
```

### Working Directory

你正在编辑的实际文件。

### Staging Area

保存下一次提交准备包含的文件内容。

### Local Repository

保存已经创建的 Git 提交历史。

## 7. git status

```bash
git status
```

用于查看：

- 当前分支
- 未追踪文件
- 未暂存的修改
- 已暂存的修改
- 与远程跟踪分支的关系

遇到 Git 问题，优先查看 `git status`。

## 8. git add

```bash
git add main.py
```

将指定文件修改加入暂存区。

```bash
git add .
```

暂存当前目录范围内的文件变化。

注意：git add 只暂存，不创建提交。

操作前应检查 .gitignore 和文件内容，避免暂存敏感数据。

## 9. git commit

```bash
git commit -m "feat: add task API"
```

创建本地提交。

- `-m`：message，提交说明
- `feat`：功能新增
- `fix`：Bug 修复
- `refactor`：重构
- `docs`：文档
- `test`：测试
- `chore`：维护或配置

建议一个 commit 尽量围绕一个清晰的修改意图。

## 10. git log

```bash
git log --oneline
```

显示简洁提交历史。

输出中的短字符串是 Commit Hash 的缩写。

可以使用：

```bash
git show HEAD
```

查看当前提交的具体内容。

## 11. git diff

```bash
git diff
```

默认比较工作区与暂存区的差异。

```bash
git diff --staged
```

比较暂存区与当前提交的差异。

建议提交前检查：

```text
git status
    ↓
git diff
    ↓
git add
    ↓
git diff --staged
    ↓
git commit
```

## 12. HEAD

HEAD 表示 Git 当前检出的位置。

通常它指向当前分支，而分支指向最近一次提交。

例如：

```text
HEAD
 ↓
main
 ↓
Commit C
```

## 13. Branch 分支

Branch 是 Git 中指向某次提交的可移动引用。

可以把它理解成一条开发线。

常见分支：

```text
main
feature/task-search
feature/chat
fix/task-validation
```

查看分支：

```bash
git branch
```

创建并切换：

```bash
git switch -c feature/demo
```

切换到已有分支：

```bash
git switch main
```

## 14. Merge 合并

把一个分支上的修改整合到当前分支。

```bash
git switch main
git merge feature/demo
```

实际项目通常使用 GitHub PR 审查后再合并。

## 15. Merge Conflict

合并冲突是指 Git 无法安全地自动整合某些修改。

冲突标记可能是：

```text
<<<<<<< HEAD
main 分支内容
=======
feature 分支内容
>>>>>>> feature/demo
```

处理方式：

1. 人工阅读双方内容
2. 决定最终保留什么
3. 删除冲突标记
4. 暂存解决后的文件
5. 完成合并

冲突不代表 Git 损坏。

## 16. Remote 远程仓库

远程仓库是本地 Git 仓库引用的其他仓库。

```bash
git remote -v
```

可以查看远程名称和地址。

`origin` 是主要远程仓库的惯用名称，不是 GitHub 的特殊关键字。

## 17. Push 推送

```bash
git push -u origin feature/demo
```

用于将本地分支的提交推送到远程仓库。

其中：

- push：推送
- -u：设置上游跟踪关系
- origin：远程名称
- feature/demo：本地分支

## 18. Fetch 与 Pull

```bash
git fetch origin
```

获取远程更新，但不自动合并到当前分支。

```bash
git pull --ff-only origin main
```

获取更新，并在可以快进合并时更新当前分支。

`--ff-only` 表示仅允许快进更新，不能快进时中止。

## 19. Clone

```bash
git clone 仓库地址
```

用于克隆已有 Git 仓库，包括版本历史及相关远程配置。

与下载 ZIP 不同，clone 后可以继续进行 Git 版本管理。

## 20. Pull Request

Pull Request，简称 PR。

它是 GitHub 上提出分支合并请求的协作功能。

常见流程：

```text
feature branch
    ↓
push
    ↓
Pull Request
    ↓
Code Review
    ↓
Merge
    ↓
main
```

## 21. Code Review

代码审查通常检查：

- 逻辑是否正确
- 是否存在 Bug
- 命名和结构是否清楚
- 安全性
- 测试是否充分
- 是否存在无关修改

## 22. .gitignore

.gitignore 用于告诉 Git 忽略符合规则的未追踪文件。

常见配置：

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/

.env
.env.*
!.env.example

.DS_Store
```

注意：

- 已被 Git 追踪的文件不会因为加入 .gitignore 而自动停止追踪。
- .env.example 可以提交，但不能包含真实密码。
- pyproject.toml 和应用项目的 uv.lock 通常应该提交。

## 23. 敏感信息安全

绝对不要上传：

- 数据库密码
- API Key
- Access Token
- SSH 私钥
- 其他真实凭证

如果凭证已经进入公开 Git 历史，应立即轮换或撤销相关凭证。

仅删除文件、补充 .gitignore 不能消除历史泄露。

## 24. git restore

丢弃指定文件未暂存的工作区修改：

```bash
git restore file.txt
```

此操作可能造成未提交修改永久丢失。

取消暂存，但保留工作区修改：

```bash
git restore --staged file.txt
```

## 25. git revert

```bash
git revert 提交哈希
```

通过创建新的反向修改提交，撤销旧提交的效果。

适合处理已共享历史中的普通错误修改。

## 26. git reset 和 force push

git reset 可以移动提交引用，并根据模式影响暂存区和工作区。

git push --force 可以强制重写远程分支历史。

这两类操作具有风险，当前阶段不建议对已共享的 main 分支使用。

## 27. README

README.md 是项目说明文档。

一个完善的项目 README 通常包含：

- 项目简介
- 技术栈
- 主要功能
- 目录结构
- 安装说明
- 环境变量配置
- 启动方式
- API 文档
- 测试方法
- 项目截图
- 后续计划

## 28. GitHub Issues

Issue 可以记录 Bug、功能请求或任务计划。

例如：

```text
Add task search
Fix invalid priority validation
```

## 29. GitHub Actions 与 CI

GitHub Actions 是 GitHub 的自动化工作流平台。

CI 全称 Continuous Integration（持续集成）。

例如：

```text
push
  ↓
GitHub Actions
  ↓
pytest
  ↓
检查结果
```

后续学习测试和部署时可以使用。

## 30. 当前项目建议工作流

```text
main 保持稳定
    ↓
创建 feature 分支
    ↓
修改代码
    ↓
git status
    ↓
git diff
    ↓
git add 指定文件
    ↓
git diff --staged
    ↓
git commit
    ↓
git push
    ↓
GitHub Pull Request
    ↓
Merge main
    ↓
本地同步 main
```

## 31. 常见问题

**Q1：git add 之后已经提交了吗？**

没有，git add 只是暂存。

**Q2：Git 和 GitHub 相同吗？**

不相同。Git 是版本控制工具，GitHub 是远程托管和协作平台。

**Q3：git fetch 和 git pull 区别？**

fetch 获取更新；pull 获取并尝试整合到当前分支。

**Q4：git restore --staged 会删除代码吗？**

不会，它只取消暂存。

**Q5：为什么不随便执行 git push --force？**

可能覆盖或改写他人已经依赖的远程历史。

**Q6：GitHub push 失败一定是 Git 出错吗？**

不一定，可能是远程地址、认证、网络或代理问题。

## 32. 本关验收

- [ ] 理解 Git 三个区域
- [ ] 会查看 status 和 diff
- [ ] 会 add 和 commit
- [ ] 会 log 和 show
- [ ] 会创建、切换、合并分支
- [ ] 了解冲突处理
- [ ] 会安全取消暂存
- [ ] 了解 restore 和 revert
- [ ] 会检查 remote
- [ ] 会 push、fetch、pull
- [ ] 理解 GitHub PR
- [ ] 不提交敏感文件
- [ ] 更新 README
- [ ] 完成 GitHub PR 合并

## 33. 核心总结

最重要的 Git 操作习惯：

```text
修改
→ status
→ diff
→ add
→ diff --staged
→ commit
→ push
→ PR
```

Git 管理版本历史，GitHub 管理远程协作。二者结合可以使 Python 项目具备可追踪、可维护、可审查的开发历史。