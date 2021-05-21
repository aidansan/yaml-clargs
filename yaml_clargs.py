import yaml
import argparse
import pprint

# https://stackoverflow.com/a/63944491/5187393
def without_keys(d, keys):
    return {k: d[k] for k in d.keys() - keys}

# Could use setattr instead
class YamlClargs:
    def __init__(self, d=dict()):
        self._pprinter = pprint.PrettyPrinter(indent=4)

        for k, v in d.items():
            setattr(self, k, v)

    def __str__(self):
        return self._pprinter.pformat(
                    without_keys(self.__dict__, ['_pprinter']))

    def __repr__(self):
        return self.__str__()

def yaml_clargs(parser=None, print_config=True):
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', type=str, required=False, default='config_files/default.yaml', help='filename of config file')
    parser.add_argument('--default_config_file', type=str, required=False, default='', help='filename of default config file')
    args = parser.parse_args()

    # Load in default hyperparameters
    if args.default_config_file:
        with open(args.default_config_file) as f:
            config = YamlClargs(yaml.safe_load(f))
    else:
        # TODO check if a default.yaml file exists
        config = YamlClargs()

    # Load in config file hyperparameters
    with open(args.config_file) as f:
        for k, v in yaml.safe_load(f).items():
            setattr(config, k, v)

    if print_config:
        print(config)
    return config
