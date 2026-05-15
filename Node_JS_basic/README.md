# NodeJS Basics — Essential Recap

## Objectif du projet

Comprendre comment :

- Exécuter du JavaScript avec NodeJS  
- Lire et traiter des données CSV  
- Créer un serveur HTTP  
- Structurer un backend propre avec Express  

Finalité : construire un mini backend organisé, proche d’une API réelle.

## NodeJS

NodeJS permet d’exécuter JavaScript côté serveur, sans navigateur.

```bash
node file.js
```

## Modules

Importer un module :

```js
const fs = require'fs';
```

Exporter une fonction :

```js
module.exports = myFunction;
```

À retenir :

- `require` sert à importer  
- `module.exports` sert à exporter  

## Process et arguments CLI

`process.argv` permet de récupérer les arguments passés dans le terminal.

Exemple :

```bash
node app.js database.csv
```

```js
process.argv[2] // "database.csv"
```

## Lecture de fichiers

Lecture synchrone :

```js
fs.readFileSyncpath, 'utf-8';
```

- simple  
- bloque le programme  

Lecture asynchrone :

```js
fs.readFilepath, 'utf-8', callback;
```

- ne bloque pas le programme  
- utilisée avec callback ou Promise  

## Traitement CSV

Étapes classiques :

1. Lire le fichier  
2. Découper en lignes  
3. Enlever le header  
4. Ignorer les lignes vides  
5. Découper chaque ligne avec `split','`  
6. Regrouper les données par field  

Pattern important :

```js
if !obj[key] obj[key] = [];
obj[key].pushvalue;
```

## Serveur HTTP avec Node

Node possède un module natif `http`.

```js
const http = require'http';

const app = http.createServerreq, res => {
  res.end'Hello Holberton School!';
};

app.listen1245;
module.exports = app;
```

À retenir :

- `req` représente la requête  
- `res` représente la réponse  
- `res.end` envoie la réponse  

## Express

Express est un framework qui simplifie la création de serveurs HTTP.

```js
const express = require'express';

const app = express;

app.get'/', req, res => {
  res.send'Hello Holberton School!';
};

app.listen1245;
module.exports = app;
```

Avantages :

- routes plus propres  
- code plus lisible  
- erreurs 404 gérées automatiquement  
- meilleure structure pour une API  

## Async / Promise / Await

Une Promise représente une opération asynchrone.

```js
function readData {
  return new Promiseresolve, reject => {
    // success: resolvedata
    // error: rejecterror
  };
}
```

Avec `.then` :

```js
readData
  .thendata => {
    console.logdata;
  }
  .catcherror => {
    console.logerror;
  };
```

Avec `async/await` :

```js
try {
  const data = await readData;
} catch error {
  console.logerror;
}
```

## Flow d’une API backend

Une requête suit souvent ce chemin :

```text
Client → Route → Controller → Data → Response
```

Exemple :

```text
/students → StudentsController → readDatabase → response
```

## Structure finale de la Task 8

```text
full_server/
├── controllers/
│   ├── AppController.js
│   └── StudentsController.js
├── routes/
│   └── index.js
├── utils.js
└── server.js
```

## Rôle des fichiers

### server.js

- crée l’application Express  
- branche les routes  
- lance le serveur sur le port 1245  

### routes/index.js

- définit les endpoints  
- associe chaque URL à un controller  

Exemple :

```js
router.get'/', AppController.getHomepage;
router.get'/students', StudentsController.getAllStudents;
```

### controllers/

Les controllers gèrent la logique HTTP.

Exemple :

- recevoir une requête  
- appeler une fonction utile  
- envoyer une réponse  
- gérer les erreurs  

### utils.js

Contient la logique réutilisable.

Exemple :

- lire la database  
- transformer les données  
- retourner un objet exploitable  

## Exemple de séparation propre

Mauvais modèle :

```text
Tout dans server.js
```

Meilleur modèle :

```text
server.js → routes → controllers → utils
```

## Lien avec HBnB / Portfolio

Cette architecture ressemble à ce que tu fais déjà avec HBnB :

```text
Flask route → Resource/Controller → Facade/Service → Data
```

Ici avec Node / Express :

```text
Express route → Controller → Utils/Data → Response
```

Pour ton portfolio, ce sera le même principe :

```text
/users
/scores
/leaderboard
/games
```

Chaque route appellera une logique métier, puis renverra une réponse.

## Ce que cette task t’apprend vraiment

- organiser un backend  
- éviter les fichiers trop gros  
- séparer les responsabilités  
- créer des routes dynamiques  
- gérer des erreurs proprement  
- exposer des données via HTTP  

## Erreurs classiques

- oublier d’exporter `app`  
- oublier `export default` dans la Task 8  
- mauvais chemin d’import  
- oublier que le fichier CSV vient de `process.argv[2]`  
- mélanger route, controller et logique data  
- ne pas gérer les erreurs avec status 500  
- oublier l’ordre alphabétique des fields dans `/students`  

## À retenir absolument

```text
NodeJS = JavaScript côté serveur
Express = framework pour créer une API
Route = URL appelée par le client
Controller = fonction qui gère la requête
Utils = fonctions réutilisables
Promise = opération async
process.argv = arguments du terminal
fs = lecture de fichiers
```

## Conclusion

Le projet commence avec de simples scripts NodeJS.

Puis il évolue vers :

```text
un vrai mini backend structuré
```

À la fin, tu sais faire :

```text
lire des données → les organiser → créer des routes → répondre à un client
```

C’est exactement la base d’une API moderne.