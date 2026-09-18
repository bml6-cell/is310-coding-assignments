# Run from the nfl-qb-maze folder after unzipping on Windows.
Get-ChildItem -Recurse -Force |
    Where-Object { $_.Name.StartsWith('.') } |
    ForEach-Object { attrib +h $_.FullName }
