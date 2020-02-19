using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class goalllllllll : MonoBehaviour {
    float timeGoal;
    public Text p1;
    public Text p2;
    public Text p3;
    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (timeGoal != 0 && Time.time - timeGoal > 2.5f)
        {
            
            this.GetComponent<Rigidbody2D>().WakeUp();
            this.transform.position = new Vector2(-0.29f, -0.38f);
            timeGoal = 0;
        }
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        
        timeGoal = Time.time;
        this.transform.position = new Vector2(0, 100);
        this.GetComponent<Rigidbody2D>().Sleep();
        tag = collision.tag;
        if(tag == "p1")
        {
            p1.text = (int.Parse(p1.text) + 1).ToString();
        }
        else if(tag == "p2")
        {
            p2.text = (int.Parse(p2.text) + 1).ToString();
        }
        else if(tag == "p3")
        {
            p3.text = (int.Parse(p3.text) + 1).ToString();
        }

    }
}
