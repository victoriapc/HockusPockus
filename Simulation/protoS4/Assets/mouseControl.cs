using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class mouseControl : MonoBehaviour {
    // Use this for initialization
    public KeyCode up;
    public KeyCode down;
    public KeyCode left;
    public KeyCode right;
    int drag;
    void Start () {
		
	}
	
	// Update is called once per frame
	void FixedUpdate () {
        drag = 1;
        if (Input.GetKey(up))
        {
            this.GetComponent<Rigidbody2D>().AddForce(Vector2.up);
            drag = 0;
        }
        else if(Input.GetKey(down))
        {
            this.GetComponent<Rigidbody2D>().AddForce(-Vector2.up);
            drag = 0;
        }
        if(Input.GetKey(left))
        {
            this.GetComponent<Rigidbody2D>().AddForce(-Vector2.right);
            drag = 0;
        }
        else if(Input.GetKey(right))
        {
            this.GetComponent<Rigidbody2D>().AddForce(Vector2.right);
            drag = 0;
        }
        if (drag==1)
            this.GetComponent<Rigidbody2D>().drag = 10;
        else
            this.GetComponent<Rigidbody2D>().drag = 0;
        /*this.GetComponent<Rigidbody2D>().AddForce(Vector2.up*)
        this.transform.position = new Vector2(Input.mousePosition.x* 0.0180635838f, Input.mousePosition.y* 0.0180635838f);
        Debug.Log(Input.mousePosition);*/
    }
}
