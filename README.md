# machines-archive 📦

> **Public repository — `BreachToPatch` organization**
> The graveyard of secrets. Source code revealed after the first pwn — the raw material for Blue Teamers.

---

## What this repo is

`machines-archive` is the **post-pwn source code library**. When a machine is successfully pwned for the first time, its source code (Vagrantfile, Ansible playbook, Docker configuration, application code) is **archived here** so that Blue Teamers can study it, fork it, and propose security patches.

It is also a historical record: every version of every machine that has ever existed on the platform lives here permanently.

---

## Why this exists

The BreachToPatch cycle depends on this handoff:

```
[Red Team pwns the machine]
         │
         ▼
[Sources are revealed here]   ← machines-archive
         │
         ▼
[Blue Team forks the code, finds the root cause, proposes a patch]
         │
         ▼
[Patch is validated → new version of the machine is released]
```

Without this repo, Blue Teamers would have nothing to work with. The vulnerability is a **black box** during the Red Team phase, but becomes a **white box** once someone has cracked it.

---

## What lives here

Each entry in this archive corresponds to a specific **version** of a machine at the moment it was first pwned.

```
machines-archive/
├── README.md                              ← You are here
│
└── vuln-apache-path-traversal-v1.0/       ← Revealed after first pwn of Bee-Path v1.0
    ├── README.md                          # Context: what the vuln was, when it was pwned
    ├── Vagrantfile                        # VM definition (flag removed)
    ├── provision/
    │   ├── playbook.yml                   # Ansible playbook (flag replaced with placeholder)
    │   └── roles/
    │       ├── docker/
    │       └── flag/
    ├── app/
    │   ├── docker-compose.yml
    │   └── apache/
    │       ├── Dockerfile
    │       └── httpd.conf                 # ← The vulnerable config Blue Teamers need to fix
    └── tests/
        ├── health_check.sh
        └── service_test.py
```

> **Note:** The flag value is **removed** before archiving. The `provision/roles/flag` task is replaced with a placeholder so the archive is safe to make public.

---

## For Blue Teamers — How to use this repo

1. **Find the machine** you want to patch (e.g., `vuln-apache-path-traversal-v1.0/`)
2. **Read the README** inside the folder to understand the vulnerability context
3. **Fork this repository** to your own GitHub account
4. **Study the code** — find the root cause of the vulnerability
5. **Apply your fix** — edit the relevant files (e.g., `httpd.conf`, `docker-compose.yml`, application source code)
6. **Test your patch** locally using `vagrant up` with your modified code
7. **Open a Pull Request** in `machines-public` with your patch writeup

The CI pipeline will automatically:
- Boot a VM using your patched code
- Check that all services still respond (SLA test)
- Run the original exploit against your patched version — it **must fail**
- Scan for new backdoors or secrets

See the [Blue Team Guide](../docs/GUIDE_BLUETEAM.md) for detailed instructions.

---

## Naming convention

Archive folders are named: `{machine-slug}-v{version}/`

| Folder | Meaning |
|--------|---------|
| `vuln-apache-path-traversal-v1.0` | Bee-Path, original version, revealed after first pwn |
| `vuln-apache-path-traversal-v1.1` | Bee-Path after first patch, revealed after second pwn |

---

## How this repo interacts with other repos

```
machines-sources (btop-sources, private)
   └── Maintainers copy sanitized sources here after first pwn
       (flag removed, internal comments cleaned)

machines-archive (this repo) ←── Blue Teamers fork from here

machines-public (BreachToPatch, public)
   └── Blue Team patch PRs are submitted there
   └── Patch PRs reference which archive version they are fixing
```
