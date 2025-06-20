import yaml
from typing import Any, Dict


# This function will be used to represent strings in the YAML output
def str_presenter(dumper: yaml.Dumper, data: str) -> yaml.ScalarNode:
    if len(data.splitlines()) > 1:  # check for multiline
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_presenter)


def prune_examples(obj: Any) -> Any:
    if isinstance(obj, dict):
        result: Dict[str, Any] = {}
        for key, value in obj.items():
            if key not in ["example", "examples"]:
                result[key] = prune_examples(value)
        return result
    elif isinstance(obj, list):
        return [prune_examples(item) for item in obj]
    else:
        return obj


if __name__ == "__main__":
    with open("openapi.yaml", "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    pruned_spec = prune_examples(spec)

    with open("openapi_no_examples.yaml", "w", encoding="utf-8") as f:
        yaml.dump(pruned_spec, f, default_flow_style=False, sort_keys=False, indent=2)
