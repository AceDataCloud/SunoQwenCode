# Scope

This repo owns one Qwen native extension manifest, commands and onboarding only. Reuse the existing hosted MCP; never fork service generation logic here. Keep credentials in sensitive settings and literal env references, do not introduce trust bypasses or automatic paid retries. Review before publishing. Validate with Python unittest discovery; use only fake tokens and localhost for CLI tests. No paid generation, merge or deployment without separate authorization.
