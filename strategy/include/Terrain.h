#ifndef TERRAIN_H  
#define TERRAIN_H

#include "Vector3.h"

struct Terrain
{
	Vector2 HautGauche;
	Vector2 HautDroite;
	Vector2 BasGauche;
	Vector2 BasDroite;
	
	Vector2 butHaut;
	Vector2 butBas;
	Vector2 murGauche;
	Vector2 murDroite;
};

#endif