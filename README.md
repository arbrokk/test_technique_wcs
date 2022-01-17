# Entretien Technique Wild Code School

## Pitch 

> Quelque part, au beau milieu des cyclades, à 500 kilomètres de Iolcos...
> 
>Tranquillement installé sur un transat au bord de la piscine de votre villa, vous vous relaxez en regardant la mer…. Mais votre tranquillité est soudainement perturbée par la sonnerie agressive de votre téléphone. C’est votre big boss Jason. Il  veut vous voir tout de suite pour constituer la liste définitive des Argonautes avec lui.

> Mince, vous avez oublié de le prévenir de votre départ pour les îles ! Pas question d’envoyer un papyrus par coursier, cela prendrait des semaines. Pas de panique, vous allez réaliser une application web dynamique comprenant un formulaire de saisie où vous et Jason ajouterez en temps réel la liste des candidats. Un peu d’acronyme CRUD, le tout enrobé dans un joli CSS, et le tour est joué.

> Qui aurait cru que la technologie était aussi avancée en Grèce antique ?

## MVP
Jason adore votre idée et s’est déjà mis au travail en vous fournissant une maquette sur CodePen[].
Cette page comporte déjà :

- un champ de formulaire permettant de saisir le nom d'un nouvel argonaute,
- la liste des argonautes déjà référencés par Jason.

Mais dans la maquette, la liste des membres d'équipage est présente "en dur".
Jason n’y connait rien en page dynamique, c’est le moment de l’épater !

Vous expliquez à votre boss que vous allez adapter cette maquette, de façon à :

- afficher les membres d'équipage récupérés depuis une base de données, à la place de ceux déjà saisis "en dur",
- stocker les noms des nouveaux membres d'équipage en base de données, lors de la validation du formulaire,
- améliorer sa mise en page, en disposant les noms des argonautes sur trois colonnes au lieu d'une seule.

Un véritable jeu d’enfants que vous allez réaliser depuis votre transat !

Pour résumer, il s'agit d'implémenter les fonctionnalités "Create" et "Read" de l'acronyme "CRUD" ! Puis d'enjoliver la présentation avec du CSS.

## Pour aider Jason, vous allez :

    Créer une application web simple dans votre langage de prédilection.
    Stocker les données de cette application dans une base de données.

L'application ne comportera qu'une seule page.

Nous imposons très peu de contraintes au niveau technique :

- Vous pouvez utiliser n'importe quel système de base de données : SQL (MySQL, PostgreSQL, etc.), NoSQL (MongoDB, etc.), voire Firebase (ou toute autre base de données "serverless")
- Vous pouvez utiliser n'importe quel langage, bibliothèque, framework, voire combinaison de plusieurs technologies : cela peut être le cas si vous travaillez avec une bibliothèque ou un framework front-end tel que React ou Angular, et que vous écrivez par ailleurs une application back-end.

Idéalement, vous pouvez publier votre travail sur un dépôt GitHub, voire déployer votre application (sur Heroku, Netlify, votre propre serveur, etc.). A défaut de déployer l'application, il faudra préparer une petite démo fonctionnelle sur votre ordinateur, et avoir le code source à portée de main, en vue de l'entretien technique avec un formateur.


## Ma Solution

Pour réaliser ce test technique, je me suis appuyé sur une stack à base de FastAPI (back en Python) et React (front en JSX).


### Back-End

Le backend est écrit en Python.
La DB est en SQLite via la lib SQLAlchemy.
La communication avec le front se fait via FastAPI :
- différents endpoints sont créés afin de mener à bien les interactions avec le front
	- /get_argonautes_list/ : return la liste de argonautes embarqués
	- /add_argonaute/{name} : ajoute l'argonaute *name* à la liste
	- /delete_argonaute/{name} : supprime l'argonaute *name* de la liste
	
### Front-End

Ecrit en ReactJS, en s'appuyant sur le framework TailwindCSS.