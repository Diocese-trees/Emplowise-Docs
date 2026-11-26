# Backups and restore

How the three repositories are backed up, where the copies live, how to restore
one, and what the 2026-11-26 release changed. Written to be usable by someone
who has only this repository and a shell.

## Repositories covered

| Repository | Role | Visibility | Canonical remote | Working clone |
| --- | --- | --- | --- | --- |
| `Emplowise-Website-Phase-I` | Laravel marketing site, `/docs` hub, showcase pages, publishes `gh-pages` | public | `https://github.com/Diocese-trees/Emplowise-Website-Phase-I.git` | `/data/emplowise` |
| `Emplowise-Docs` | Markdown source of truth, brand tokens, Office generators, internal reports | public | `https://github.com/Diocese-trees/Emplowise-Docs.git` | `/data/emplowise/_staging/Emplowise-Docs` |
| `EmploStart` | Standalone free career product, publishes its own Pages site | public | `https://github.com/Diocese-trees/EmploStart.git` | no clone; restored from mirror or bundle |

The website repo also has the private work-in-progress mirror
`Emplowise-repo-qodar-ai-work-in-progress` (remote name `wip`). It is a full
mirror kept in sync by `sync-from-upstream.yml`; it is not a backup target and
publishes nothing.

## What a backup is

Each backup round produces, per repository:

1. a **bare mirror** (`<repo>.git`) fetched from the canonical remote, plus any
   local-only refs from the working clone, with `refs/pull/*` excluded;
2. a **git bundle** (`<repo>.bundle`) built with `--all`, so every branch, tag
   and `HEAD` restores offline;
3. a **checksum** (sha256) and byte count in `MANIFEST.txt`;
4. a **verification** result from `git bundle verify` (must print `is okay`);
5. a **restore check**: a throwaway clone from the bundle whose `HEAD` must equal
   the mirror's `refs/heads/main`.

A clone of the bundle is a working repository on its own. Nothing depends on the
mirror directory surviving.

## Backup locations

| Path | Date | Contents |
| --- | --- | --- |
| `/data/backups/20261126-seo-phase8/` | 2026-11-26 | Current round: three mirrors, three bundles, `MANIFEST.txt`, `MANIFEST.json`, source snapshots of the website and Docs working trees |
| `/data/backups/20261126-shadow/` | 2026-11-26 | Earlier round from the same day: bundles plus the pre-audit archive zip |
| `/data/backups/20261124-vercel/` | 2026-11-24 | Previous round: three bundles, Vercel config zip, manifest |
| `/data/backups/20261123-exec-report/` | 2026-11-23 | Executive report inputs |
| `/data/backups/emplowise-main-*.bundle`, `emplowise-worktree-*.tar.gz` | 2026-11-22 onwards | Per-step bundles and working-tree tarballs kept during the redesign |

Backups are local to the workspace. Durability comes from the shadow
repositories below, not from the workspace itself, which is temporary.

## Private shadow repositories

Each round pushes every branch and tag to a private repository in the same
GitHub account:

| Shadow repository | Mirrors |
| --- | --- |
| `Diocese-trees/Emplowise-Website-Phase-I-shadow-20261126` | website: 28 branches, 16 tags |
| `Diocese-trees/Emplowise-Docs-shadow-20261126` | Docs: 2 branches, 1 tag |
| `Diocese-trees/EmploStart-shadow-20261126` | EmploStart: 1 branch, 1 tag |

Push policy, deliberately narrow:

```bash
git push --prune --force <shadow-url> \
  '+refs/heads/*:refs/heads/*' '+refs/tags/*:refs/tags/*'
```

Only `refs/heads/*` and `refs/tags/*` are pushed. GitHub-managed `refs/pull/*`
stay in the local mirror: they are review metadata, not history. The push is
`--force --prune` on purpose, because the shadow must match the source exactly;
a mirror that silently keeps a deleted branch is not a mirror.

Authentication uses the token already in the git credential store. It is passed
as a per-command header, never written into a remote URL or a config file.

## Restore

### From a bundle (offline, no network)

```bash
OUT=/data/backups/20261126-seo-phase8
mkdir -p /tmp/restore && cd /tmp/restore
git clone "$OUT/Emplowise-Website-Phase-I.bundle" site
cd site
git rev-parse HEAD                    # must match MANIFEST.txt
git branch -a | head                  # every branch and tag is present
git tag | sort | tail
```

To restore a specific ref from a bundle without cloning:

```bash
git clone "$OUT/EmploStart.bundle" emplostart
git -C emplostart checkout main
```

### From a shadow repository

```bash
git clone https://github.com/Diocese-trees/Emplowise-Website-Phase-I-shadow-20261126.git site
git -C site fetch --tags --prune
git -C site branch -a
```

### From an existing mirror

```bash
git clone --mirror /data/backups/20261126-seo-phase8/Emplowise-Docs.git docs.git
git clone docs.git docs-work && git -C docs-work log --oneline -1
```

### Verify a backup before trusting it

```bash
cd /data/backups/20261126-seo-phase8
git bundle verify Emplowise-Website-Phase-I.bundle      # prints "is okay"
sha256sum -c <(grep -E '^[0-9a-f]{64}  ' MANIFEST.txt)  # if checksums were saved in that form
```

`git bundle verify` writes its verdict to stderr and needs to run inside a
repository, hence the `cd` into the mirror or a clone.

### Re-publish a restored site

A restored clone has no GitHub remote by default when it came from a bundle:

```bash
git remote add origin https://github.com/Diocese-trees/Emplowise-Website-Phase-I.git
git push origin main
```

`publish-static.yml` then rebuilds `gh-pages`, which is the same path a normal
merge takes.

## Release of 2026-11-26

The Phase 8 SEO rewrite was merged with a fast-forward, so `main` has no merge
commit and history stays linear.

| Step | Result |
| --- | --- |
| Branch | `seo-rewrite-20261126` at `26834d7` |
| Pull request | #3, "Phase 8 SEO/AEO/GEO rewrite across all public pages" |
| CI on the pull request | run 45898488118, passed |
| Merge | `main` 89a8e7f → 26834d7, fast-forward, no merge commit |
| CI on `main` | run 45898538138, passed |
| Publish static site | run 45898538129, passed; `gh-pages` updated |
| Publish Vercel branch | run 45898538106, skipped; gate variable off |
| Deploy to Vercel | run 45898537940, skipped; gate variable off |

Gate results at `26834d7`: `php artisan emplowise:seo-audit` 15/15,
`php artisan test` 57 passed (902 assertions), static export 15 pages. Brand
kit, colours, fonts and logos are unchanged.

### Rollback

Reverting is a normal revert commit; do not rewrite published history:

```bash
cd /data/emplowise
git revert --no-edit 26834d7
git push origin main
```

That restores the 89a8e7f copy and retriggers CI and `gh-pages`. If the site
must be served from the old tree immediately, point Pages at the previous
`gh-pages` commit while the revert runs. A full offline restore from the bundle
above is the last resort and does not require GitHub at all.

## Limits worth knowing

- A bundle captures committed history only. Untracked files and ignored build
  output are covered by the source snapshots in the round directory, not the
  bundle. Both working clones were clean at capture time.
- `refs/pull/*` are not mirrored remotely. Reconstructing a review thread needs
  GitHub, not the backup.
- The shadow repos live in the same account as the originals. They protect
  against branch loss, force-pushes and accidental history edits; they do not
  protect against loss of the account. Treat an account-level export as a
  separate, offsite task.
- Checksums detect corruption, not tampering. Sign or store the manifest
  elsewhere if provenance matters.
