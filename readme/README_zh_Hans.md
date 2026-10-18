# Suno by Ace Data Cloud：Qwen Code 原生扩展

通过 Ace Data Cloud 生成 Suno 音乐，并查询同一任务的音频结果。 每个服务独立安装、独立输入凭据，复用现有托管 MCP；不会安装其它四项，也不会自动增加 LLM 服务商。

**当前为候选源码，未获 Qwen 官方收录、未默认内置。** 实现在 `codex/native-qwen-extension` 分支待人审；main 初始化 README 不是正式包。

[English](../README.md) · [注册/登录与应用列表](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_signup) · [当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_pricing)

## 1. 通过 Qwen 原生扩展命令安装

```bash
qwen extensions install AceDataCloud/SunoQwenCode --ref codex/native-qwen-extension
```

基线为 Qwen 0.25.2+、Node 22+。确认本地扩展安装摘要后，按提示输入自己的 Token。正式源码合并发布后才使用省略 `--ref` 的命令。也可按 [Ace 目录说明](https://github.com/AceDataCloud/AceDataCloudQwenCode) 添加来源，在 `/extensions manage` → Discover 搜 **Suno**。用户添加目录不代表 Qwen 默认市场收录。

## 2. 注册、进入 General application、复制或创建 Token

打开 [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_api_key) 并注册/登录。没有通用应用时先点 **Initialize General Application**；进入 **General application**，复制 API Key，或 **Manage Keys → Create** 创建名为 `Suno Qwen Code` 的独立 Key。

![复制 API Key / Manage Keys](../_assets/tutorial/get-api-key-en.png)

核对本服务权限、当前价格、余额、有效期和用量限制；若限制 Allowed APIs，需要包含选定操作用到的 `/suno/audios`, `/suno/tasks`。按需限制，不能把任务查询权限当成生成权限。只复制原始 Token，不含 Bearer 或引号；`platform-...` 管理 Token 不可替代。

![创建独立 Key](../_assets/tutorial/create-api-key-en.png)

以上为共用 Ace 应用页真实截图，来自 2026-10-07 固定 SunoDify 教程，2026-10-18 复用；Key 已遮盖，不代表你的账户权益。

## 3. 粘贴到本扩展的敏感设置

安装时在 **Ace Data Cloud API Token** 隐藏输入框中粘贴。凭据由 Qwen 的 keychain/加密文件后备存储管理；扩展 JSON 只保存变量名 `ACE_SUNO_API_TOKEN`。不把 Key 放到聊天、脚本参数或共享配置，也不执行 `qwen mcp add` 重复添加。

```bash
qwen extensions settings set suno-by-ace-data-cloud "Ace Data Cloud API Token"
```

上面命令用于后续轮换，Token 在隐藏提示框输入。重启已有会话后 `/mcp` 检查 `suno` 连接；连接不是业务成功。

![官方 Qwen 历史终端改编预览](../_assets/tutorial/qwen-provider-preview.png)

该图为 v0.18.2 官方终端截图于 2026-10-17 编辑，标的是另一个手动模型设置入口，**不是本扩展凭据框或 Ace 实测结果**；当前扩展设置真实截图已排队，不能用预览声称上线。

## 4. 首用与查询原任务

Qwen 的对话模型另行配置；模型对话本身可能收费。先查看工具定义，或调用仅列模型信息的 `suno_list_models`；不凭空发生成测试。

确需媒体时，选当前允许的明确模型、输入和预算后授权一次 `suno_generate_music`。保存返回的 task_id，使用 `suno_get_task` 的 `task_id` 查询**同一 ID**。pending 时继续查原 ID，不重跑生成；保留失败/限流/权限错误，不自动切模型。终态成功和可用媒体链接都确认后才展示结果；GPT Image 的 finished_at 只表示终态，失败也会设置；还要检查 response.error / response.success，不能把终态一律当成功。候选包不声称已有付费结果图。

## 常见问题

- 401/403：核对完整原始 Token、应用权限、余额、过期与 Allowed APIs。
- 找不到工具：重启、查看 `/extensions manage`、`/mcp`；同名手工 MCP 配置会覆盖扩展。
- 非交互 permission declined：只授权需要的工具，不默认信任整个服务器。
- pending/超时：查原任务，不自动发新收费请求；429 按响应退避。

[隐私](../PRIVACY.md) · [当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_pricing) · [原有工具实现](https://github.com/AceDataCloud/SunoMCP)。这是 Ace 提供的集成，不冒充 Suno 或 Qwen 官方。
