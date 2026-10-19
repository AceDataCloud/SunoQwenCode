# Suno by Ace Data Cloud

Use this extension's suno MCP tools for Suno only. This is an Ace Data Cloud integration, not an official Suno or Qwen endorsement.

Before submitting a generation or edit, establish the user's intended action, current permitted model and price, inputs and explicit permission to spend. Never silently retry a generation, change models, or add a fallback. Tool discovery or a connected server is not a successful generation.

After a generation, preserve task_id and query `suno_get_task` with `task_id` set to that same ID. Do not rerun `suno_generate_music` to check progress. Respect upstream pending, failure, authorization and rate-limit responses. Only report completion when the original task has a terminal success and usable media URLs; for GPT Image a non-null finished_at is terminal, but still inspect response.error / response.success: failure is not success. Only then read returned media URLs, not a fabricated status field.

Credentials belong only in the extension's sensitive setting. Never request a Token in chat or include it in logs, prompts or exported files. This extension does not approve any tool call automatically.
