
#

#!pip install ncclient
#!pip install xmltodict
#f = open("capabilities.txt", "w")
from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
m = manager.connect(host='192.168.2.12', port='830', username='root', password='ChgMeNOW', device_params={'name':'iosxe'}, hostkey_verify=False)
print(m.connected)
running_config = m.get_config('running').xml


############## Change the Network element name ############
filter4 = """
<config>
   <sub-network xmlns="http://www.advaoptical.com/ns/yang/fsp150cm-entity">
    <network-element>
            <ne-id>1</ne-id>
            <ne-name>FSP150CC-XG116PRO-German</ne-name>
    </network-element>
   </sub-network>         
</config>
"""

############## Set port up  ############

filter5= """
    <config>
      <sub-network xmlns="http://www.advaoptical.com/ns/yang/fsp150cm-entity">
        <network-element>
          <ne-id>1</ne-id>
          <shelf>
            <shelf-id>1</shelf-id>
            <slot>
              <slot-id>1</slot-id>
              <card>
                <ethernet-card>
                  <ethernet-port xmlns="http://www.advaoptical.com/ns/yang/fsp150cm-facility">
                    <port-id>1</port-id>
                    <port-type>eth-port</port-type>
                    <admin-state>in-service</admin-state>
                    <alias>Puerto No. 1</alias>
                    <description>ETHERNET NETWORK PORT</description>
                    <mtu>9638</mtu>
                    <media-type>fiber</media-type>
                    <config-speed>speed-auto-1000MB-full</config-speed>
                  </ethernet-port>
                </ethernet-card>
              </card>
            </slot>
          </shelf>
        </network-element>
      </sub-network>
    </config>
"""

############## Set port down  ############

filter6= """
    <config>
      <sub-network xmlns="http://www.advaoptical.com/ns/yang/fsp150cm-entity">
        <network-element>
          <ne-id>1</ne-id>
          <shelf>
            <shelf-id>1</shelf-id>
            <slot>
              <slot-id>1</slot-id>
              <card>
                <ethernet-card>
                  <ethernet-port xmlns="http://www.advaoptical.com/ns/yang/fsp150cm-facility">
                    <port-id>1</port-id>
                    <port-type>eth-port</port-type>
                    <admin-state>unassigned</admin-state>
                    <alias>Puerto No. 1</alias>
                    <description>ETHERNET NETWORK PORT</description>
                    <mtu>9638</mtu>
                    <media-type>fiber</media-type>
                    <config-speed>speed-auto-1000MB-full</config-speed>
                  </ethernet-port>
                </ethernet-card>
              </card>
            </slot>
          </shelf>
        </network-element>
      </sub-network>
    </config>
"""


result = m.edit_config(target='running', config=filter5)
if "<nc:ok/>" in result.xml:
    print("OK")

