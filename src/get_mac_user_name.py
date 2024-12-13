import osquery

def get_mac_user_name():
    instance = osquery.ExtensionClient('/Users/Sebastian/.osquery/shell.em')
    instance.open()
    client = instance.extension_client()
    users = client.query('select username from users;')
    print(users)
    return users
def main():

    #instance = osquery.SpawnInstance()
    instance = osquery.ExtensionClient('/Users/Sebastian/.osquery/shell.em')
    #instance = osquery.ExtensionClient('/usr/local/bin/osqueryi')
    instance.open()  # This may raise an exception

    # Issues queries and call osquery Thrift APIs.
    # instance.extension_client
    # instance.client.query("select username from users;")
    client = instance.extension_client()
    print(client.query('select username from users;'))

if __name__ == "__main__":
    main()