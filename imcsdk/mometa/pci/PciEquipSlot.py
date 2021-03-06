"""This module contains the general information for PciEquipSlot ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciEquipSlotConsts():
    pass


class PciEquipSlot(ManagedObject):
    """This is PciEquipSlot class."""

    consts = PciEquipSlotConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("PciEquipSlot", "pciEquipSlot", "equipped-slot-[id]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'computeRackUnit'], [u'faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "controller_reported": MoPropertyMeta("controller_reported", "controllerReported", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "smbios_id": MoPropertyMeta("smbios_id", "smbiosId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerReported": "controller_reported", 
        "dn": "dn", 
        "id": "id", 
        "model": "model", 
        "rn": "rn", 
        "smbiosId": "smbios_id", 
        "status": "status", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.controller_reported = None
        self.model = None
        self.smbios_id = None
        self.status = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "PciEquipSlot", parent_mo_or_dn, **kwargs)

