# wake-hf-spaces 🤗👈

[![wake](https://github.com/sukiboo/wake-hf-spaces/actions/workflows/wake.yml/badge.svg)](https://github.com/sukiboo/wake-hf-spaces/actions/workflows/wake.yml)
[![keepalive](https://github.com/sukiboo/wake-hf-spaces/actions/workflows/keepalive.yml/badge.svg)](https://github.com/sukiboo/wake-hf-spaces/actions/workflows/keepalive.yml)

Daily GitHub Actions workflow that wakes sleeping Hugging Face Spaces via the
HF API. A second monthly workflow pushes an empty commit so GitHub doesn't
auto-disable the schedule after 60 days of repo inactivity.

## How it works

- `.github/workflows/wake.yml` runs daily: lists your spaces, restarts any in
  `SLEEPING` state, leaves running/error spaces alone.
- `.github/workflows/keepalive.yml` runs on the 1st of each month: empty
  commit to keep the schedule alive.

Spaces re-sleep after ~48h of inactivity on free CPU, so this is a continuous
wake/sleep cycle, not always-on.

## Setup

1. Fork this repo.
2. Edit `config.yml`:
   - `hf_username` — your HF username.
   - `ignored_spaces` — optional list of space names (no `username/` prefix)
     to skip (e.g. outdated demos you don't want restarted).
3. Create an HF token at https://huggingface.co/settings/tokens with write
   access to your spaces (see [Token scope](#token-scope) below).
4. Add it to the repo as a secret named `HF_TOKEN` (repo Settings → Secrets
   and variables → Actions → New repository secret).
5. (Optional) Adjust cron schedules in the two workflow files.

Trigger a run manually from the Actions tab → pick workflow → *Run workflow*.

## Token scope

The workflow needs an `HF_TOKEN` repo secret to call `restart_space()` on
sleeping spaces. Two ways to scope it, with a tradeoff:

- **Per-space (strict):** create a fine-grained token granting *Write access to
  contents/settings of selected repos* and pick each space individually. If the
  token leaks, only those specific spaces can be modified. Downside: you have
  to re-issue the token whenever you add a new space.
- **Namespace-wide (convenient):** grant *Write access to contents/settings of
  all repos under your personal namespace*. Covers new spaces automatically,
  but a leak gives an attacker write access to every repo in your namespace
  (models, datasets, spaces). Fine for hobby accounts; reconsider if your
  namespace holds anything sensitive.

Note: HF's UI auto-enables *Read access* alongside *Write* — that's expected
and cannot be unchecked.
