from client import YougileProjectClient


def get_api_client():
    return YougileProjectClient()


def test_post_project_positive():
    client = get_api_client()
    title = "new projects"
    response = client.create_project(title=title)
    assert response.status_code == 201
    res_data = response.json()
    assert "id" in res_data
    client.delete_project(res_data["id"])


def test_get_project_positive():
    client = get_api_client()
    create_res = client.create_project(title="test")
    project_id = create_res.json()["id"]
    response = client.get_project(project_id)
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["id"] == project_id
    assert "title" in res_data
    client.delete_project(project_id)


def test_put_project_positive():
    client = get_api_client()
    create_res = client.create_project(title="test projects")
    project_id = create_res.json()["id"]
    new_title = "project"
    response = client.update_project(project_id, title=new_title)
    assert response.status_code == 200
    get_response = client.get_project(project_id)
    assert get_response.json()["title"] == new_title
    client.delete_project(project_id)


def test_post_project_negative_empty_title():
    client = get_api_client()
    response = client.create_project(title="")
    assert response.status_code == 400
    assert "error" in response.text.lower(
    ) or "message" in response.text.lower()


def test_get_project_negative_invalid_id():
    client = get_api_client()
    invalid_id = "2345677-hkb-f56yh-gjht-h67tgfgbv56"
    response = client.get_project(invalid_id)
    assert response.status_code == 404


def test_put_project_negative_invalid_id():
    client = get_api_client()
    invalid_id = "2345677-hkb-f56yh-gjht-h67tgfgbv56"
    response = client.update_project(invalid_id, title="new name")
    assert response.status_code == 404
