"""This module contains the general information for BiosVfIntelVTForDirectedIO ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIntelVTForDirectedIOConsts():
    VP_INTEL_VTDATSSUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDATSSUPPORT_ENABLED = "Enabled"
    VP_INTEL_VTDATSSUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDATSSUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDATSSUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "Enabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "Disabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "Enabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "disabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "enabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "Enabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "Disabled"
    VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "Enabled"
    VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "disabled"
    VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "enabled"
    VP_INTEL_VTFOR_DIRECTED_IO_PLATFORM_DEFAULT = "platform-default"


class BiosVfIntelVTForDirectedIO(ManagedObject):
    """This is BiosVfIntelVTForDirectedIO class."""

    consts = BiosVfIntelVTForDirectedIOConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", VersionMeta.Version151f, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "vp_intel_vtdats_support": MoPropertyMeta("vp_intel_vtdats_support", "vpIntelVTDATSSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        "vp_intel_vtd_coherency_support": MoPropertyMeta("vp_intel_vtd_coherency_support", "vpIntelVTDCoherencySupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        "vp_intel_vtd_interrupt_remapping": MoPropertyMeta("vp_intel_vtd_interrupt_remapping", "vpIntelVTDInterruptRemapping", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        "vp_intel_vtd_pass_through_dma_support": MoPropertyMeta("vp_intel_vtd_pass_through_dma_support", "vpIntelVTDPassThroughDMASupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        "vp_intel_vt_for_directed_io": MoPropertyMeta("vp_intel_vt_for_directed_io", "vpIntelVTForDirectedIO", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpIntelVTDATSSupport": "vp_intel_vtdats_support", 
        "vpIntelVTDCoherencySupport": "vp_intel_vtd_coherency_support", 
        "vpIntelVTDInterruptRemapping": "vp_intel_vtd_interrupt_remapping", 
        "vpIntelVTDPassThroughDMASupport": "vp_intel_vtd_pass_through_dma_support", 
        "vpIntelVTForDirectedIO": "vp_intel_vt_for_directed_io", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_intel_vtdats_support = None
        self.vp_intel_vtd_coherency_support = None
        self.vp_intel_vtd_interrupt_remapping = None
        self.vp_intel_vtd_pass_through_dma_support = None
        self.vp_intel_vt_for_directed_io = None

        ManagedObject.__init__(self, "BiosVfIntelVTForDirectedIO", parent_mo_or_dn, **kwargs)

