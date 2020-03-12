struct Vector2
{
	float X;
	float Y;
};

Vector2 pos;
Vector2 posPrec;

Vector2 deltaPos;

deltaPos.X = pos.X - posPrec.X;
deltaPos.Y = pos.Y - posPrec.Y;

