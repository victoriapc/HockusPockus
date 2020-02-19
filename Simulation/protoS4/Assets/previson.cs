using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class previson : MonoBehaviour {
    public Transform rondelle;
    Vector2 posRondelle;
    Vector2 currentPosRondelle;
    Vector2 prevPosRondelle;
    public Vector2 prediction;
    const int LEFT = -1;
    const int RIGHT = 1;
    const int maxIter = 50;

    const float yBUT = 4.6f;//5.77f;
    const float yZone = 1.41f;
    const float x1Mur = -2.7f;
    const float x2Mur = 2.1f;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void FixedUpdate () {
        posRondelle = rondelle.position;
        currentPosRondelle = posRondelle;
        float A = (currentPosRondelle.y - prevPosRondelle.y) / (currentPosRondelle.x - prevPosRondelle.x);
        float B = currentPosRondelle.y - A * currentPosRondelle.x;
        //Debug.Log("y = " + A + "x + " + B);
        int dir = 0;
        if (currentPosRondelle.x - prevPosRondelle.x >= 0)
        {
            dir = RIGHT;
        }
        else
        {
            dir = LEFT;
        }
        prediction = linePredict(A, B, dir,currentPosRondelle, 0);
        //Debug.Log(prediction);

        prevPosRondelle = currentPosRondelle;
	}

    Vector2 linePredict(float A, float B, int dir, Vector2 pos, int iteration)
    {
        iteration ++;
        int wallHit = 0;

        Vector2 posWallHit = new Vector2(0, 0);
        //RaycastHit2D hit = Physics2D.Raycast(pos, new Vector2(1, A) * dir);
        
               
        float distBut = 1000;
        float distMur1 = 1000;
        float distMur2 = 1000;
        
        //Mur but
        float tempXBut = (yBUT - B) / A;
        
        if ((x1Mur < tempXBut) && (tempXBut < x2Mur)&&dir*A > 0)
        {
            distBut = Mathf.Sqrt(Mathf.Pow(tempXBut - pos.x, 2) + Mathf.Pow(yBUT - pos.y, 2));
            //Debug.DrawLine(pos, new Vector2(tempXBut,yBUT), Color.red);

        }
        
        //Mur 1
        float tempYMur1 = (A * x1Mur + B);
        if(yZone < tempYMur1 && tempYMur1 < yBUT && dir<0)
        {
            distMur1 = Mathf.Sqrt(Mathf.Pow(x1Mur - pos.x, 2) + Mathf.Pow(tempYMur1 - pos.y,2));
        }

        //Mur 2
        float tempYMur2 = (A * x2Mur + B);
        if (yZone < tempYMur2 && tempYMur2 < yBUT && dir > 0)
        {
            distMur2 = Mathf.Sqrt(Mathf.Pow(x2Mur - pos.x, 2) + Mathf.Pow(tempYMur2 - pos.y, 2));
        }
        //Debug.Log(tempXBut + " " + tempYMur1 + " " + tempYMur2);
        
        if (distBut < distMur1 && distBut < distMur2 && iteration < maxIter && A*dir>0)//But
        {
            //Debug.Log(tempXBut);
            Debug.DrawLine(pos, new Vector2(tempXBut, yBUT), Color.red);
            return new Vector2(tempXBut, yBUT);
        }
        else if (distMur1 < distMur2 && distMur1 < distBut && iteration < maxIter)//Mur1
        {
            float A2 = A * -1;
            float B2 = tempYMur1-A2*x1Mur;
            int dir2 = dir * -1;
            Debug.DrawLine(pos, new Vector2(x1Mur, tempYMur1), Color.red);
            return linePredict(A2,B2,dir2,new Vector2(x1Mur,tempYMur1),iteration);
        }
        else if (distMur2 < distBut && distMur2 < distMur1 && iteration<maxIter)//Mur2
        {
            float A2 = A * -1;
            float B2 = tempYMur2 - A2 * x2Mur;
            int dir2 = dir * -1;
            Debug.DrawLine(pos, new Vector2(x2Mur, tempYMur2), Color.red);
            return linePredict(A2, B2, dir2, new Vector2(x2Mur, tempYMur2), iteration);
        }
        else
            return new Vector2(Mathf.Infinity, Mathf.Infinity);
           
    }
}
