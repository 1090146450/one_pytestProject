import yaml

with open("./Params/Login.yaml", encoding="gbk", mode="r") as f:
    val = yaml.load_all(stream=f, Loader=yaml.FullLoader)
    print([i for i in val])
