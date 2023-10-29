import requests


res = requests.post("http://127.0.0.1:1232/api/zbolj23bn156m69mu6f3xzlmvmwm3m/get_code", json={"type_game": "викторина"})
print(res.status_code)
print(res.json())

res = requests.get("http://127.0.0.1:1232/api/zbolj23bn156m69mu6f3xzlmvmwm3m/update_player", json={"code_room": "AEU0"})
print(res.status_code)
print(res.json())

res = requests.post("http://127.0.0.1:1232/api/zbolj23bn156m69mu6f3xzlmvmwm3m/exit", json={"code_room": "AEU0"})
print(res.status_code)
print(res.json())

