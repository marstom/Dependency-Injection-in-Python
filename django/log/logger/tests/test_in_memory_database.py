from log.logger.database_repo.in_memory_database_repo import InMemoryDatabase


def test_in_memory_database_save_load(log_info_data, log_warn_data):
    repo = InMemoryDatabase(connection=None, access_path="xyz")
    repo.save_data(object_name="logs", data=log_info_data)
    repo.save_data(object_name="logs", data=log_warn_data)

    assert len(repo.load_data(object_name="logs")) == 2
    assert repo.load_data(object_name="logs")[1]["content"] == "this is warning"
    assert repo.load_data(object_name="logs")[1]["type"] == "WARNING"


def test_in_memory_database_save_more_objects(log_info_data, log_warn_data):
    repo = InMemoryDatabase(connection=None, access_path="xyz")
    repo.save_data(object_name="warns", data=log_warn_data)
    repo.save_data(object_name="infos", data=log_info_data)

    assert repo.load_data(object_name="warns")[0]["type"] == "WARNING"
    assert repo.load_data(object_name="infos")[0]["type"] == "INFO"