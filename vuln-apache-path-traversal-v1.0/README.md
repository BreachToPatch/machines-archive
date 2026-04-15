# Archive: vuln-apache-path-traversal-v1.0

> **BreachToPatch — machines-archive**
> Sanitized source code revealed after First Blood. For Blue Team use.

---

## Context

| Field | Value |
|-------|-------|
| Machine slug | `vuln-apache-path-traversal` |
| Archived version | `v1.0` |
| First Blood by | [@MohamedOutougane](https://github.com/MohamedOutougane) |
| First Blood PR | https://github.com/BreachToPatch/machines-public/pull/1 |
| Archived on | 2026-04-15 |

---

## What this archive is

This folder contains the **sanitized source code** of `vuln-apache-path-traversal` as it existed
at version `v1.0`.

It was made public automatically after the first validated pwn, so that Blue Teamers can:
- Study the vulnerable code
- Understand the root cause of the vulnerability
- Propose a patch via Pull Request in `machines-public`

**Important:** The flag value has been replaced by `FLAG{REDACTED}` throughout.
The internal reference exploit has been removed — the locked player exploit is available
in `BreachToPatch/machines-public` under `vuln-apache-path-traversal/exploit/exploit.py`.

---

## How to use this for Blue Team

See the full guide: [GUIDE_BLUETEAM.md](https://github.com/BreachToPatch/docs/blob/main/GUIDE_BLUETEAM.md)

Quick steps:
1. Study the code in this folder to understand the root cause
2. Read the locked exploit at `machines-public/vuln-apache-path-traversal/exploit/exploit.py`
3. Fork `machines-archive` and work on your patch
4. Open a PR on `machines-public` following the `patch/{username}/vuln-apache-path-traversal` branch convention
5. The CI will replay the locked exploit against your patched version — it must exit with code `1`

---

*BreachToPatch — From shadow to light, from breach to patch.*
