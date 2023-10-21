## VSCode Pascal Compiler

---

VSCode Pascal Compiler est un module pour compiler et exécuter du pascal sur 
vscode.

Il utilise les taches et le fichier task.json de vscode pour lancer la 
compilation grâce à FreePascal. S'il n'est pas installé le programme 
l'installera automatiquement

<br>

Pour compiler, vous devez faire Ctrl+Maj+B (pour build)

Pour lancer le programme, vous devez faire Ctrl+Maj+T (pour test)

<br>

Liste des fonctionnalités :

- Quand vous compilez, le programme traduit proprement les erreurs les plus 
  courantes
- Lors de la compilation, le programme ferme les autres instances en cours 
  d'exécution pour éviter les conflicts
- Si la traduction des erreurs ne s'affiche pas correctement, compilez 2 
  fois d'affilée pour afficher le message original 
