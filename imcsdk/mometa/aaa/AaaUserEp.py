"""This module contains the general information for AaaUserEp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import ImcVersion, MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserEpConsts():
    pass


class AaaUserEp(ManagedObject):
    """This is AaaUserEp class."""

    consts = AaaUserEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaUserEp", "aaaUserEp", "user-ext", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'topSystem'], [u'aaaSession', u'aaaUser', u'aaaUserPolicy'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "AaaUserEp", parent_mo_or_dn, **kwargs)

