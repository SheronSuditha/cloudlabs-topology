"""demo-1

Instructions:
demo-1"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node client1
node_client1 = request.RawPC('client1')
node_client1.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client1.sh'))
iface0 = node_client1.addInterface('interface-1', pg.IPv4Address('192.168.4.1','255.255.255.0'))

# Node client2
node_client2 = request.RawPC('client2')
node_client2.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client2.sh'))
iface1 = node_client2.addInterface('interface-2', pg.IPv4Address('192.168.4.2','255.255.255.0'))

# Node client3
node_client3 = request.RawPC('client3')
node_client3.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/client3.sh'))
iface2 = node_client3.addInterface('client:interface-3', pg.IPv4Address('192.168.4.3','255.255.255.0'))

# Node router
node_router = request.RawPC('router')
node_router.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/router.sh'))
iface3 = node_router.addInterface('interface-1', pg.IPv4Address('192.168.6.1','255.255.255.0'))
iface4 = node_router.addInterface('interface-3', pg.IPv4Address('192.168.7.1','255.255.255.0'))

# Node server
node_server = request.RawPC('server')
node_server.addService(pg.Execute(
    '/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/server.sh'))
iface5 = node_server.addInterface('interface-0', pg.IPv4Address('192.168.8.2','255.255.255.0'))

# Link link-1
link_1 = request.Link('link-1')
link_1.addInterface(iface2)
link_1.addInterface(iface0)
link_1.addInterface(iface1)
link_1.addInterface(iface4)

# Link link-3
link_3 = request.Link('link-3')
link_3.addInterface(iface3)
link_3.addInterface(iface5)


# Print the generated rspec
pc.printRequestRSpec(request)
