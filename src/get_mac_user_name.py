import osquery

def get_mac_user_name(port):
    instance = osquery.ExtensionClient(port)
    instance.open()
    client = instance.extension_client()
    users = client.query('select username from users;')
    print(users)
    return users