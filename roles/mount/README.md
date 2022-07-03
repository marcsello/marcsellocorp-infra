This role is used to handle mounts other than the root disk.

When setting the device id for block devices provided by virtio, you can use multiple methods to set the correct value. 

Since libvirt and virtio disk handler is capable of setting a fix device node (e.g.: `/dev/vdb`) you can use this safely.

Otherwise the recommended way to set the device value is to use bus path assigned by libvirt.
Something similar to this:
```
/dev/disk/by-path/virtio-pci-0000:09:00.0
```
The corresponding entry in the libvirt config is the following:
```
<disk type="block" device="disk">
  <driver name="qemu" type="raw" cache="none" io="native"/>
  <source dev="/dev/storage/generic" index="2"/>
  <backingStore/>
  <target dev="vdb" bus="virtio"/>
  <alias name="virtio-disk1"/>
  <address type="pci" domain="0x0000" bus="0x09" slot="0x00" function="0x0"/>
</disk>
```
