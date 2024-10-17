""" PyStorm Hivestorm Script """
__author__ = 'SystematicSkid, Campinator, and AlecHoward76'


from modules.ssh import SSHPolicyScanner
from modules.userandgroup import UserGroupPolicyScanner
from modules.net import NetworkConfigScanner
from modules.pam import PAMPolicyScanner
from modules.logindefs import LoginDefsPolicyScanner
from modules.sysctl import SysCtlPolicyScanner
from modules.media import MediaPolicyScanner


if __name__ == '__main__':
    # Define our entrypoint, always '/'
    entrypoint = '/'

    # Show stylized header
    print( '----------------------------------------' )
    print( 'PyStorm v1.0 - Python Security Auditing' )
    print( 'University of Tulsa - 2023' )
    print( '----------------------------------------' )
    print( '' )

    # Run ssh scan
    ssh_policy = SSHPolicyScanner( entrypoint )
    ssh_policy.audit_all( )

    #pam_policy = PAMPolicyScanner( entrypoint )
    
    #uncomment when ready
    #logindef_policy = LoginDefsPolicyScanner( entrypoint )
    #logindef_policy.audit_all( )
    
    sysctl_policy = SysCtlPolicyScanner( entrypoint )
    sysctl_policy.audit_all()
    
    #print( 'Media Files' )
    media_policy = MediaPolicyScanner( entrypoint )
    media_policy.find_media_files

    # Run user and group fan
    usergroup_policy = UserGroupPolicyScanner( entrypoint )
    usergroup_policy.audit_all( )

    # Run network scan
    network_policy = NetworkConfigScanner ( entrypoint )
    network_policy.audit_all( )

