# Suno by Ace Data Cloud — Qwen Code extension

Generate Suno music and retrieve completed audio through Ace Data Cloud. A native Qwen extension with one service, its own credential prompt, and the existing hosted MCP implementation. No copied generation backend. Independently install/uninstall this service; the [Ace source catalog](https://github.com/AceDataCloud/AceDataCloudQwenCode) is optional.

**Candidate source, not an official Qwen listing or released default integration.** Implementation is on `codex/native-qwen-extension` pending review. See repository Pull Requests for current state. Do not assume the initial main-branch README is an installable release.

**Current runtime blocker (2026-10-18):** Qwen Code 0.25.2 installs and securely stores the sensitive setting, but its MCP loader does not read that stored value into HTTP Header references. See [upstream bug #14532](https://github.com/QwenLM/qwen-code/issues/14532). Do not treat install/Connected as authenticated use; this candidate is not ready for a real media request until the upstream fix is verified/released. No plaintext-Token workaround or paid retry is recommended.

[简体中文](readme/README_zh_Hans.md) · [Register / sign in](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_signup) · [API and current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_pricing)

## 1. Install using Qwen's extension installer

Qwen Code0.25.2 and Node22 were tested for installation; real authenticated use still requires the fixed release described below. In a terminal run the candidate source command:

```bash
qwen extensions install AceDataCloud/SunoQwenCode --ref codex/native-qwen-extension
```

The normal release command (after the implementation is merged/published) is `qwen extensions install AceDataCloud/SunoQwenCode`. Inspect the source and installation summary before confirming the local extension installation. This does not register an Ace LLM provider.

To discover by brand, add the public [Ace Qwen catalog](https://github.com/AceDataCloud/AceDataCloudQwenCode) using the source URL in its README, then open `/extensions manage` → **Discover** and search **Suno**. A user-added source is not a default Qwen marketplace listing.

## Credential storage and verified platform boundary

**Wait for an official Qwen release containing [fix #14544](https://github.com/QwenLM/qwen-code/pull/14544) before using this extension with a real Token.** Qwen0.25.2 is the installation baseline, not a fixed authenticated-runtime version. No fixed release version has been verified yet.

A [validation-only fork run](https://github.com/AceDataCloud/qwen-code/actions/runs/39109190158) built the owning core package at the exact fix candidate and exercised saved settings through Qwen's real MCP transport to localhost, without forcing a backend:

| Environment | Selected backend | Evidence |
|---|---|---|
| Windows Server2022 x64, Node22.23.3 | System credential store (`keychain` through keytar) | 26 checks PASS, including stored Token → extension Header → localhost initialize. This covers the hosted runner session, not every user's permission or lock state. |
| Linux x64, Node22.23.3 | Qwen's normal `encrypted_file` fallback | 25 checks PASS. The runner's system Secret Service was unavailable; this does not validate Linux Keychain. |
| macOS arm64, Node22.23.3 | Real system Keychain; platform check FAILED | User-scope saved Header and localhost handshake passed, then target-workspace override failed after 11 passing checks. The cause is under focused investigation. The matrix run is not all green. Earlier local x64 encrypted-file CLI evidence does not cover this failure. |

These additional Windows/Linux checks build core and use its real storage/manager/transport; they do not replace a full Windows/Linux interactive CLI test or prove a released fix. Existing macOS source-built CLI checks remain separately recorded.

The installer records the selected backend in `.qwen-extension-settings.json`; no need to copy or expose the secret bundle. Qwen can normally choose encrypted-file storage when the OS backend is unavailable; that is encrypted storage, not a plaintext Token fallback. A missing/unreadable selected store after installation is a failure, not permission to switch credentials silently. The fix candidate keeps the extension manageable and disables its MCP servers on an unreadable store. Check store availability and retry/reload first; do not uninstall for a transient lock or unavailable backend. Only after missing/corrupt settings are confirmed should you back up recoverable settings and consider reinstalling. Reinstall can preserve existing workspace overrides; review and rotate scoped settings through hidden input if needed. Do not export the Token globally, force a different backend, put it in manifests/arguments, unlock a keychain or change OS permissions to work around this candidate's blocker.

## 2. Register, sign in and get an API Token

1. Open [Ace Data Cloud → Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_api_key). Register/sign in if needed. If no **General application** exists, choose **Initialize General Application**.
2. Open **General application** and copy an existing API Key, or choose **Manage Keys → Create** for a dedicated key named `Suno Qwen Code`.
3. Check Suno access, current price and balance; review expiration, usage limitation and Allowed APIs. If restricting APIs, include `/suno/audios`, `/suno/tasks` as applicable to your selected operation. Permissions do not create balance or free generation.

![Copy API Key or open Manage Keys](_assets/tutorial/get-api-key-en.png)

![Create a separate integration key](_assets/tutorial/create-api-key-en.png)

These are real Ace application-page screenshots from the SunoDify onboarding source, pinned 2026-10-07; copied 2026-10-18. Keys are redacted. General application controls are shared; your account and entitlements differ.

## 3. Paste into Qwen's sensitive extension setting

During installation, Qwen asks for **Ace Data Cloud API Token**. Paste only the raw Token, without `Bearer`, quotes or screenshot redaction characters. Qwen stores sensitive extension settings in its credential backend (keychain or encrypted-file fallback). This package stores only `$ACE_SUNO_API_TOKEN` in the HTTP Header template, never a built-in customer Token. Do not paste a Token into chat or run `qwen mcp add` to duplicate this server.

To rotate it later:

```bash
qwen extensions settings set suno-by-ace-data-cloud "Ace Data Cloud API Token"
```

Use Qwen's interactive hidden input, not a command-line argument containing the key. `qwen extensions settings list suno-by-ace-data-cloud` should show the setting masked. Restart an existing session, then open `/mcp` and confirm **suno** is connected. Connection is not a successful API operation.

![Official Qwen historical terminal screenshot with manual-provider annotation](_assets/tutorial/qwen-provider-preview.png)

This is an official Qwen v0.18.2 screenshot edited on 2026-10-17, not an Ace run. It shows the native terminal and a separate custom-model setup entry, **not** the extension Token prompt. The current extension-settings screenshot is queued for capture; this image cannot prove this package installed or a paid request succeeded.

## 4. First use, result and the same task ID

A chat model is configured separately in Qwen. Inspect `suno_list_models` to list available Suno models without generating media. You can also ask Qwen to show the schemas of this extension's tools; an assistant response may consume your chat-model quota.

When you choose to spend on media, specify your desired inputs, an explicitly chosen current model and budget, then authorize **one** `suno_generate_music` operation. It may return a `task_id` before completion. Poll `suno_get_task` with **task_id = that same task ID**. Never regenerate to poll. Do not fabricate an ID for a setup test.

For a pending task, wait and retrieve the same ID again. For a failed task, preserve its error. Only present completed media after the terminal success and returned URL are verified. For GPT Image, `finished_at` means terminal even on failure: inspect `response.error` / `response.success` before treating it as a successful result; media result shapes vary by service. No paid result screenshot is claimed in this candidate.

## Troubleshooting

| Symptom | Action |
|---|---|
| Install source/main has no manifest | Use the candidate `--ref` while review is open; do not describe this as a released default install. |
| 401 / 403 | Check raw API Token, service access, expiry and Allowed APIs. A `platform-...` management token is not a media API Token. |
| Missing tools | Restart Qwen, check `/extensions manage` and `/mcp`; settings.json with the same MCP name overrides an extension. |
| Permission declined in scripts | Non-interactive calls cannot ask for approval; authorize only the required tool. Never auto-trust the whole service. |
| Pending / timeout | Query the original task ID. Do not retry generation automatically. |
| 429 / failed | Respect the response and limits; no automatic model substitution or new paid retry. |

## Privacy, pricing and support

The extension is free source; existing Ace service requests may be charged. User-chosen inputs and your Token are sent over HTTPS to `suno.mcp.acedata.cloud` and the Ace API. See [Privacy](PRIVACY.md), [pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_pricing) and [service documentation](https://platform.acedata.cloud/documents/suno?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=sunoqwencode_readme_service_docs). This is provided by Ace Data Cloud and is not an official Suno or Qwen endorsement.

[Upstream MCP implementation](https://github.com/AceDataCloud/SunoMCP) · [Official Qwen extension documentation](https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/) · [Report a problem](https://github.com/AceDataCloud/SunoQwenCode/issues) · dev@acedata.cloud.
