# Name:    CiceroCloudAPI
# Purpose: Execute the CiceroCloudAPI program

######################### Parameters ##########################
param(
    $lat = '', 
    $long = '',
    $location = '',
    $max = '',
    $license = '', 
    [switch]$quiet = $false
    )

########################## Main ############################
Write-Host "`n===================================== Melissa Cicero Cloud API ===================================`n"

# Get license (either from parameters or user input)
if ([string]::IsNullOrEmpty($license) ) {
  $license = Read-Host "Please enter your license string"
}

# Check for License from Environment Variables 
if ([string]::IsNullOrEmpty($license) ) {
  $license = $env:MD_LICENSE 
}

if ([string]::IsNullOrEmpty($license)) {
  Write-Host "`nLicense String is invalid!"
  Exit
}

# Run project
if ([string]::IsNullOrEmpty($lat) -and [string]::IsNullOrEmpty($long) -and [string]::IsNullOrEmpty($location) -and [string]::IsNullOrEmpty($max)) {
  python3 CiceroPython3.py --license $license 
}
else {
  python3 CiceroPython3.py --license $license --lat $lat --long $long --location $location --max $max
}
