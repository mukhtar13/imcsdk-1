"""This module contains the general information for IodController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IodControllerConsts():
    pass


class IodController(ManagedObject):
    """This is IodController class."""

    consts = IodControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("IodController", "iodController", "iod", VersionMeta.Version152, "OutputOnly", 0xf, [], ["read-only"], [u'topSystem'], [u'iodSnapshotCancel', u'iodSnapshotStart', u'iodSnapshotStatus'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version152, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "IodController", parent_mo_or_dn, **kwargs)

