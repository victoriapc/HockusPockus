#include "Vector2.h"

struct Vector3
{
	Vector3():pos(0, 0),iter(0){}
	Vector3(Vector2 i_pos, int i_iter):pos(i_pos.X, i_pos.Y),iter(i_iter){}
	Vector2 pos;
	int iter;
};