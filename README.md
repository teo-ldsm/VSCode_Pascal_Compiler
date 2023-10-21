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

---
### Installation :

Vous pouvez installer automatiquement avec l'installateur
[présent ici](https://github.com/teo-ldsm/VSCode_Pascal_Compiler/releases/latest)

Sinon, vous pouvez installer le programme en copiant manuellement les 
fichiers dans les répertoires suivants :
```tasks.json``` / ```keybindings.json``` --> 
AppData\Roaming\Code\User

```pascal_compiler.py``` / ```pascal_error_displayer``` --> 
AppData\Roaming\Code\User\PascalCompiler

---

### Liste des fonctionnalités :

- Quand vous compilez, le programme traduit proprement les erreurs les plus 
  courantes
- Lors de la compilation, le programme ferme les autres instances en cours 
  d'exécution pour éviter les conflicts
- Si la traduction des erreurs ne s'affiche pas correctement, compilez 2 
  fois d'affilée pour afficher le message original 
