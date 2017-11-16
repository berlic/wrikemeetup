#!powershell

#Requires -Module Ansible.ModuleUtils.Legacy.psm1
#Requires -Module Ansible.ModuleUtils.MyWinLib.psm1

$result = @{
    msg = Hello
}

Exit-Json -obj $result
