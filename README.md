# download-counter-episodes

## Français

Séparer téléchargements observés, remises à zéro et totaux inconnus.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m download_counter_episodes examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Transforme les captures de compteurs cumulés en reçus par actif : référence initiale séparée, différences temporelles et baisses inconnues. Une baisse ne devient ni zéro ni de nouveaux téléchargements inventés.

### Limites

Interprétation conditionnelle à l’absence de réinitialisation ou correction cachée. Les actifs remplacés restent séparés ; aucun compteur ne prouve utilisateurs humains, installations ou adoption.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Separate observed downloads, counter resets and unknown totals.

Synthetic data; no network access or secret required.

```sh
python -m download_counter_episodes examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Turns cumulative-counter snapshots into per-asset receipts: separate initial baseline, time deltas and unknown decreases. A decrease becomes neither zero nor invented new downloads.

### Limits

Interpretation assumes no hidden reset or correction. Replacement assets remain separate; no counter proves human users, installations or adoption.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Separar descargas observadas, reinicios y totales desconocidos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m download_counter_episodes examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Transforma capturas de contadores acumulados en recibos por activo: base inicial separada, diferencias temporales y descensos desconocidos. Un descenso no se vuelve cero ni descargas inventadas.

### Límites

Interpretación condicionada a ausencia de reinicios o correcciones ocultas. Activos reemplazados separados; ningún contador prueba usuarios humanos, instalaciones o adopción.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.github.com/en/rest/releases/assets#get-a-release-asset
