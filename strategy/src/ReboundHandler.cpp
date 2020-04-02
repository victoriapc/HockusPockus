#include "ReboundHandler.h"


ReboundHandler::ReboundHandler():
	m_subscriberDimensionsTerrain(n.subscribe("/table_dimensions", 1000, &ReboundHandler::initTerrain,this)),
	m_subscriberPositionActuellePuck(n.subscribe("/puck_pos", 1000,&ReboundHandler::reception,this)),
	m_publisherPositionDesiree(n.advertise<geometry_msgs::Point>("desired_pos", 1000))
{
}
		
void ReboundHandler::initTerrain(const std_msgs::Float32MultiArray i_dimensionsCotes)
{
	map.BasGauche.X = 0 ; 
	map.BasGauche.Y = 0 ; 
	
	map.HautGauche.X = map.BasGauche.X; 
	map.HautGauche.Y = i_dimensionsCotes.data[0];
	
	map.HautDroite.X = i_dimensionsCotes.data[1];
	map.HautDroite.Y = map.HautGauche.Y;
	
	map.BasDroite.X = map.HautDroite.X;
	map.BasDroite.Y = map.BasGauche.Y;
	
	map.butHaut.X = (map.HautDroite.Y-map.HautGauche.Y)/(map.HautDroite.X-map.HautGauche.X);
	map.butHaut.Y = map.HautDroite.Y - (map.butHaut.X * map.HautDroite.X);
	
	map.butBas.X = (map.BasDroite.Y-map.BasGauche.Y)/(map.BasDroite.X-map.BasGauche.X);
	map.butHaut.Y = map.BasDroite.Y - (map.butBas.X * map.BasDroite.X);
	
	if(map.BasGauche.Y == map.HautGauche.Y)
		map.murGauche.X = 10000;
	else
		map.murGauche.X = (map.HautGauche.Y-map.BasGauche.Y)/(map.HautGauche.X-map.BasGauche.X);
	map.murGauche.Y = map.HautGauche.Y- (map.murGauche.X*map.HautGauche.X);
	
	if(map.BasDroite.Y == map.HautDroite.Y)
		map.murDroite.X = 10000;
	else
		map.murDroite.X = (map.HautDroite.Y-map.BasDroite.Y)/(map.HautDroite.X-map.BasDroite.X);
	map.murDroite.Y = map.HautDroite.Y- (map.murDroite.X*map.HautDroite.X);
	
	
	
}


Vector3 ReboundHandler::linePredict(float A, float B, int dir, Vector2 pos, int iteration)
{
	iteration++;
	
	
	float distBut = 1000;
	float distBut2 = 1000;
	float distMur = 1000;
	float distMur2 = 1000;
	
	//But robot
	float tempXBut = (B-map.butHaut.Y)/(map.butHaut.X-A);
	float tempYBut = map.butHaut.X * tempXBut + map.butHaut.Y;
	
	if((map.HautGauche.X < tempXBut) && (tempXBut < map.HautDroite.X) && (dir*A>0))
	{
		distBut = sqrt(pow(tempXBut-pos.X, 2) + pow(tempYBut-pos.Y,2));
	}
	
	//But joueur
	float tempXBut2 = (B-map.butBas.Y)/(map.butBas.X-A);
	float tempYBut2 = map.butBas.X * tempXBut2 + map.butBas.Y;
	
	if((map.BasGauche.X < tempXBut2) && (tempXBut2 < map.BasDroite.X) && (dir*A<0))
	{
		distBut2 = sqrt(pow(tempXBut2-pos.X, 2) + pow(tempYBut2-pos.Y,2));
	}
	
	
	//Mur gauche
	float tempXMur = (B-map.murGauche.Y)/(map.murGauche.X-A);
	float tempYMur = map.murGauche.X * tempXMur + map.murGauche.Y;
	
	if((tempYMur > map.BasGauche.Y) && (tempYMur < map.HautGauche.Y) && (dir < 0))
	{
		distMur = sqrt(pow(tempXMur - pos.X,2)+pow(tempYMur-pos.Y,2));
	}
	
	//Mur droite
	float tempXMur2 = (B-map.murDroite.Y)/(map.murDroite.X-A);
	float tempYMur2 = map.murDroite.X * tempXMur2 + map.murDroite.Y;
	
	if((tempYMur2 > map.BasDroite.Y) && (tempYMur < map.HautDroite.Y) && (dir > 0))
	{
		distMur2 = sqrt(pow(tempXMur2 - pos.X,2)+pow(tempYMur2-pos.Y,2));
	}
	
	if(distBut < distBut2 && distBut < distMur && distBut < distMur2 && iteration < ReboundHandler::maxIter)
		return Vector3(Vector2(tempXBut, tempYBut), iteration);
	else if(distBut2 < distBut && distBut2 < distMur && distBut2 < distMur2 && iteration < ReboundHandler::maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYBut2-A2*tempXBut2;
		return linePredict(A2,B2,dir, Vector2(tempXBut2, tempYBut2), iteration);
	}
	else if(distMur < distBut && distMur < distBut2 && distMur < distMur2 && iteration < ReboundHandler::maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYMur-A2*tempXMur;
		int dir2 = dir*-1;
		return linePredict(A2,B2,dir2, Vector2(tempXMur,tempYMur),iteration);
	}
	else if(distMur2 < distBut && distMur2 < distBut2 && distMur2 < distMur && iteration < ReboundHandler::maxIter)
	{
		float A2 = A*-1;
		float B2 = tempYMur2-A2*tempXMur2;
		int dir2 = dir*-1;
		return linePredict(A2,B2,dir2, Vector2(tempXMur2,tempYMur2),iteration);
	}
	else
		return Vector3(Vector2(pos.X, 0.05), iteration);
}

void ReboundHandler::reception(const geometry_msgs::Point i_puckPos)
{
	pos.X = i_puckPos.x ; 
	pos.Y = i_puckPos.y ; 

	float A = (pos.Y - posPrec.Y)/(pos.X-posPrec.X);
	float B = pos.Y - A * pos.X;

	int dir = 0;

	if(pos.X-posPrec.X >= 0)
	{
		dir = ReboundHandler::RIGHT;
	}
	else
	{
		dir = ReboundHandler::LEFT;
	}

	Vector3 prediction;
	prediction = linePredict(A,B,dir,pos,0);
	predictionToDesiredPosition(prediction.pos);
	posPrec = pos;
}
	
