from rtslib_fb import UserBackedStorageObject, RBDStorageObject

from ceph_iscsi_config.utils import CephiSCSIError

USER_RBD = 'user:rbd'
RBD = 'rbd'


def lookup_storage_object(name, backstore):
    if backstore == USER_RBD:
        return UserBackedStorageObject(name=name)
    elif backstore == RBD:
        return RBDStorageObject(name=name)
    else:
        raise CephiSCSIError("Could not lookup storage object - "
                             "Unsupported backstore {}".format(backstore))
