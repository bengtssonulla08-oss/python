import requests
from configuration import BASE_URL, TOKEN


class YougileProjectClient:
    def __init__(self):
        self.base_url = f"{BASE_URL}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str, users: dict = None):
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(self.base_url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        return requests.get(f"{self.base_url}/{project_id}",
                            headers=self.headers)

    def update_project(self, project_id: str, title: str):
        payload = {"title": title}
        return requests.put(f"{self.base_url}/{project_id}",
                            json=payload, headers=self.headers)

    def delete_project(self, project_id: str):
        return requests.delete(f"{self.base_url}/{project_id}",
                               headers=self.headers)
