Param(
[ValidateSet("x86", "x64")]
[string]$Platform="x64"
)

. "./project.ps1"

$p = [Postgres]::new()
echo $p.id
