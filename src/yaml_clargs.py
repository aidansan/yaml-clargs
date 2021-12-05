import yaml
import argparse
import pprint
import re

# https://stackoverflow.com/a/30462009
loader = yaml.SafeLoader
loader.add_implicit_resolver(
    u'tag:yaml.org,2002:float',
    re.compile(u'''^(?:
    [-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+]?[0-9]+)?
    |[-+]?(?:[0-9][0-9_]*)(?:[eE][-+]?[0-9]+)
    |\\.[0-9_]+(?:[eE][-+][0-9]+)?
    |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*
    |[-+]?\\.(?:inf|Inf|INF)
    |\\.(?:nan|NaN|NAN))$''', re.X),
    list(u'-+0123456789.'))


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

def yaml_clargs(parser=None, print_config=True, encoding='utf-8'):
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', type=str, required=False, default='config_files/default.yaml', help='filename of config file')
    parser.add_argument('--default_config_file', type=str, required=False, default='', help='filename of default config file')
    args = parser.parse_args()

    # Load in default hyperparameters
    if args.default_config_file:
        with open(args.default_config_file) as f:
            config = YamlClargs(yaml.load(f, Loader=loader))
    else:
        # TODO check if a default.yaml file exists
        config = YamlClargs()

    # Load in config file hyperparameters
    with open(args.config_file, encoding=encoding) as f:
        for k, v in yaml.load(f, Loader=loader).items():
            setattr(config, k, v)

    if print_config:
        print(config)
    return config
