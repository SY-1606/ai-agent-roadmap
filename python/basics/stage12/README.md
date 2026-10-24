# Stage 12 — Git and GitHub Fundamentals

第十二关：Git 版本控制与 GitHub 协作。

## 学习目标

理解 Git 的核心工作原理，并熟练使用分支、提交、合并和 Pull Request。

## 学习内容

- Git / GitHub
- Repository / .git
- Working Directory
- Staging Area
- Commit / HEAD
- Branch / Merge
- Merge Conflict
- Remote / origin
- Fetch / Pull / Push
- Pull Request / Code Review
- .gitignore
- README / Issues / Actions

## Git 工作流

```text
修改代码
    ↓
git status
    ↓
git diff
    ↓
git add
    ↓
git diff --staged
    ↓
git commit
    ↓
git push
    ↓
Pull Request
    ↓
Merge main
```

## 实战练习

1. 初始化独立 Git 实验仓库。
2. 创建和修改文件。
3. 完成两次提交。
4. 查看 Git 历史和差异。
5. 创建并合并功能分支。
6. 练习取消暂存。
7. 练习丢弃未提交修改。
8. 练习处理一次合并冲突。
9. 检查真实项目的 .gitignore。
10. 创建并合并 Stage 12 Pull Request。

实验仓库位于 `~/git-practice-stage12`，不放进 ai-agent-roadmap 内，以避免嵌套 Git 仓库。

## 注意事项

- 不提交 .env、密码和 API Key。
- 不随意执行 git reset --hard。
- 不随意对共享的 main 分支使用 force push。
- 提交前检查 git diff --staged。
- 应用型 uv 项目通常应提交 pyproject.toml 与 uv.lock。

## 学习成果

能够独立完成：

```text
创建分支 → 开发 → 暂存 → 提交 → 推送 → PR → 合并 → 同步 main
```

并能够理解常见 Git 错误、分支差异和基础冲突处理。