import yaml
import argparse
import pprint

# Could use setattr instead
class YamlClargs:
    def __init__(self, d=dict()):
        for k, v in d.items():
            setattr(self, k, v)

def yaml_clargs(parser=None, print_config=True):
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', type=str, required=False, default='config_files/default.yaml', help='filename of config file')
    parser.add_argument('--default_config_file', type=str, required=False, default='config_files/default.yaml', help='filename of default config file')
    args = parser.parse_args()
    with open(args.default_config_file) as f:
        config = yaml.safe_load(f)
    with open(args.config_file) as f:
        for k, v in yaml.safe_load(f).items():
            config[k] = v
    if print_config:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(config)
    return config
