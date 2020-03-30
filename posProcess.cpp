#include <math.h>

const int LEFT = -1;
const int RIGHT = 1;
const int maxIter = 50;

struct Vector2
{
	float X;
	float Y;
};

struct Vector3
{
	Vector2 pos;
	int iter;
}

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

Vector2 pos;
Vector2 posPrec;

Terrain map; 
//Calcul murs
//Calcul buts



//Fonction réception de données
void reception()
{
	pos = //Réception des données

	float A = (pos.Y - posPrec.Y)/(pos.X-posPrec.X);
	float B = pos.Y - A * pos.X;

	int dir = 0;

	if(pos.X-posPrec.X >= 0)
	{
		dir = RIGHT;
	}
	else
	{
		dir = LEFT;
	}

	Vector3 prediction;
	prediction = linePredict(A,B,dir,pos,0);
	posPrec = pos;
}

Vector3 linePredict(float A, float B, int dir, Vector2 pos, int iteration)
{
	iteration++;
	
	Vector2 posWallHit = new Vector2(0,0);
	
	float distBut = 1000;
	float distBut2 = 1000;
	float distMur = 1000;
	float distMur2 = 1000;
	
	//But robot
	float tempXBut = (B-map.butHaut.Y)/(map.butHaut.X-A);
	float tempYBut = map.butHaut.X * tempXBut + map.butHaut.Y;
	
	if((map.HautGauche.X < tempXBut) && tempXBut < map.HautDroite.X) && dir*A>0)
	{
		distBut = sqrt(pow(tempXBut-pos.X, 2) + pow(tempYBut-pos.Y,2));
	}
	
	//But joueur
	float tempXBut2 = (B-map.butBas.Y)/(map.butBas.X-A);
	float tempYBut2 = map.butBas.X * tempXBut2 + map.butBas.Y;
	
	if((map.BasGauche < tempXBut2) && tempXBut2 < map.BasDroite) && dir*A<0)
	{
		distBut2 = sqrt(pow(tempXBut2-pos.X, 2) + pow(tempYBut2-pos.Y,2));
	}
	
	
	//Mur gauche
	float tempXMur = (B-map.murGauche.Y)/(map.murGauche.X-A);
	float tempYMur = map.murGauche.X * tempXMur + map.murGauche.Y;
	
	if(tempYMur > map.BasGauche.Y && tempYMur < map.HautGauche.Y && dir < 0)
	{
		distMur = sqrt(pow(tempXMur - pos.X,2)+pow(tempYMur-pos.Y,2));
	}
	
	//Mur droite
	float tempXMur2 = (B-map.murDroite.Y)/(map.murDroite.X-A);
	float tempYMur2 = map.murDroite.X * tempXMur2 + map.murDroite.Y;
	
	if(tempYMur2 > map.BasDroite.Y && tempYMur1 < map.HautDroite.Y && dir > 0)
	{
		distMur2 = sqrt(pow(tempXMur2 - pos.X,2)+pow(tempYMur2-pos.Y,2));
	}
	
	if(distBut < distBut2 && distBut < distMur && distBut < distMur2 && iteration < maxIter)
		return new Vector3(new Vector2(tempXBut, tempYBut), iteration);
	else if(distBut2 < distBut && distBut2 < distMur && distBut2 < distMur2 && iteration < maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYBut2-A2*tempXBut2;
		return linePredict(A2,B2,dir,new Vector2(tempXBut2, tempYBut2), iteration);
	}
	else if(distMur < distBut && distMur < distBut2 && distMur < distMur2 && iteration < maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYMur-A2*tempXMur;
		int dir2 = dir*-1;
		return linePredict(A2,B2,dir2,new Vector2(tempXMur,tempYMur),iteration);
	}
	else if(distMur2 < distBut && distMur2 < distBut2 && distMur2 < distMur && iteration < maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYMur2-A2*tempXMur2;
		int dir2 = dir*-1;
		return linePredict(A2,B2,dir2,new Vector2(tempXMur2,tempYMur2),iteration);
	}
	else
		return new Vector3(new Vector2(1000, 1000), iteration);
}

