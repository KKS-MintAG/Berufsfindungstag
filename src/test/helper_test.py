import os

cur_path: str = os.getcwd()
hi: str = "Berufsfindungstag"
print(cur_path)
print(cur_path.rfind(hi))
print(cur_path[:cur_path.rfind(hi)+len(hi)])
os.chdir(cur_path[:cur_path.rfind(hi)])
print(os.getcwd())