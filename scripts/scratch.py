from brownie import config, network


def check_configs():
    print(config["networks"][network.show_active()].get("default"))


def main():
    check_configs()
