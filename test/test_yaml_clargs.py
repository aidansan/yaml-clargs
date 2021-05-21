from data_util.yaml_clargs import yaml_clargs

config = yaml_clargs()
print(config['lr'] + .5)