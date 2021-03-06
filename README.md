# Entretien Technique Wild Code School

## MVP
- afficher les membres d'équipage récupérés depuis une base de données, à la place de ceux déjà saisis "en dur",
- stocker les noms des nouveaux membres d'équipage en base de données, lors de la validation du formulaire,
- améliorer sa mise en page, en disposant les noms des argonautes sur trois colonnes au lieu d'une seule.

- Créer une application web simple dans votre langage de prédilection.
- Stocker les données de cette application dans une base de données.

Peu de contraintes imposées :

- Vous pouvez utiliser n'importe quel système de base de données : SQL (MySQL, PostgreSQL, etc.), NoSQL (MongoDB, etc.), voire Firebase (ou toute autre base de données "serverless")
- Vous pouvez utiliser n'importe quel langage, bibliothèque, framework, voire combinaison de plusieurs technologies : cela peut être le cas si vous travaillez avec une bibliothèque ou un framework front-end tel que React ou Angular, et que vous écrivez par ailleurs une application back-end.

Idéalement, vous pouvez publier votre travail sur un dépôt GitHub, voire déployer votre application (sur Heroku, Netlify, votre propre serveur, etc.). A défaut de déployer l'application, il faudra préparer une petite démo fonctionnelle sur votre ordinateur, et avoir le code source à portée de main, en vue de l'entretien technique avec un formateur.


## Ma Solution

Pour réaliser ce test technique, je me suis appuyé sur une stack à base de FastAPI (back en Python) et React (front en JSX).


### Back-End

Le backend est écrit en Python basé sur FastAPI.
La DB est en SQLite via la lib SQLAlchemy.
- différents endpoints sont créés afin de mener à bien les interactions avec le front
	- /get_argonautes_list/ : return la liste de argonautes embarqués
	- /add_argonaute/{name} : ajoute l'argonaute *name* à la liste
	- /delete_argonaute/{name} : supprime l'argonaute *name* de la liste
	
### Front-End

Ecrit en ReactJS, en s'appuyant sur le framework TailwindCSS.
