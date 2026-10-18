# Validation (2026-10-18)

Official Qwen Code0.25.2 macOS x64; fake per-service secret and isolated profile. Native extension install, hidden prompt, manifest retained, masked setting listing, no plaintext secret in profile: PASS. Five independent packages installed from their immutable candidate GitHub archive URLs on one complete remote run; later network fetches were intermittent and local snapshots were used only for diagnosis.

Native source discovery returned all five brand entries. This is a user-added Ace catalog, not a default official Qwen listing.

BLOCKED: runtime HTTP Headers remain literal environment references even after the native secret setting is stored. Reproduced with5 localhost-only initialize connections,0 correct secret expansion; no media/model/production tools/call. Upstream issue: https://github.com/QwenLM/qwen-code/issues/14532 . No authenticated business-operation claim.

Tests: python3 -m unittest discover -s tests -v. Images are real redacted Ace Key screenshots plus a labeled official historical provider-entry edit; current extension-settings capture is queued, not forged.
