from ldap3 import Server, Connection, ALL

server = Server('ldap://DC02.odchc.org')
conn = Connection(server, user='jwilliams', password='')
conn.bind()

conn.search('dc=odchc,dc=org', '(&(objectclass=person)(userPrincipalName=jvangurp@odchc.org))', attributes=['*'], paged_size=1000)
print(conn.entries)


conn.unbind()