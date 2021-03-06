"""This module contains the general information for BiosVfExecuteDisableBit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfExecuteDisableBitConsts():
    VP_EXECUTE_DISABLE_BIT_DISABLED = "Disabled"
    VP_EXECUTE_DISABLE_BIT_ENABLED = "Enabled"
    VP_EXECUTE_DISABLE_BIT_DISABLED = "disabled"
    VP_EXECUTE_DISABLE_BIT_ENABLED = "enabled"
    VP_EXECUTE_DISABLE_BIT_PLATFORM_DEFAULT = "platform-default"


class BiosVfExecuteDisableBit(ManagedObject):
    """This is BiosVfExecuteDisableBit class."""

    consts = BiosVfExecuteDisableBitConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfExecuteDisableBit", "biosVfExecuteDisableBit", "Execute-Disable-Bit", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "vp_execute_disable_bit": MoPropertyMeta("vp_execute_disable_bit", "vpExecuteDisableBit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpExecuteDisableBit": "vp_execute_disable_bit", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_execute_disable_bit = None

        ManagedObject.__init__(self, "BiosVfExecuteDisableBit", parent_mo_or_dn, **kwargs)

