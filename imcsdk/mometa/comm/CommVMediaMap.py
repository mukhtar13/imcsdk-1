"""This module contains the general information for CommVMediaMap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommVMediaMapConsts():
    DRIVE_TYPE_CD = "cd"
    DRIVE_TYPE_FLOPPY = "floppy"
    MAP_CIFS = "cifs"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class CommVMediaMap(ManagedObject):
    """This is CommVMediaMap class."""

    consts = CommVMediaMapConsts()
    naming_props = set([u'volumeName'])

    mo_meta = MoMeta("CommVMediaMap", "commVMediaMap", "vmmap-[volume_name]", VersionMeta.Version151f, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], [u'commVMedia'], [], ["Add", "Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], []), 
        "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["cifs", "nfs", "www"], []), 
        "mapping_status": MoPropertyMeta("mapping_status", "mappingStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 1, 248, None, [], []), 
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []), 
        "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []), 
        "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "driveType": "drive_type", 
        "map": "map", 
        "mappingStatus": "mapping_status", 
        "mountOptions": "mount_options", 
        "password": "password", 
        "remoteFile": "remote_file", 
        "remoteShare": "remote_share", 
        "rn": "rn", 
        "status": "status", 
        "username": "username", 
        "volumeName": "volume_name", 
    }

    def __init__(self, parent_mo_or_dn, volume_name, **kwargs):
        self._dirty_mask = 0
        self.volume_name = volume_name
        self.child_action = None
        self.drive_type = None
        self.map = None
        self.mapping_status = None
        self.mount_options = None
        self.password = None
        self.remote_file = None
        self.remote_share = None
        self.status = None
        self.username = None

        ManagedObject.__init__(self, "CommVMediaMap", parent_mo_or_dn, **kwargs)

