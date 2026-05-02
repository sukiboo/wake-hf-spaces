import yaml
from huggingface_hub import HfApi

with open("config.yml") as f:
    config = yaml.safe_load(f)

api = HfApi()
spaces = api.list_spaces(author=config["hf_username"], expand=["runtime"])

for space in spaces:
    stage = space.runtime.stage if space.runtime else None
    if stage == "SLEEPING":
        try:
            api.restart_space(space.id)
            print(f"woke {space.id}")
        except Exception as e:
            print(f"FAIL {space.id}: {e}")
    else:
        print(f"{space.id}: {stage}")
