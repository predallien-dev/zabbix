# Это тест интеграцтии с гитхабом, не нужно его исполнять

from pyzabbix.api import ZabbixAPI

zapi = ZabbixAPI(url='URL', user='m.gerbersgagen', password='password*')
res = zapi.do_request(method="host.create", params= {
                          "host": "testapi",
                          "interfaces": [
                              {
                                  "type": '1',
                                  "main": '1',
                                  "useip": '1',
                                  "ip": '192.168.10.252',
                                  "dns": '',
                                  "port": '10050'}],
                          "groups": [
                              {"groupid": "50"}
                          ],
                      }
                      )
print(res)
zapi.user.logout()
