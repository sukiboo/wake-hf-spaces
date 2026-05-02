# wake-hf-spaces
Simple script to keep my HF spaces awake

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
