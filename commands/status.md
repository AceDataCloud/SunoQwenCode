---
description: Retrieve an existing Suno task without regenerating
---
Use the task ID supplied in {{args}}. If no ID was supplied, ask for the existing task ID, not a credential. Call only suno_get_task with task_id set to that ID. Preserve pending/failed/terminal meaning and returned media URLs. Do not submit a generation, retry with a new ID or claim success from connectivity alone.
