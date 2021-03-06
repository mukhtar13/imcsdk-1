"""This module contains the general information for BiosVfLegacyUSBSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLegacyUSBSupportConsts():
    VP_LEGACY_USBSUPPORT_AUTO = "Auto"
    VP_LEGACY_USBSUPPORT_DISABLED = "Disabled"
    VP_LEGACY_USBSUPPORT_ENABLED = "Enabled"
    VP_LEGACY_USBSUPPORT_AUTO = "auto"
    VP_LEGACY_USBSUPPORT_DISABLED = "disabled"
    VP_LEGACY_USBSUPPORT_ENABLED = "enabled"
    VP_LEGACY_USBSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfLegacyUSBSupport(ManagedObject):
    """This is BiosVfLegacyUSBSupport class."""

    consts = BiosVfLegacyUSBSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfLegacyUSBSupport", "biosVfLegacyUSBSupport", "LegacyUSB-Support", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "vp_legacy_usb_support": MoPropertyMeta("vp_legacy_usb_support", "vpLegacyUSBSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpLegacyUSBSupport": "vp_legacy_usb_support", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_legacy_usb_support = None

        ManagedObject.__init__(self, "BiosVfLegacyUSBSupport", parent_mo_or_dn, **kwargs)

