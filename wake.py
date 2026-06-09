import yaml
from huggingface_hub import HfApi

with open("config.yml") as f:
    config = yaml.safe_load(f)

wake_only = set(config.get("wake_spaces") or [])
ignored = set(config.get("ignored_spaces") or [])

api = HfApi()
spaces = api.list_spaces(author=config["hf_username"], expand=["runtime"])

for space in spaces:
    name = space.id.split("/")[-1]
    skip = name not in wake_only if wake_only else name in ignored
    if skip:
        print(f"{space.id}: skipped")
        continue
    stage = space.runtime.stage if space.runtime else None
    if stage == "SLEEPING":
        try:
            api.restart_space(space.id)
            print(f"woke {space.id}")
        except Exception as e:
            print(f"FAIL {space.id}: {e}")
    else:
        print(f"{space.id}: {stage}")
