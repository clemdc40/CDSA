---
title: Windows Privilege Escalation
tags: [privesc, windows]
os: [Windows]
difficulty: Advanced
---

Escalade de privilèges sous Windows.

!!! info
    Utilise `winPEAS.exe` pour l'énumération.

=== "pwsh"
    ```pwsh
    .\winPEAS.exe
    ```

=== "bash"
    ```bash
    smbclient \\{{ target_ip }}\C$ -U {{ domain }}\\user
    ```

!!! danger
    Les modifications du registre peuvent rendre le système instable.
