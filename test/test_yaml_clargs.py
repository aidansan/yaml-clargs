from yaml_clargs import yaml_clargs
import sys
# https://stackoverflow.com/questions/30458977/yaml-loads-5e-6-as-string-and-not-a-number

# Config 1
# lr: .0005
# beam_size: 4

# Default
# batch_size: 64
# lr: .001
# dropout: .5

# Use no default config file (only main config file)
sys.argv =['test_json_clargs.py', '--config_file', 'config_files/config1.yaml']
config1 = yaml_clargs()
assert config1.lr == .0005
assert config1.beam_size == 4 
assert len(config1.__dict__) == 3 # 2 attributes + pprinter

sys.argv =['test_json_clargs.py']
# Use default.yaml as main config file
config2 = yaml_clargs()
assert config2.lr == .001
assert config2.batch_size == 64
assert config2.dropout == .5
assert len(config2.__dict__) == 4 # 3 attributes + pprinter

# Use both a main config file and default config file
#'--default_config_file'
sys.argv =['test_json_clargs.py', '--config_file', 'config_files/config1.yaml', '--default_config_file', 'config_files/default.yaml']
config3 = yaml_clargs()
assert config3.lr == .0005
assert config3.batch_size == 64
assert config3.dropout == .5
assert config3.beam_size == 4
assert len(config3.__dict__) == 5 # 4 attributes + pprinter

