import requests

#MASUKAN DATAKAMU DISINI
username = "YOUR_GITHUB_USERNAME"
token = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"

base_url = "https://api.github.com/user/repos"


headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}


response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["url"]

        # Hapus repositori
        delete_response = requests.delete(repo_url, headers=headers)

        if delete_response.status_code == 204:
            print(f"Repositori '{repo_name}' berhasil dihapus.")
        else:
            print(f"Gagal menghapus repositori '{repo_name}': {delete_response.status_code}")
else:
    print(f"Gagal mengambil daftar repositori: {response.status_code}")
