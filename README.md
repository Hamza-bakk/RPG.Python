<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="RPG GAME" />

  &#xa0;

  <!-- <a href="https://rpggame.netlify.app">Demo</a> -->
</div>

<h1 align="center">RPG GAME</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Hamza-bakk/rpg-game?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Hamza-bakk/rpg-game?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Hamza-bakk/rpg-game?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/Hamza-bakk/rpg-game?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/Hamza-bakk/rpg-game?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/Hamza-bakk/rpg-game?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/Hamza-bakk/rpg-game?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  RPG GAME 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/Hamza-bakk" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Ce projet consiste en la création d'un jeu où cinq personnages s'affrontent dans des combats façon gladiateurs. Chaque personnage possède des caractéristiques telles que des points de vie (hp), des points de dégât (dmg) et des points de mana. Le but du jeu est de survivre à 10 tours, en utilisant judicieusement les attaques normales et spéciales de chaque personnage.

Les cinq classes de personnages sont les suivantes : Fighter, Paladin, Monk, Berzerker et Assassin. Chaque classe a ses propres caractéristiques et une attaque spéciale unique qui consomme des points de mana.

Les personnages du jeu sont les suivants :

- Grace (Fighter)
- Ulder (Paladin)
- Moana (Monk)
- Draven (Berzerker)
- Carl (Assassin)

Chaque personnage a une méthode pour infliger et recevoir des dégâts, ainsi qu'un statut (playing, winner ou loser). Si les points de vie d'un personnage atteignent zéro, il devient un loser et ne peut plus jouer ni être attaqué. Un personnage gagne 20 points de mana en éliminant un autre personnage.

Le jeu se déroule dans la console et est orchestré par une classe Game. Cette classe gère le déroulement des tours, enregistre le nombre de tours restants, et déclare un personnage comme gagnant lorsque les tours sont épuisés. Chaque tour consiste en l'activation de la méthode startTurn, suivie des actions de chaque personnage. Les actions sont enregistrées dans la console, et lorsque tous les personnages ont joué, le tour est sauté.

Le jeu continue jusqu'à ce qu'il ne reste qu'un personnage en vie, qui est déclaré gagnant. Les joueurs peuvent utiliser la méthode watchStats à tout moment pour afficher les statistiques des personnages et prendre des décisions tactiques.

La partie est lancée en utilisant la fonction startGame.

En résumé, ce projet est un jeu de combat entre cinq personnages, chacun ayant des caractéristiques uniques et des attaques spéciales, et le but est de survivre à 10 tours en utilisant stratégie et tactique. Le jeu est entièrement basé sur la console, et la classe Game gère le déroulement du jeu.

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python]

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/Hamza-bakk/rpg-game

# Access
$ cd rpg-game

# Install dependencies
$ pyton3 rpg.py

```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/Hamza-bakk" target="_blank">Hamza</a>

&#xa0;

<a href="#top">Back to top</a>
