from brownie import SimpleCollectible, network, config, accounts
from scripts.helpful_scripts import get_account
from metadata.simple_metadata import metadata_template
from pathlib import Path

simple_token_uri = "https://ipfs.io/ipfs/QmYurS9NiMhG1bbGfsPF5oXakuhHnDZAgJ5iQV8XJwfg49?filename=0.json"

def deploy():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    print(f"Contract deployed to {simple_collectible.address}")
    return simple_collectible

def create_nft():
    account = get_account()
    simple_collectible = SimpleCollectible[-1]
    tx = simple_collectible.createCollectible(simple_token_uri, {"from": account})
    tx.wait(1)

def metadata_create():
    account = get_account()
    simple_collectible = SimpleCollectible[-1]
    number_of_simple_collectible = simple_collectible.tokenCounter()
    for token_id in range(number_of_simple_collectible):
        metadata_file_name = (f"./metadata/{network.show_active()}/{token_id}.json")
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} уже существует. Удали его чтобы перезаписать")
        else:
            print(f"Создание файл метаданных: {metadata_file_name}")
            collectible_metadata["name"] = "Cat"
            collectible_metadata["description"] = "My cat"
            image_path = "./img/Cat.png"
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
# C 1:25:00

def test():
    account1 = get_account()
    #account2 = accounts[2]
    simple_collectible = SimpleCollectible[-1]
    print("Всего токенов", simple_collectible.totalSupply())
    print("Владелец токена ", simple_collectible.ownerOf(0))
    print("URI токена ", simple_collectible.tokenURI(0))
    print("Название колекции", simple_collectible.name())
    print("Количество токенов на счете 1: ", simple_collectible.balanceOf(account1))
    #print("Количество токенов на счете 2: ", simple_collectible.balanceOf(account2))
    #(simple_collectible.approve(account1, 0, {"from": account2})).wait(1)
    #(simple_collectible.safeTransferFrom(account2, account1, 0, {"from": account1})).wait(1)

def main():
    #deploy()
    #create_nft()
    test()
