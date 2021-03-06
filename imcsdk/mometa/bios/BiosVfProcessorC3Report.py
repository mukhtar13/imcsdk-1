"""This module contains the general information for BiosVfProcessorC3Report ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfProcessorC3ReportConsts():
    VP_PROCESSOR_C3_REPORT_DISABLED = "Disabled"
    VP_PROCESSOR_C3_REPORT_ENABLED = "Enabled"
    VP_PROCESSOR_C3_REPORT_DISABLED = "disabled"
    VP_PROCESSOR_C3_REPORT_ENABLED = "enabled"
    VP_PROCESSOR_C3_REPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfProcessorC3Report(ManagedObject):
    """This is BiosVfProcessorC3Report class."""

    consts = BiosVfProcessorC3ReportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfProcessorC3Report", "biosVfProcessorC3Report", "Processor-C3-Report", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "vp_processor_c3_report": MoPropertyMeta("vp_processor_c3_report", "vpProcessorC3Report", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpProcessorC3Report": "vp_processor_c3_report", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_processor_c3_report = None

        ManagedObject.__init__(self, "BiosVfProcessorC3Report", parent_mo_or_dn, **kwargs)

